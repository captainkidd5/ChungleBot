import os, discord, json, re

from discord.ext import commands, tasks
from cogs.activity_manager import activity_manager

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
PREFIX = os.environ.get('PREFIX', '!chungle ')

client = commands.Bot(command_prefix=PREFIX)

activities_path = join(dirname(__file__), 'config', 'activities.json')
client.add_cog(activity_manager(client, activities_path))

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

@client.command()
async def speak(ctx, *args):
    await ctx.message.delete()
    await ctx.send(' '.join(args))

client.get_cog('activity_manager').update.start()
client.run(TOKEN)
