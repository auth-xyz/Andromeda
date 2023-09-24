from nextcord import Interaction, Member, SlashOption, DiscordException
from nextcord.ext import commands

dbot = commands.Bot()


class IntUnban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(ban_members=True)
    async def unban(self, interaction: Interaction, user: Member = SlashOption(required=True),
                    reason: str = SlashOption(required=False)):
        try:
            await user.unban(reason=reason)
            await interaction.send(content=f"Done.", ephemeral=True)
        except DiscordException as e:
            print(e)


def setup(bot):
    bot.add_cog(IntUnban(bot))
