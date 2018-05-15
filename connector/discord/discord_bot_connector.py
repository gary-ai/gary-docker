import os
import time
import requests
import discord
import logging


TOKEN = os.environ.get("DISCORD_TOKEN")
client = discord.Client()


def handle_command(user_id, user_entry, user_chan):
    print(user_id, user_entry, user_chan)
    response = "Hum ... I can't access to natural language processing service. :robot_face:"
    try:
        r = requests.get('http://nlp:5000/api/message/' + user_id + '/' + user_chan + '/' + user_entry + '/').json()
        if r and 'response' in r and r['response']['message']:
            response = r['response']['message']
    except ValueError:
        print ("chat_response: can't decode json from nlp api")
    return response


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    rep = 'error :robot:'
    if message.channel.is_private:
        rep = handle_command(message.author.id, message.content, message.channel.id)
    await client.send_message(message.channel, rep)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
