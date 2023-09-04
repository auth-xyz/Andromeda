import pymongo

from os import getenv
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()
client = pymongo.MongoClient(getenv("DB_L"))
db = client["Dataset"]
col = db["Chatlogs"]


class Command_ARSP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="arsp_add")
    async def add_query(self, ctx, word: str, response: str):
        payload = {"query": word, "value": response}
        col.insert_one(payload)
        await ctx.reply("Done.")

    @commands.command(name="arsp_remove")
    async def remove_query(self, ctx, word: str):
        payload = {"query": word}
        col.delete_one(payload)
        await ctx.reply("Done.")


def setup(bot):
    bot.add_cog(Command_ARSP(bot))
