import os
import discord
import json

from discord.ext import commands, tasks

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
PREFIX = os.environ.get('PREFIX', '!chungle ')

activity_index = 0

with open(join(dirname(__file__), 'config', 'activities.json')) as json_file:
    activities = json.load(json_file)

client = commands.Bot(command_prefix=PREFIX)

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

@tasks.loop(seconds=0.5)
async def update_activity():
    global activity_index

    activity = activities[activity_index]
    print(activity['type'] + " " + activity['message'])

    activity_index += 1

    if activity_index >= len(activities):
        activity_index = 0

update_activity.start()
client.run(TOKEN)
