import os
import discord
import json
import re

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

@tasks.loop(seconds=5.0)
async def update_activity():
    global activity_index
    await client.wait_until_ready()

    activity_data = activities[activity_index]

    activity_type = discord.ActivityType[activity_data['type']]
    activity_message = activity_data['message']

    message_values = {
        "${guild_count}": str(len(client.guilds)),
        "${user_count}": str(len(client.users))
    }

    # Replace some template placeholders to create a dynamic string
    replace = dict((re.escape(k), v) for k, v in message_values.items())
    pattern = re.compile("|".join(replace.keys()))

    activity_message = pattern.sub(lambda m: replace[re.escape(m.group(0))], activity_message)
    await client.change_presence(activity=discord.Activity(type=activity_type, name=activity_message))

    activity_index += 1

    if activity_index >= len(activities):
        activity_index = 0

update_activity.start()
client.run(TOKEN)
