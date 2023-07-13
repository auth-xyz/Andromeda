import nextcord
from nextcord.ext import commands

class Command_Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deleted_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.deleted_messages[message.channel.id] = message

    @commands.command(name="snipe")
    async def snipe(self, ctx):
        channel_id = ctx.channel.id
        if channel_id in self.deleted_messages:
            message = self.deleted_messages[channel_id]
            embed = nextcord.Embed(
                title="Sniped Message",
                description=message.content,
                color=nextcord.Color.green()
            )
            embed.set_author(
                name=message.author.name,
                icon_url=message.author.avatar_url
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("No deleted messages to snipe.")

def setup(bot):
    bot.add_cog(Command_Snipe(bot))

