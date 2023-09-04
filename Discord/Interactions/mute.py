import re
from datetime import timedelta

from nextcord import Interaction, Member, SlashOption, DiscordException
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions

dbot = commands.Bot()


class int_mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @dbot.slash_command(guild_ids=[1070169312284917860])
    @has_permissions(moderate_members=True)
    async def mute(self, interaction: Interaction, user: Member = SlashOption(required=True),
                   reason: str = SlashOption(required=False), time: str = SlashOption(required=False)):
        time = self.parse_duration(time)

        try:
            await user.timeout(time, reason=reason)
            await interaction.send(content="Done", ephemeral=True)
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
    bot.add_cog(int_mute(bot))
