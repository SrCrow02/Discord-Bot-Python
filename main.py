import discord
from discord.ext import commands

prefix = "u-"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = prefix, intents = intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

bot.run('')