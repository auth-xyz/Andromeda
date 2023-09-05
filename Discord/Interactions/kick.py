from nextcord import Interaction, Embed, Member, SlashOption, DiscordException, Permissions
from nextcord.ext import commands


dbot = commands.Bot()


class int_kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, user: Member = SlashOption(required=True),
                   reason: str = SlashOption(required=False)):
        try:
            await user.kick(reason=reason)
            await interaction.send(content=f"Kicked {user}")
        except DiscordException as e:
            print(e)


def setup(bot):
    bot.add_cog(int_kick(bot))
