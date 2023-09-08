import nextcord
from nextcord import Interaction, Member, SlashOption
from nextcord.ext import commands


client = commands.Bot()


class int_off(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.off_users = {}

    @client.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(ban_members=True)
    async def off(self, interaction: Interaction, target: Member = SlashOption(required=True)):
        if target.id == interaction.user.id:
            return interaction.send(ephemeral=True, content="Are you stupid?")

        self.off_users[target.id] = True
        await interaction.send(content="Done", ephemeral=True)

    @client.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(ban_members=True)
    async def on(self, interaction: Interaction, target: Member = SlashOption(required=True)):
        if target.id in self.off_users:
            del self.off_users[target.id]
            await interaction.send(content="Done.", ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.id in self.off_users:
            await message.delete()


def setup(bot):
    bot.add_cog(int_off(bot))
