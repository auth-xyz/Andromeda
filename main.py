import os
import nextcord

from dotenv import load_dotenv
from nextcord.ext import commands

from Utils.database import Database
from Discord.loader import LegacyLoader, InteractionLoader, EventLoader

load_dotenv()

intents = nextcord.Intents.all()
client = commands.Bot("!", intents=intents)
cl = LegacyLoader(client)
il = InteractionLoader(client)
el = EventLoader(client)

db = Database(os.getenv("DB_L"), "Dataset", "Chatlogs")
db.connect()


@client.event
async def on_ready():
    await el.on_ready()


@client.event
async def on_raw_reaction_add(payload):
    await el.on_raw_reaction_add(payload)


@client.event
async def on_message(message):
    await el.on_message(message)


@client.event
async def on_member_update(before, after: nextcord.Member):
    await el.on_member_update(before, after)


@client.event
async def on_member_join(member: nextcord.Member):
    await el.on_member_join(member)


@client.event
async def on_message_delete(message: nextcord.Message):
    await el.on_message_delete(message)


@client.event
async def on_message_edit(before: nextcord.Message, after: nextcord.Message):
    await el.on_message_edit(before, after)


@client.event
async def on_channel_update(before, after):
    await el.on_channel_update(before, after)


client.run(os.getenv("TOKEN"))
