import os
import pymongo
import nextcord
from nextcord import Interaction

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("DB_L"))
db = client["Dataset"]
col = db["Chatlogs"]
dbot = commands.Bot()


class int_register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    async def register(self, interaction: Interaction):
        author = interaction.user
        author_admin = False
        author_avatar = author.display_avatar

        if author.guild_permissions.ban_members:
            author_admin = True

        embed = nextcord.Embed(
            title=f"{author.display_name} : {author.id}",
            description="```\n> Registration Complete!\n> Thank you for registering, now just wait until the AI is "
                        "finished, afterwards use '!ax' to talk with it!\n```",
            color=0x000
        )
        embed.set_thumbnail(url=author_avatar)
        embed.set_footer(text="Andromeda Chatbot © - 2023")
        payload = {"signature": "", "admin": author_admin, "username": author.name, "user_id": author.id,
                   "Andromeda Usage": 0}
        search_payload = {"user_id": author.id}

        if col.find_one(search_payload):
            return await interaction.send("You are already registered.")
        else:
            col.insert_one(payload)
            await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(int_register(bot))
