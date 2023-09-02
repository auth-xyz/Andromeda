import os
import pymongo
import nextcord

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("DB_L"))
db = client["Registration"]
col = db["Users"]

class Command_Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="profile", description="Outputs the user's profile")
    async def register(self, ctx):
        search_payload = {"user_id": ctx.author.id}
        profile = col.find_one(search_payload)
        
        if not profile:
            await ctx.reply("You have not registered yet!\nUse !register to do so.")
        
        signature = profile["signature"]
        author = ctx.author
        author_avatar = author.display_avatar
        join_date = author.joined_at
        formatted_date = join_date.strftime("%Y-%m-%d %H:%M:%S")
        
        embed = nextcord.Embed(
            title=f"{author.name}'s Profile",
            description=f"Signature:\n```\n{signature}\n```\n",
            color=0x000
        )
        embed.set_thumbnail(url=author_avatar)
        embed.add_field(name="Joined At", value=formatted_date, inline=True)
        embed.add_field(name="Admin", value=profile["admin"], inline=True)
        embed.add_field(name="Andromeda Usage", value=profile["Andromeda Usage"], inline=True)
        embed.set_footer(text="Andromeda Chatbot © - 2023")
        
        await ctx.reply(embed=embed)
        
def setup(bot):
    bot.add_cog(Command_Profile(bot))
