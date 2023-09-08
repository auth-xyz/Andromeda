import os

from dotenv import load_dotenv
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

from Utils.database import Database

client = commands.Bot()
load_dotenv()

db = Database(os.getenv("DB_L"), "Registration", "Users")
db.connect()


class int_sign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.slash_command(guild_ids=[1070169312284917860])
    async def sign(self, interaction: Interaction, signature: str = SlashOption(required=True)):
        query = {"user_id": interaction.user.id}
        profile = db.find_document(query)

        if not profile:
            return interaction.send(ephemeral=True, content="You must register first")

        signature = signature[:255]
        db.update_document(query, {"signature": signature})
        await interaction.send(ephemeral=True, content="Done.")


def setup(bot):
    bot.add_cog(int_sign(bot))
