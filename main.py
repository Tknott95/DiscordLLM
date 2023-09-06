import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
# END KEY SETTING 

from colors import clr

from llm import Chain

print('\n' + clr.cyan + '  TOC_BOT RUNNNING... \n' + clr.clear)

import discord
import re

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

_chain= Chain()


@client.event
async def on_ready():
    print(clr.bold + '  We have logged in as {0.user}'.format(client) + clr.clear)

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!ask'):
        match = re.search(r"!ask (.*)", message.content)
        x = _chain.chat(match, _chain.PROMPTS[1])
        await message.channel.send(x)
    
    if message.content.startswith('!poem'):
        match = re.search(r"!poem (.*)", message.content)
        x = _chain.chat(match, _chain.PROMPTS[3])
        await message.channel.send(x)
    
    if message.content.startswith('!psyop'):
        match = re.search(r"!psyop (.*)", message.content)
        x = _chain.chat(match, _chain.PROMPTS[4])
        await message.channel.send(x)

    if message.content.startswith('!argue'):
        match = re.search(r"!argue (.*)", message.content)
        x = _chain.chat(match, _chain.PROMPTS[5])
        await message.channel.send(x)

    if message.content.startswith('!sup bbz'):
        await message.channel.send('yo, weak little human!')

client.run(DISCORD_TOKEN)
