import nextcord
from nextcord import Interaction, Member, SlashOption, DiscordException
from nextcord.ext import commands

intents = nextcord.Intents.all()
client = commands.Bot("!", intents=intents)

class int_ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, user: Member = SlashOption(required=True),
                  reason: str = SlashOption(required=False)):

        text = f"{user.name} has been banned."
        pu_desc = f"```\nModerator: {interaction.user.display_name}\n```"
        pr_desc = f"```\nModerator: {interaction.user.display_name}\nReason: {reason}\n```"
        chan_public = interaction.guild.get_channel(1070188919192305744)
        chan_private = interaction.guild.get_channel(1070569664599556146)

        print(f"{chan_public}, {chan_private}")

        public_embed = nextcord.Embed(
            title=text,
            description=pu_desc,
            colour=nextcord.Color.red()
        )
        public_embed.set_thumbnail(user.display_avatar)
        private_embed = nextcord.Embed(
            title=text,
            description=pr_desc,
            colour=nextcord.Color.red()
        )
        private_embed.set_thumbnail(user.display_avatar)

        try:
            await user.ban(reason=reason)

            await chan_public.send(embed=public_embed)
            await chan_private.send(embed=private_embed)
            await interaction.send(content=f"Done.", ephemeral=True)
        except DiscordException as e:
            print(e)


def setup(bot):
    bot.add_cog(int_ban(bot))
