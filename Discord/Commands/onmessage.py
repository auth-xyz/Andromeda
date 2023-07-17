import nextcord 
import pymongo

from os import getenv
from dotenv import load_dotenv
from nextcord.ext import commands

client = pymongo.MongoClient(getenv("DB_L"))
db = client["Dataset"]
col = db["Chatlogs"]

class Command_ARSP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_create(self, message):
        if message.author == self.bot.user:
            return

        word = message.content.lower()

        # Check if the word exists in the autoresponse collection
        document = col.find_one({"word": word})
        if document:
            response = document["response"]
            await message.reply(response)
        
    @commands.command(name="arsp_add")
    async def add_query(self, ctx, word: str, response: str):
        payload = { "query": word, "value": response }
        col.insert_one(payload)
        await ctx.reply("Done.")
        
def setup(bot):
    bot.add_cog(Command_ARSP(bot))