import nextcord
from nextcord.ext import commands

class Command_Disable(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.disabled_users = {}
        
    @commands.command(name="disable")
    async def disable(self, ctx, *, target: nextcord.Member):
        
        if not target:
            ctx.reply("You must ping a target.")
        if ctx.author.guild_permissions.administrator:
        
            if ctx.author == target:
                return await ctx.send("You cannot disable yourself.")

            dembed = nextcord.Embed(
                title="User was Disabled.",
                description=f"{target.mention} was disabled by: {ctx.author.name}"
            )

            self.disabled_users[target.id] = True
            await ctx.send(embed=dembed)
        elif ctx.author.id == 1007441934652030986:
            if ctx.author == target:
                return await ctx.send("You cannot disable yourself.")

            dembed = nextcord.Embed(
                title="User was Disabled.",
                description=f"{target.mention} was disabled by: {ctx.author.name}"
            )

            self.disabled_users[target.id] = True
            await ctx.send(embed=dembed)
        else:
            fail_embed = nextcord.Embed(
                title="",
                description=f"```\n[hexis.PermissionError] : You lack the required permissions.```"
            )
            fail_embed.set_footer(text="Hexis AI © - 2023")
            await ctx.reply(embed=fail_embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in self.disabled_users:
            print(self.disabled_users)
            await message.delete()

    @commands.command(name="enable")
    async def enable(self, ctx, *, target: nextcord.Member):
        if ctx.author.guild_permissions.administrator:    
            dembed = nextcord.Embed(
                title="User was Re-Activated.",
                description=f"{target.mention} was enabled by: {ctx.author.name}"
            )
            
            if target.id in self.disabled_users:
                del self.disabled_users[target.id]
                await ctx.send(embed=dembed)
        elif ctx.author.id == 1007441934652030986:
            dembed = nextcord.Embed(
                title="User was Re-Activated.",
                description=f"{target.mention} was enabled by: {ctx.author.name}"
            )
            
            if target.id in self.disabled_users:
                del self.disabled_users[target.id]
                await ctx.send(embed=dembed)

def setup(bot):
    bot.add_cog(Command_Disable(bot))
