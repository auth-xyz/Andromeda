import nextcord
import pymongo

from nextcord.ext import commands
from os import getenv

client = pymongo.MongoClient(getenv("DB_L"))
db = client["Registration"]
col = db["Users"]


class Command_Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="update", description="Updates the bot")
    async def update(self, ctx):
        if not ctx.author.id == 1007441934652030986:
            return await ctx.reply("Only @auth.ca can use this command!")

        update_query = {"Andromeda Usage": {"$exists": True}}
        update_payload = {"$set": {"Andromeda Usage": 0}}

        result = col.update_many(update_query, update_payload)
        if result.modified_count > 0:
            embed = nextcord.Embed(
                title="Update Request",
                description=f"```\n[mongo.db] : updated [{result.modified_count}] entry(ies)```"
            )
            print(f"\n[mongo.db] : updated [{result.modified_count}] entry(ies)")
            await ctx.reply(embed=embed)
        else:
            nan_embed = nextcord.Embed(
                title="Update Request",
                description="```[mongo.db] : no entry(ies) to update were found.```"
            )
            print(f"[mongo.db] : no entry(ies) to update were found.")
            await ctx.reply(embed=nan_embed)


def setup(bot):
    bot.add_cog(Command_Update(bot))
