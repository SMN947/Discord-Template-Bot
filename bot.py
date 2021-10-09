import json
import discord
from itertools import cycle
from discord.ext import commands, tasks
import os

with open("config.json",'r') as f:
    CONFIG = json.load(f)

TOKEN = CONFIG["token"]
PREFIX = CONFIG["bot_prefix"]
INTENTS = discord.Intents.default()
BOT = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
STATUS = cycle(['Try * help','Prefix - *'])

BOT.remove_command("help")

@BOT.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@tasks.loop(seconds=5)
async def change_status():
    await BOT.change_presence(activity=discord.Game(next(STATUS)))

for filename in os.listdir('./modulos'):
    if filename.endswith('.py'):
        BOT.load_extension(f'modulos.{filename[:-3]}')

BOT.run(TOKEN)