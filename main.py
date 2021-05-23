import discord
import os
from dotenv import load_dotenv
from functionality import add, list, clear, remove

load_dotenv()
grocery_lists = {}
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as "+str(client.user))

@client.event
async def on_message(message):
    print(message.content)
    if not message.content.startswith('!'):
        return
    if message.content == '!quit':
        await client.close()
    if message.content.startswith('!add '):
        if message.guild.id not in grocery_lists:
            grocery_lists[message.guild.id] = []
        add(grocery_lists[message.guild.id], message.content)
    elif message.content == '!list':
        if message.guild.id not in grocery_lists:
            grocery_lists[message.guild.id] = []
        list(grocery_lists[message.guild.id])
    elif message.content == '!clear':
        if message.guild.id in grocery_lists:
            clear(grocery_lists[message.guild.id])
    elif message.content.startswith('!remove '):
        if message.guild.id in grocery_lists:
            remove(grocery_lists[message.guild.id], message.content)

client.run(os.environ.get("TOKEN"))