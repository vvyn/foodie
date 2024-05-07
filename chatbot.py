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
                # get recommendation response
                #recommendation = rec_food(msg.content)
                #data_test = get_data(msg.content)
                #label_test = find_related_foods(get_label(msg.content))
                label_test2 = rec_food(msg.content)
                #label_test2 = get_label2(msg.content)
                #label_test2 = get_data(msg.content)
                #label_test2 = find_related_foods(get_label(msg.content))              
                await message.channel.send(f'{label_test2}\n\nwhat other type of food would you like to be recommended?')
            except asyncio.TimeoutError:
                await message.channel.send("time out, please try again!")
                break



def rec_food(query):
    if 'fishy' in query:
        return 'how about sushi, grilled salmon, or fried cod?'
    elif 'sweet' in query:
        return 'how about cheesecake, cherries, or chocolate?'
    elif 'salty' in query:
        return 'how about french fries or ramen?'
    elif 'breakfast' in query:
        return 'how about over easy eggs with sourdough bread or oatmeal with berries?'
    elif 'lunch' in query:
        return 'how about a burrito, fried chicken, or shawarma?'
    elif 'dinner' in query:
        return 'how about pesto pasta or tomato soup?'
    else:
        'how about pizza?'

def get_data(item):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f'''
    SELECT ?item ?itemLabel WHERE {{
        ?item wdt:P31 wd:Q2095;
        rdfs:label ?itemLabel.
        FILTER(CONTAINS(LCASE(?itemLabel), LCASE("{item}"))).
        FILTER(LANG(?itemLabel) = "en").
    }}
    LIMIT 5
    ''')

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert() 

    results_df = pd.json_normalize(results['results']['bindings'])
    return results_df[['item.value', 'itemLabel.value']].to_string(index=False)



def get_label2(item):
    #food_keywords = ['pizza', 'cake', 'soup', 'burger', 'salad', 'steak', 'pasta', 'curry', 'bread', 'cheese']

    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f'''
    SELECT ?item ?itemLabel WHERE {{
      SERVICE wikibase:mwapi {{
        bd:serviceParam wikibase:endpoint "www.wikidata.org";
        wikibase:api "EntitySearch";
        mwapi:search "{item}";
        mwapi:language "en".
        ?item wikibase:apiOutputItem mwapi:item.
      }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    LIMIT 10
    ''')

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert() 

    print(results)
    return results




def get_label(search_term):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery =  (f"""
    SELECT ?item WHERE {{
      SERVICE wikibase:mwapi {{
        bd:serviceParam wikibase:endpoint "www.wikidata.org";
        wikibase:api "EntitySearch";
        mwapi:search "{search_term}";
        mwapi:language "en".
        ?item wikibase:apiOutputItem mwapi:item.
      }}
    }}
    LIMIT 1
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results['results']['bindings'][0]['item']['value'] if results['results']['bindings'] else None

def find_related_foods(item_id):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f'''
    SELECT ?item ?itemLabel WHERE {{
        ?item wdt:P361 wd:"{item_id}";
        FILTER(CONTAINS(LCASE(?itemLabel), LCASE("{item}"))).
        FILTER(LANG(?itemLabel) = "en").
    }}
    LIMIT 5
    ''')
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return [(result['foodLabel']['value']) for result in results['results']['bindings']]


client.run(os.getenv('BOT_TOKEN'), log_handler=handler)
