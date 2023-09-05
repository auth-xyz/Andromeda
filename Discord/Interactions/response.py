import nextcord
import pymongo

from os import getenv
from dotenv import load_dotenv
from nextcord import Interaction, SlashOption, Permissions
from nextcord.ext import commands

load_dotenv()
client = pymongo.MongoClient(getenv("DB_L"))
db = client["Dataset"]
col = db["Chatlogs"]
dbot = commands.Bot()


class int_response(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860], description="Adds a response", name="add_response")
    @commands.has_permissions(ban_members=True)
    async def add_query(self, interaction: Interaction, trigger: str = SlashOption(required=True),
                        response: str = SlashOption(required=True)):
        payload = {"query": trigger, "value": response}
        if not payload:
            return

        col.insert_one(payload)
        await interaction.send(content="Done.", ephemeral=True)

    @dbot.slash_command(guild_ids=[1070169312284917860], description="Removes a response", name="rem_response")
    @commands.has_permissions(ban_members=True)
    async def remove_query(self, interaction: Interaction, arg: str = SlashOption(required=True, name="trigger")):
        payload = {"query": arg}
        if not payload:
            return

        col.delete_one(payload)
        await interaction.send(content="Done.", ephemeral=True)


def setup(bot):
    bot.add_cog(int_response(bot))
