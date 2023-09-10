## Requirements:
> [Python 3.10+](https://python.org/downloads)

### Setting up
```bash
git clone https://github.com/auth-xyz/Andromeda
cd Andromeda

# Installing dependencies <pip>
pip install -r requirements.txt

# Installing dependencies <poetry>
poetry install

# Create a .env file that follows this example:
DB_U=database user
DB_P=database password (mongodb)
DB_L=database link (uri)

TOKEN=discord token
GUILD_ID=the guild where interactions will be used

# After everything is done, you should be able to just:

# Running via python:
python3 main.py

# Running via poetry:
poetry run python main.py
```
