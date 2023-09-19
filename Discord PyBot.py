# Not another Discord Bot, Hackman's walkthrough

# The bot listens for messages in the channel and responds with "Hello" 
# if the message starts with !hello. 
# You can customize the responses and commands as needed.


# 1 You'll need to install the discord.py library to work with Discord's API.
#   pip install discord.py

# 2 (https://discord.com/developers/applications) Create and get bot token

# 3

import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Create a bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Don't respond to our own messages

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, {0.author.mention}!'.format(message))

bot.run(BOT_TOKEN)


# 4 run the python script
#   python your_script.py

# 5 Invite Bot to server
