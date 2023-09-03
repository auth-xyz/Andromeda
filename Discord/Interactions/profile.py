from nextcord import SlashOption, Interaction
from nextcord.ext import commands

bot = commands.Bot()


class int_profile:
    def __init__(self):
        ...

    @bot.slash_command(guild_ids=[1070169312284917860], description="Outputs your profile")
    async def profile(self, interaction: Interaction, arg: str = SlashOption(name="user", required=False)):
        await interaction.send(content="Test")


def setup(dbot):
    dbot.add_cog(int_profile())
