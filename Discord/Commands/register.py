import os
import pymongo
import nextcord

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("DB_L"))
db = client["Registration"]
col = db["Users"]


class Command_Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="register", description="Registers the user to the database")
    async def register(self, ctx):
        author = ctx.author
        author_admin = False
        author_avatar = author.display_avatar

        if author.guild_permissions.ban_members:
            author_admin = True

        embed = nextcord.Embed(
            title=f"{author.display_name} : {author.id}",
            description="```\n> Registration Complete!\n> Thank you for registering, now just wait until the AI is finished, afterwards use '!hx' to talk with it!\n```",
            color=0x000
        )
        embed.set_thumbnail(url=author_avatar)
        embed.set_footer(text="Andromeda Chatbot © - 2023")
        payload = {"signature": "", "admin": author_admin, "username": author.name, "user_id": author.id,
                   "Andromeda Usage": 0}
        search_payload = {"user_id": author.id}

        if col.find_one(search_payload):
            return await ctx.reply("You are already registered.")
        else:
            col.insert_one(payload)
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Command_Register(bot))
