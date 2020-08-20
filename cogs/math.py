  
from discord.ext import commands
import discord
import json
import random
import asyncio

def setup(bot):
        bot.add_cog(math(bot))

#Eventually want to export token system to this file

class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx,*choices : str):
        """Chooses between multiple choices."""
        await ctx.channel.send(random.choice(choices))
        

