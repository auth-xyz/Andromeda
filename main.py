import os
import nextcord

from dotenv import load_dotenv
from nextcord.ext import commands
from Discord.loader import CommandLoader, ModuleLoader

load_dotenv()

intents = nextcord.Intents.all()
client = commands.Bot("!", intents=intents)
cl = CommandLoader(client)
ml = ModuleLoader(client)

@client.event
async def on_ready():
    cl.load_commands() # Loading commands from Discord.Commands
    ml.load_modules()
    
    print("\n[discord.main] : successfully established connection with discord.")

client.run(os.getenv("TOKEN"))