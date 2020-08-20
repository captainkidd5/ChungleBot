from discord.ext import commands, tasks
import discord, json, re

class activity_manager(commands.Cog):
    def __init__(self, bot, file):
        self.bot = bot
        self.activity_data = None
        self.activity_index = 0
        self.load(file)

    # Loads activities from the JSON configuration file
    def load(self, file):
        with open(file) as json_file:
            self.activity_data = json.load(json_file)
            self.activity_index = 0

    # Replaces a message's placeholder and returns the new string
    def get_message(self, message):
        message_values = {
            "${guild_count}": str(len(self.bot.guilds)),
            "${user_count}": str(len(self.bot.users)),
            "${prefix}": self.bot.command_prefix
        }

        # Replace some template placeholders to create a dynamic string
        replace = dict((re.escape(k), v) for k, v in message_values.items())
        pattern = re.compile("|".join(replace.keys()))

        return pattern.sub(lambda m: replace[re.escape(m.group(0))], message)

    @tasks.loop(seconds=5.0)
    async def update(self):
        await self.bot.wait_until_ready()

        if self.activity_data is None:
            return

        # Fetch the current data entry based on the index
        activity_data = self.activity_data[self.activity_index]

        # Get the activity type and message from the activities configuration
        activity_type = discord.ActivityType[activity_data['type']]
        activity_message = self.get_message(activity_data['message'])

        await self.bot.change_presence(activity=discord.Activity(type=activity_type,
            name=activity_message))

        self.activity_index += 1

        # If the index exceeds the amount of activities, go back to the start
        if self.activity_index >= len(self.activity_data):
            self.activity_index = 0
