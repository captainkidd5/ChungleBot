
# bot.py
import os

import discord
from discord.ext import commands

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")

client = commands.Bot(command_prefix='!chungle ')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Dev Ex!'
    )

@client.command()
async def test(ctx):
    await ctx.send('Hello, world!')

client.run(TOKEN)
