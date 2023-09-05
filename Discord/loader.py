import os


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

