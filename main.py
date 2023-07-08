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
async def on_member_join(member):
    channel_id = 1070173038194216990
    channel = client.get_channel(channel_id)
    embed = nextcord.Embed(
        title="",
        description=f"┏━•❃°•°❀°•°❃°•°❀°•°❃•━┓\n\nWelcome {member.mention} to Nebula!\nEnjoy your stay and get some cool roles in {client.get_channel(1070172711835410452)}\n\n┗━•❃°•°❀°•°❃°•°❀°•°❃•━┛"
    )

    if not channel: return
    
    #await channel.send(embed=embed)

@client.event
async def on_ready():
    cl.load_commands() # Loading commands from Discord.Commands
    
    print("\n[discord.main] : successfully established connection with discord.")

client.run(os.getenv("TOKEN"))