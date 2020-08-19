
# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Dev Ex!'
    )

client.run(TOKEN)