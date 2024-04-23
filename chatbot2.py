import discord
from dotenv import load_dotenv
import os
import logging
import asyncio
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

load_dotenv('.env.local')

# lets bot subscribe to bucket of events
intents = discord.Intents.default()
intents.message_content = True

# connection to discord
client= discord.Client(intents=intents)

# set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# load recipes dataset
recipes = pd.read_csv('./data/recipes_dataset/RAW_recipes.csv')

# when bot online
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# bot actions/event
@client.event
async def on_message(message):
    # want bot to overlook own msgs
    if message.author == client.user:
        return

    # user prompts with $foodie
    if message.content.startswith('$foodie'):

        # initial bot response
        await message.channel.send('Hello! What type of food recommendations are you in the mood for?')
        
        # loop to let user ask for many recs until they say "thank you!"
        def check(m):
            return m.author == message.author and m.channel == message.channel
        
        while True:
            try:
                msg = await client.wait_for('message', check=check, timeout=120.0)
                if msg.content.lower() == "thank you!":
                    await message.channel.send('you\'re welcome! ask for more recommendations later!')
                    break
                if msg:
                    response = get_recommendation(msg.content)
                    await message.channel.send(f'{response}\n\nwhat other type of food would you like to be recommended?')
            except asyncio.TimeoutError:
                await message.channel.send("time out, please try again!")
                break


def get_recommendation(ingredients):
    return  "How about ordering take out?"


client.run(os.getenv('BOT_TOKEN'), log_handler=handler)
