import os
import nextcord

from dotenv import load_dotenv
from nextcord.ext import commands

from Utils.welcome import generate_custom_message
from Utils.database import Database
from Discord.loader import LegacyLoader, InteractionLoader

load_dotenv()

intents = nextcord.Intents.all()
client = commands.Bot("!", intents=intents)
cl = LegacyLoader(client)
il = InteractionLoader(client)

db = Database(os.getenv("DB_L"), "Dataset", "Chatlogs")
db.connect()


@client.event
async def on_ready():
    cl.load_commands()
    print("\n")
    il.load_interaction()

    try:
        await client.sync_all_application_commands()
    except Exception as e:
        print(f"[discord.error] : {e}")

    print("\n[discord.main] : successfully established connection with discord.\n")


@client.event
async def on_message(message):
    word = message.content.lower()
    document = db.find_document({"query": word})
    if message.author.bot:
        return

    if document:
        response = document["value"]
        await message.reply(response)


@client.event
async def on_member_update(before, after: nextcord.Member):
    added_roles = set(after.roles) - set(before.roles)
    if added_roles:
        for role in added_roles:
            if role.id == 1070171459202322442:
                channel = client.get_channel(1070173038194216990)
                msg = generate_custom_message(f"Welcome to Nebula, {after.display_name}\nHave an awesome time here!",
                                              table_width=40, center_text=False)
                embed = nextcord.Embed(
                    title=f"Member {after} joined!",
                    description=f"```\n{msg}\n```"
                )
                embed.set_thumbnail(after.display_avatar)
                await channel.send(embed=embed, content=f"{after.mention}")


@client.event
async def on_member_join(member: nextcord.Member):
    ids = [1070217307143536700, 1070216214871294022]
    sid = 521850636321423371

    serv = client.get_guild(sid)
    if serv:
        for rid in ids:
            role = serv.get_role(rid)
            if not role:
                return
            await member.add_roles(role)


@client.event
async def on_message_delete(message: nextcord.Message):
    channel = client.get_channel(1070176260891889725)
    title = f"Deleted Message in {message.channel.name}"
    desc = f"User {message.author.display_name} deleted a message\n```\n{message.content}\n```"
    author = message.author
    if message.author.bot:
        return

    embed = nextcord.Embed(
        title=title,
        description=desc,
        colour=nextcord.Color.red()
    )
    embed.set_thumbnail(author.display_avatar)
    await channel.send(embed=embed)


@client.event
async def on_message_edit(before: nextcord.Message, after: nextcord.Message):
    channel: nextcord.TextChannel = client.get_channel(1070176260891889725)
    title = f"Edited Message in {before.channel.name}"
    author = before.author or after.author

    if before.content != after.content and not author.bot:
        desc = f"User {author.display_name} edited a message.\n```\nFrom: {before.content}\n\nTo: {after.content}\n```"

        embed = nextcord.Embed(
            title=title,
            description=desc,
            color=nextcord.Color.yellow(),
        )
        embed.set_thumbnail(author.display_avatar)
        await channel.send(embed=embed)


@client.event
async def on_channel_update(before: nextcord.TextChannel, after: nextcord.TextChannel):
    channel = client.get_channel(1070176260891889725)
    text = f"Channel {before.name} was changed"
    chan = set(before) - set(after)
    desc = f"```\nChanges:\n{chan}\n```"

    embed = nextcord.Embed(
        title=text,
        description=desc,
        colour=nextcord.Color.blue()
    )
    await channel.send(embed=embed)


client.run(os.getenv("TOKEN"))
