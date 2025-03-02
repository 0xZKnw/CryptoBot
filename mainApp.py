import discord
from discord.ext import commands
from discord import app_commands
import requests
import cryptocompare

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game("/help | btc, sol, eth, ..."))
    await bot.tree.sync()

@bot.tree.command(name="quoi", description="Replies with 'feur' every time")
async def quoi(interaction: discord.Interaction):
    await interaction.response.send_message("feur")

@bot.tree.command(name="zknw", description="Returns the link to Nyfime's website")
async def nyfime(interaction: discord.Interaction):
    await interaction.response.send_message("https://0xZKnw.netlify.app")

@bot.tree.command(name="price", description="Get the current price of a token in USD")
async def price(interaction: discord.Interaction, token_name: str):
    token = cryptocompare.get_price(token_name, currency='USD')
    if token:
        up = token_name.upper()
        await interaction.response.send_message(f"1 {token_name} = {token[up]['USD']}$")
    else:
        await interaction.response.send_message("Token not found.")

@bot.tree.command(name="exchanges", description="Returns a list of major cryptocurrency exchanges")
async def exchanges(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.binance.com\nhttps://www.coinbase.com\nhttps://www.moonpay.com\nhttps://www.kraken.com\nhttps://www.kucoin.com/")

@bot.tree.command(name="wallets", description="Returns a list of popular cryptocurrency wallets")
async def wallets(interaction: discord.Interaction):
    await interaction.response.send_message("https://phantom.app/\nhttps://www.coinbase.com/wallet\nhttps://metamask.io/\nhttps://rabby.io/")

@bot.tree.command(name="ethwallet", description="Returns the balance of an Ethereum wallet")
async def eth_wallet(interaction: discord.Interaction, address: str):
    url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}/balance"
    response = requests.get(url)
    if response.status_code == 200:
        balance = response.json()["balance"]
        token = cryptocompare.get_price("ETH", currency='USD')
        nb = round(balance / 10**18, 5)
        await interaction.response.send_message(f"Address: {address}\nBalance: {nb} ETH ({round(nb * token['ETH']['USD'], 2)}$)")
    else:
        await interaction.response.send_message("Unable to retrieve the wallet.")

@bot.tree.command(name="btcwallet", description="Returns the balance of a Bitcoin wallet")
async def btc_wallet(interaction: discord.Interaction, address: str):
    url = f"https://blockstream.info/api/address/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        balance = data.get("chain_stats", {}).get("funded_txo_sum", 0) - data.get("chain_stats", {}).get("spent_txo_sum", 0)
        token = cryptocompare.get_price("BTC", currency='USD')
        nb = round(balance / 100000000, 5)
        await interaction.response.send_message(f"Address: {address}\nBalance: {nb} BTC ({round(nb * token['BTC']['USD'], 2)}$)")
    else:
        await interaction.response.send_message("Unable to retrieve the wallet.")

@bot.tree.command(name="solwallet", description="Returns the balance of a Solana wallet")
async def sol_wallet(interaction: discord.Interaction, address: str):
    try:
        api_url = f"https://api.mainnet-beta.solana.com"
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [address]
        }
        response = requests.post(api_url, json=payload, headers=headers)
        response_data = response.json()
        lamports = response_data.get("result", {}).get("value", 0)
        sol_balance = lamports / 1_000_000_000
        await interaction.response.send_message(f"Address: {address}\nBalance: {sol_balance:.5f} SOL")
    except Exception as e:
        await interaction.response.send_message("Error: Unable to retrieve the wallet.")

@bot.tree.command(name="calc", description="Calculate the value of a certain amount of a token")
async def calc(interaction: discord.Interaction, nb: int, token_name: str):
    token = cryptocompare.get_price(token_name, currency='USD')
    if token:
        up = token_name.upper()
        await interaction.response.send_message(f"{nb} {up} = {round(nb * token[up]['USD'], 2)}$")
    else:
        await interaction.response.send_message("Token not found.")

@bot.tree.command(name="help", description="Displays a list of all bot commands")
async def hlp(interaction: discord.Interaction):
    await interaction.response.send_message(
        "All available commands:\n"
        " - /price token: returns the price of the token\n"
        " - /exchanges: returns a list of major exchanges\n"
        " - /wallets: returns a list of popular wallets\n"
        " - /quoi: returns 'feur'\n"
        " - /btcwallet address: returns the balance of a Bitcoin wallet\n"
        " - /ethwallet address: returns the balance of an Ethereum wallet\n"
        " - /solwallet address: returns the balance of a Solana wallet\n"
        " - /zknw: returns the link to my website\n"
        " - /help: displays all bot commands"
    )

bot.run('TOKEN')