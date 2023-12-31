import re
import nextcord

from nextcord import Interaction, Member, SlashOption, DiscordException
from nextcord.ext import commands
from datetime import timedelta

from Utils.database import Database
from os import getenv

client = commands.Bot()
db = Database(getenv("DB_L"), "Offenses", "Logs")
db.connect()


class intMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.slash_command(guild_ids=[1070169312284917860])
    @commands.has_permissions(moderate_members=True)
    async def mute(self, interaction: Interaction, user: Member = SlashOption(required=True),
                   reason: str = SlashOption(required=False), time: str = SlashOption(required=False)):
        time = self.parse_duration(time)
        text = f"User {user.display_name} was muted"
        desc = f"```\nModerator: {interaction.user.name}\nReason:{reason}\nTime:{time}\n```"
        chan = interaction.guild.get_channel(1070569664599556146)
        embed = nextcord.Embed(title=text, description=desc, colour=nextcord.Colour.yellow())
        embed.set_thumbnail(user.display_avatar)

        reason = "No reason given."

        payload = {
            "action": "mute",
            "user_id": user.id,
            "username": user.name,
            "reason": reason,
            "time": str(time),
            "moderator": interaction.user.display_name,
        }

        try:
            await user.timeout(time, reason=reason)
            db.insert_document(payload)

            await interaction.send(content="Done", ephemeral=True)
            await chan.send(embed=embed)
        except DiscordException as e:
            print(e)

    @staticmethod
    def parse_duration(input_string):
        # Define a dictionary to map abbreviations to corresponding time units
        time_units = {
            's': 'seconds',
            'm': 'minutes',
            'h': 'hours',
            'd': 'days'
        }

        # Use regular expressions to extract the numeric value and unit abbreviation
        match = re.match(r'(\d+)([smhd])', input_string)

        if match:
            value, unit = match.groups()
            value = int(value)

            if unit in time_units:
                # Create a timedelta object based on the parsed values
                duration = timedelta(**{time_units[unit]: value})
                return duration

        return "Invalid input"


def setup(bot):
    bot.add_cog(intMute(bot))
