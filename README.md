## Requirements:
> `python 3.10+`
> `a working brain`

```bash
# Initialize the repository
git clone https://github.com/auth-xyz/hexis-tfai
cd hexis-tfai

# Install requirements
python3 -m pip install -r requirements.txt # Or:
pip install -r requirements.txt

# Create a .env on the root directory with the following:
> DB_U # Database user
> DB_P # Database password
> DB_L # Database uri (using mongo on this repo)
> TOKEN # discord bot token

# For the current iteration of hexis, you'll need a rapid api account that is subscribed
# to the "Waifu" api.

# so add the following to the .env
> API_URL # should be: "https://waifu.p.rapidapi.com/path"
> KEY # API key
> GUILD_ID # The guild you're using the bot on. (i forgor why i need this...)
```