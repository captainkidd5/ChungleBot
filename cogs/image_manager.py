import discord, json, random, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(image_manager(bot))

# Eventually want to export token system to this file

class image_manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='grab',description='Summon Thanos to restore balance to a member in chat')
    async def thanos_command(self,ctx):
        await ctx.channel.send('Perfectly balanced...', file=discord.File('images/thanos1.png'))
        await self.bot.wait_for('message',timeout=30)
        await ctx.channel.send(file=discord.File('images/thanos2.png'))
        await ctx.channel.send(f'...as <@{ctx.author.id}> should be.')
