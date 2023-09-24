from os import getenv

import nextcord
from nextcord import Interaction, Member, SlashOption, Embed
from nextcord.ext import commands

from Utils.database import Database


client = commands.Bot()
database = Database(getenv("DB_L"), "Offenses", "Logs")
database.connect()


class intLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.slash_command(description="Shows all offenses committed by this user")
    async def logs(self, interaction: Interaction, target: Member = SlashOption(required=True)):
        reasons = []
        moderators = []

        query = {"user_id": target.id}
        res = database.find_in_all(query)
        if not res:
            return interaction.send(content="User has committed no crimes")

        crimes = database.find_all(query)
        text = f"{target.display_name}'s crimes"
        desc = f"```\nCrimes committed: {len(res)}\n```"

        embed = Embed(
            title=text,
            description=desc,
            colour=nextcord.Colour.light_gray()
        )

        for entry in crimes['Logs']:
            reason = entry['reason']
            moderator = entry['moderator']
            reasons.append(reason)
            moderators.append(moderator)

        for i in range(len(reasons)):
            embed.add_field(name=f"Log {i + 1}", value=f"Reason: {reasons[i]}\nModerator: {moderators[i]}",
                            inline=False)

        embed.set_thumbnail(target.display_avatar)
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(intLogs(bot))
