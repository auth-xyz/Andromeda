import nextcord

from nextcord import Interaction, Member, SlashOption, DiscordException
from Utils.database import Database
from nextcord.ext import commands
from os import getenv

client = commands.Bot()

db = Database(getenv("DB_L"), "Offenses", "Logs")
db.connect()


class int_kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, user: Member = SlashOption(required=True),
                   reason: str = SlashOption(required=False)):
        text = f"{user.name} has been kicked."
        pu_desc = f"```\nModerator: {interaction.user.display_name}\n```"
        pr_desc = f"```\nModerator: {interaction.user.display_name}\nReason: {reason}\n```"

        pu = interaction.guild.get_channel(1070188919192305744)
        pr = interaction.guild.get_channel(1070569664599556146)

        payload = {
            "action": "kick",
            "user_id": user.id,
            "username": user.name,
            "reason": reason,
            "moderator": interaction.user.display_name,
        }

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
            db.insert_document(payload)

            await interaction.send(content=f"Done.", ephemeral=True)
            await pr.send(embed=private_embed)
            await pu.send(embed=public_embed)

        except DiscordException as e:
            print(e)


def setup(bot):
    bot.add_cog(int_kick(bot))
