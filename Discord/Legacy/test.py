import nextcord
from nextcord.ext import commands


class Command_Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="test")
    async def test(self, ctx):
        if not ctx.author.id == 1007441934652030986:
            return
        embed = nextcord.Embed(
            title="",
            description=f"┏━•❃°•°❀°•°❃°•°❀°•°❃•━┓\n\nWelcome {ctx.author.mention} to Nebula!\nEnjoy your stay and get some cool roles at [placeholder for test]\n\n┗━•❃°•°❀°•°❃°•°❀°•°❃•━┛"
        )
        embed.set_footer(text="go fuck yourself © - Andromeda : 2023")
        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(Command_Test(client))
