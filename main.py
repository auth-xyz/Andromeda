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

@client.event
async def on_message_delete(message):
    channel = client.get_channel(1070176260891889725)
    embed = nextcord.Embed(
            title=f"{message.author.mention} deleted a message.",
            description=f"{message.content}"
            )
    embed.set_footer(text=f"Message deleted in {message.channel}")
    await channel.send(embed=embed)

client.run(os.getenv("TOKEN"))
