from nextcord import Interaction, Embed, Member, SlashOption, DiscordException
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

dbot = commands.Bot()


class int_unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    @has_permissions(ban_members=True)
    async def unban(self, interaction: Interaction, user: Member = SlashOption(required=True),
                    reason: str = SlashOption(required=False)):
        try:
            await user.unban(reason=reason)
            await interaction.send(content=f"Unbanned {user}")
        except DiscordException as e:
            print(e)


def setup(bot):
    bot.add_cog(int_unban(bot))
