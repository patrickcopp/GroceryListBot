import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as "+str(client.user))

@client.event
async def on_message(message):
    if message.content == '!quit':
        await client.close()
    elif message.content.startswith("!"):
        await message.channel.send('Good joke')

client.run(os.environ.get("TOKEN"))