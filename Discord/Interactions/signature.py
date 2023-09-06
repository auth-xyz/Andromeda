import os

import pymongo
from dotenv import load_dotenv
from nextcord import Interaction, Member, SlashOption, DiscordException
from nextcord.ext import commands
import nextcord


dbot = commands.Bot()
load_dotenv()

client = pymongo.MongoClient(os.getenv("DB_L"))
db = client["Registration"]
col = db["Users"]

class int_sign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    async def sign(self, interaction: Interaction, signature: str = SlashOption(required=True)):
        query = {"user_id": interaction.user.id}
        profile = col.find_one(query)

        if not profile:
            return interaction.send(ephemeral=True, content="You must register first")

        signature = signature[:255]
        col.update_one(query, {"$set": {"signature": signature}})
        await interaction.send(ephemeral=True, content="Done.")


def setup(bot):
    bot.add_cog(int_sign(bot))
