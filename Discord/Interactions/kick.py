from nextcord import Interaction, Member, SlashOption, DiscordException
from nextcord.ext import commands
import nextcord


dbot = commands.Bot()


class int_kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, user: Member = SlashOption(required=True),
                   reason: str = SlashOption(required=False)):
        text = f"{user.name} has been kicked."
        pu_desc = f"```\nModerator: {interaction.user.display_name}"
        pr_desc = f"```\nModerator: {interaction.user.display_name}\nReason: {reason}"
        public_channel = dbot.get_channel(1070188919192305744)
        private_channel = dbot.get_channel(1070569664599556146)

        public_embed = nextcord.Embed(
            title=text,
            description=pu_desc,
            colour=nextcord.Color.red()
        )
        private_embed = nextcord.Embed(
            title=text,
            description=pr_desc,
            colour=nextcord.Color.red()
        )

        try:
            await user.kick(reason=reason)
            await interaction.send(content=f"Kicked {user}")
            await public_channel.send(embed=public_embed)
            await private_channel.send(embed=private_embed)
        except DiscordException as e:
            print(e)


def setup(bot):
    bot.add_cog(int_kick(bot))
