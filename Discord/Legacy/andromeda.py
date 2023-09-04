import json
import aiohttp
import pymongo

from os import getenv
from nextcord.ext import commands

NAME = "Andromeda"
GUID = getenv("GUILD_ID")
URL = getenv("API_URL")
KEY = getenv("API_KEY")

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": KEY,
    "X-RapidAPI-Host": "aeona3.p.rapidapi.com"
}

client = pymongo.MongoClient(getenv("DB_L"))
db = client["Registration"]
col = db["Users"]
ai_situation = "We're having a chill conversation"


class Command_Andromeda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.command(name="ax", description="Talk with Andromeda")
    # async def hx_command(self, ctx, *, query):
    #     async with ctx.typing():
    #         context = None
    #         res = await self.ai_query(query, ctx.author.id, ctx.author.display_name, context)
    #         await ctx.send(res)

    @staticmethod
    async def ai_query(query, user_id, user_name, context=None):
        search_payload = {"user_id": user_id}
        user_profile = col.find_one(search_payload)
        usage = user_profile["Andromeda Usage"]
        usage = usage + 1

        modify_payload = {"$set": {"Andromeda Usage": usage}}
        if not search_payload:
            return

        query_string = {
            "userId": user_id,
            "text": query,
            "chatbot": NAME,
            "context": ai_situation
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
    bot.add_cog(Command_Andromeda(bot))
