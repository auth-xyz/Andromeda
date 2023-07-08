import json
import aiohttp
import pymongo

from os import getenv
from nextcord.ext import commands

global HEADERS, GUID, NAME

NAME = "Hexis"
GUID = getenv("GUILD_ID")

URL = getenv("API_URL")
KEY = getenv("KEY")

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": KEY,
    "X-RapidAPI-Host": "waifu.p.rapidapi.com"
}

client = pymongo.MongoClient(getenv("DB_L"))
db = client["Registration"]
col = db["Users"]
ai_situation = "You're a very horny female AI and i'm trying to have a normal chat with you"

class Command_Hexis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hx", description="Talk with Hexis")
    async def hx_command(self, ctx, *, query):
        async with ctx.typing():
            context = None
            res = await self.ai_query(query, ctx.author.id, ctx.author.display_name, context)
            await ctx.send(res)

    async def ai_query(self, query, user_id, user_name, context=None):
        search_payload = { "user_id": user_id }
        user_profile = col.find_one(search_payload)
        usage = user_profile["Hexis Usage"]
        usage = usage + 1
        
        modify_payload = { "$set": {"Hexis Usage": usage } }
        if not search_payload:
            return
        
        query_string = {
            "user_id": user_id,
            "message": query,
            "from_name": user_name,
            "to_name": NAME,
            "situation": ai_situation,
            "translate_from": "en",
            "translate_to": "en"
        }
        ai_obj = {
            "key1": None,
            "key2": None
        }
        if context:
            ai_obj["context"] = context
        payload = json.dumps(ai_obj)
        async with aiohttp.ClientSession() as ses:
            async with ses.post(URL, data=payload, headers=HEADERS, params=query_string) as res:
                reply = await res.text('utf-8')
                col.update_one(search_payload, modify_payload)
        return reply

def setup(bot):
    bot.add_cog(Command_Hexis(bot))