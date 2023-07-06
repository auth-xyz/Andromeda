import os

class CommandLoader:
    def __init__(self, client):
        self.client = client

    def load_commands(self):
        path = "Discord/Commands"
        for filename in os.listdir(path):
            if not filename:
                return print("[discord.loader] : no module found, skipping...")
            
            if filename.endswith(".py") and filename != "__init__.py":
                module = f"Discord.Commands.{filename[:-3]}"
                try:
                    self.client.load_extension(module)
                    print(f"[discord.loader] : loaded {module}")
                except Exception as e:
                    print(f"[discord.loader] : failed to load {module}: \n{e}")


class EventLoader:
    def __init__(self, client):
        self.client = client

    def load_modules(self):
        path = "Discord/Modules"
        for filename in os.listdir(path):
            if not filename:
                return print("[discord.loader.modules] : no module found, skipping...")
            
            if filename.endswith(".py") and filename != "__init__.py":
                module = f"Discord.Modules.{filename[:-3]}"
                try:
                    self.client.load_extension(module)
                    print(f"[discord.loader.modules] : loaded {module}")
                except Exception as e:
                    print(f"[discord.loader.modules] : failed to load {module}: \n{e}")

