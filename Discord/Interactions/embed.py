import nextcord

from nextcord import Interaction, SlashOption, Embed
from nextcord.ext import commands
from Discord.discord_rules import drules, drules2
from Discord.nsfw_rules import nsfw_rules, reward

intents = nextcord.Intents.all()
client = commands.Bot("!", intents=intents)


class intEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.slash_command(name="embed", description="Embed generator")
    @commands.has_permissions(ban_members=True)
    async def embed(self, interaction: Interaction, embed: str = SlashOption(required=True, choices=[
        "rules",
        "nsfw_rules",
        "andromeda_usage",
        "voice_rules",
    ])):
        rules_embed = self.embed_creator(
            title="",
            desc=f"{drules}",
            color=nextcord.Color.dark_purple()
        )
        rules_2 = self.embed_creator(
            title="",
            desc=f"{drules2}",
            color=nextcord.Color.dark_purple()
        )
        rules_3 = self.embed_creator(
            title="Accept Rules",
            desc="""
            NOW THAT YOU'VE READ & UNDERSTAND THESE RULES, PLEASE REACT TO THIS MESSAGE TO GET MEMBER ROLE STATUS, 
            TO VIEW ALL CHANNELS ALSO VISIT #【🔘】self-assign-roles TO GET YOUR PERSONIFIED ROLES.
            """,
            color=nextcord.Color.dark_purple()
        )
        nsfw_embed = self.embed_creator(
            title="",
            desc=f"{nsfw_rules}",
            color=nextcord.Color.red()
        )
        nsfw_reward = self.embed_creator(
            title="",
            desc=f"{reward}",
            color=nextcord.Color.red()
        )

        if embed == "rules":
            await interaction.send(embed=rules_embed)
            await interaction.send(embed=rules_2)
            await interaction.send(embed=rules_3)
        elif embed == "nsfw_rules":
            await interaction.send(embed=nsfw_embed)
            await interaction.send(embed=nsfw_reward)

    @staticmethod
    def embed_creator(title, desc, color):
        text = title
        desc = desc

        embed = Embed(
            title=text,
            description=desc,
            colour=color
        )

        return embed


def setup(bot):
    bot.add_cog(intEmbed(bot))
