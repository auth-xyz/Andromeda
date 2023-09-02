import os
import nextcord

from dotenv import load_dotenv
from nextcord.ext import commands
from Discord.loader import CommandLoader

load_dotenv()

intents = nextcord.Intents.all()
client = commands.Bot("!", intents=intents)
cl = CommandLoader(client)


@client.event
async def on_ready():
    cl.load_commands()

    print("\n[discord.main] : successfully established connection with discord.")


@client.event
async def on_member_update(before, after):
    added_roles = set(after.roles) - set(before.roles)
    if added_roles:
        for role in added_roles:
            if role.id == 1070171459202322442:
                channel = client.get_channel(1070173038194216990)
                embed = nextcord.Embed(
                    title="",
                    description=f"\n┌── ⋅ ⋅ ── ✩ ── ⋅ ⋅── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ──┐\n\nWelcome to Nebula, {before.mention}\nhave an awesome time here!\n\n└── ⋅ ⋅ ── ✩ ── ⋅ ⋅── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ──┘"
                )
                await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    roles_to_add = [1070216214871294022, 1070217307143536700]
    for role in roles_to_add:
        _role = nextcord.utils.get(member.guild.roles, id=role)
        if _role:
            await member.add_roles(_role)


@client.event
async def on_message_delete(message):
    channel = client.get_channel(1070176260891889725)
    embed = nextcord.Embed(
        title=f"{message.author.mention} deleted a message.",
        description=f"{message.content}"
    )
    embed.set_footer(text=f"Message deleted in {message.channel}")
    await channel.send(embed=embed)


@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(1070176260891889725)
    embed = nextcord.Embed(
        title=f"{before.author.mention} edited a message.",
        description=f"Before: {before.content}\nAfter: {after.content}"
    )
    await channel.send(embed=embed)


@client.event
async def on_channel_update(before, after):
    channel = client.get_channel(1070176260891889725)
    embed = nextcord.Embed(
        title="Channel updated.",
        description=f"{before.name} was changed"
    )
    embed.add_field(name="Author", value=f"Changed {after.name}")
    await channel.send(embed=embed)


client.run(os.getenv("TOKEN"))
