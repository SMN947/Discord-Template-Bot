import json
import discord
from itertools import cycle
from discord.ext import commands, tasks

with open("config.json",'r') as f:
    CONFIG = json.load(f)

TOKEN = CONFIG["token"]
PREFIX = CONFIG["bot_prefix"]
INTENTS = discord.Intents.default()
BOT = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
STATUS = cycle(['Try * help','Prefix - *'])

@BOT.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@tasks.loop(seconds=5)
async def change_status():
    await BOT.change_presence(activity=discord.Game(next(STATUS)))

BOT.run(TOKEN)