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
    client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="the [Maintence Modes]"))
    cl.load_commands() # Loading commands from Discord.Commands
    
    print("\n[discord.main] : successfully established connection with discord.")

client.run(os.getenv("TOKEN"))