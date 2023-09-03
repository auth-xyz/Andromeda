import os


class LegacyLoader:
    def __init__(self, client):
        self.client = client

    def load_commands(self):
        path = "Discord/Legacy"
        for filename in os.listdir(path):
            if not filename:
                return print("[andromeda.legacy] : no module found, skipping...")
            
            if filename.endswith(".py") and filename != "__init__.py":
                module = f"Discord.Legacy.{filename[:-3]}"
                try:
                    self.client.load_extension(module)
                    print(f"[andromeda.legacy] : loaded {module}")
                except Exception as e:
                    print(f"[andromeda.legacy] : failed to load {module}: \n{e}")


class InteractionLoader:
    def __init__(self, client):
        self.client = client

    def load_interaction(self):
        path = "Discord/Interactions"
        for filename in os.listdir(path):
            if not filename:
                return print("[andromeda.interaction] : no module found, skipping...")

            if filename.endswith(".py") and filename != "__init__.py":
                module = f"Discord.Interactions.{filename[:-3]}"
                try:
                    self.client.load_extension(module)
                    print(f"[andromeda.interactions] : loaded {module}")
                except Exception as e:
                    print(f"[andromeda.interactions] : failed to load {module}\n[andromeda.error] {e}")

