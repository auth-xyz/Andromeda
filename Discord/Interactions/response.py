import nextcord
import pymongo

from os import getenv
from dotenv import load_dotenv
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

client = pymongo.MongoClient(getenv("DB_L"))
db = client["Dataset"]
col = db["Chatlogs"]
dbot = commands.Bot()


class int_response(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860], description="Adds a response", name="add_response")
    async def add_query(self, interaction: Interaction, trigger: str = SlashOption(required=True),
                        response: str = SlashOption(required=True)):
        payload = {"query": trigger, "value": response}
        if not payload:
            return

        col.insert_one(payload)
        await interaction.send(content="Done.")

    @dbot.slash_command(guild_ids=[1070169312284917860], description="Removes a response", name="rem_response")
    async def remove_query(self, interaction: Interaction, arg: str = SlashOption(required=True, name="trigger")):
        payload = {"query": arg}
        if not payload:
            return

        col.delete_one(payload)
        await interaction.send(content="Done.")


def setup(bot):
    bot.add_cog(int_response(bot))
