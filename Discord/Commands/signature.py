import os
import pymongo

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("DB_L"))
db = client["Registration"]
col = db["Users"]

class Command_Signature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="signature", description="Updates the user's signature quote")
    async def register(self, ctx, *, signature):
        search_payload = {"user_id": ctx.author.id}
        profile = col.find_one(search_payload)
        
        if not profile:
            await ctx.reply("You have not registered yet!\nUse !register to do so.")
        
        signature = signature[:255]
        col.update_one(search_payload, {"$set": {"signature": signature}})
        await ctx.reply("Successfully updated your signature!")

        
def setup(bot):
    bot.add_cog(Command_Signature(bot))
