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
        payload = { "query": message.content }
        document = await self.collection.find_one(payload)

        if document:
            response = document["value"]
            await message.reply(text=response)
        
    @commands.command(name="arsp_add")
    async def add_query(self, ctx, word: str, response: str):
        word = word.lower()
        payload = { "value": word }
        await col.insert_one(payload)
        await ctx.reply("Done.")
        
