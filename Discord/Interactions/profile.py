import nextcord
import os

from nextcord import SlashOption, Interaction, Embed
from Utils.database import Database
from nextcord.ext import commands
from dotenv import load_dotenv

client = commands.Bot()
load_dotenv()

db = Database(os.getenv("DB_L"), "Registration", "Users")
db.connect()


class intProfile(commands.Cog):
    def __init__(self):
        ...

    @client.slash_command(guild_ids=[1070169312284917860], description="Outputs your profile", name="profile")
    async def profile(self, interaction: Interaction, arg: nextcord.Member = SlashOption(name="user", required=False)):
        if arg:
            query = {"user_id": arg.id}
        else:
            query = {"user_id": interaction.user.id}
        profile = db.find_document(query)

        if not profile:
            await interaction.send(content="You have yet to register!", ephemeral=True)

        signature = profile["signature"]
        if not arg:
            author = interaction.user.name
            author_avatar = interaction.user.display_avatar
            join_date = interaction.user.joined_at
        else:
            author = arg.name
            author_avatar = arg.display_avatar
            join_date = arg.joined_at

        formatted = join_date.strftime("%Y-%m-%d %H:%M:%S")

        embed = Embed(
            title=f"{author}'s Profile",
            description=f"Signature:\n```\n{signature}\n```\n",
            color=0x000
        )

        embed.set_thumbnail(url=author_avatar)
        embed.add_field(name="Joined At", value=formatted, inline=True)
        embed.add_field(name="Admin", value=profile["admin"], inline=True)
        embed.add_field(name="Andromeda Usage", value=profile["Andromeda Usage"], inline=True)
        embed.set_footer(text="Andromeda Chatbot © - 2023")

        await interaction.send(embed=embed)


def setup(dbot):
    dbot.add_cog(intProfile())
