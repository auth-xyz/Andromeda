import os
import dotenv
import nextcord

from Utils.welcome import generate_custom_message
from Utils.database import Database

dotenv.load_dotenv()
db = Database(os.getenv("DB_L"), "Dataset", "Chatlogs")
db.connect()


class LegacyLoader:
    def __init__(self, client):
        self.client = client

    def load_commands(self):
        path = "Discord/Legacy"
        for filename in os.listdir(path):
            if not filename:
                return print("[andromeda.loader] : no module found, skipping...")

            if filename.endswith(".py") and filename != "__init__.py":
                module = f"Discord.Legacy.{filename[:-3]}"
                try:
                    self.client.load_extension(module)
                    print(f"[andromeda.loader] : loaded {module}")
                except Exception as e:
                    print(f"[andromeda.loader] : failed to load {module}: \n{e}")


class InteractionLoader:
    def __init__(self, client):
        self.client = client

    def load_interaction(self):
        path = "Discord/Interactions"
        for filename in os.listdir(path):
            if not filename:
                return print("[andromeda.loader] : no module found, skipping...")

            if filename.endswith(".py") and filename != "__init__.py":
                module = f"Discord.Interactions.{filename[:-3]}"
                try:
                    self.client.load_extension(module)
                    print(f"[andromeda.loader] : loaded {module}")
                except Exception as e:
                    print(f"[andromeda.loader] : failed to load {module}\n[andromeda.error] {e}")


class EventLoader:
    def __init__(self, client):
        self.client = client

    async def on_channel_update(self, before, after):
        channel = self.client.get_channel(1070176260891889725)
        text = f"Channel {before.name} was changed"
        chan = set(before) - set(after)
        desc = f"```\nChanges:\n{chan}\n```"

        embed = nextcord.Embed(
            title=text,
            description=desc,
            colour=nextcord.Color.blue()
        )
        await channel.send(embed=embed)

    async def on_raw_reaction_add(self, payload):
        guild_id = 1070169312284917860

        guild = self.client.get_guild(guild_id)
        message = await self.client.get_channel(payload.channel_id).fetch_message(payload.message_id)

        emoji = '✅'
        member = guild.get_member(payload.user_id)

        if str(payload.emoji) == emoji:
            member_role = guild.get_role(1070171459202322442)
            if member_role not in member.roles:
                await member.add_roles(member_role)
                print(f'Added role {member_role.name} to {member.display_name}')

    async def on_message_edit(self, before: nextcord.Message, after: nextcord.Message):
        channel = self.client.get_channel(1070176260891889725)
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

    async def on_message_delete(self, message: nextcord.Message):
        if message.author.bot:
            return

        channel = self.client.get_channel(1070176260891889725)
        title = f"Deleted Message in {message.channel.name}"
        desc = f"User {message.author.display_name} deleted a message\n```\n{message.content}\n```"

        embed = nextcord.Embed(
            title=title,
            description=desc,
            colour=nextcord.Color.red()
        )
        embed.set_thumbnail(message.author.display_avatar)
        await channel.send(embed=embed)

    async def on_member_join(self, member: nextcord.Member):
        ids = [1070217307143536700, 1070216214871294022]
        sid = 521850636321423371
        serv = self.client.get_guild(sid)

        if serv:
            for rid in ids:
                role = serv.get_role(rid)
                if role:
                    await member.add_roles(role)

    async def on_member_update(self, before, after: nextcord.Member):
        added_roles = set(after.roles) - set(before.roles)

        if added_roles:
            for role in added_roles:
                if role.id == 1070171459202322442:
                    channel = self.client.get_channel(1070173038194216990)
                    msg = generate_custom_message(
                        f"Welcome to Nebula, {after.display_name}\nHave an awesome time here!",
                        table_width=40, center_text=False)
                    embed = nextcord.Embed(
                        title=f"Member {after} joined!",
                        description=f"```\n{msg}\n```"
                    )
                    embed.set_thumbnail(after.display_avatar)
                    await channel.send(embed=embed, content=f"{after.mention}")

    async def on_ready(self):
        cl = LegacyLoader(self.client)
        il = InteractionLoader(self.client)

        cl.load_commands()
        print("\n")
        il.load_interaction()

        try:
            await self.client.sync_all_application_commands()
        except Exception as e:
            print(f"[discord.error] : {e}")

        print("\n[discord.main] : successfully established connection with discord.\n")

    @staticmethod
    async def on_message(message: nextcord.Message):
        if message.author.bot:
            return

        word = message.content.lower()
        document = db.find_document({"query": word})

        if document:
            response = document["value"]
            await message.reply(response)
