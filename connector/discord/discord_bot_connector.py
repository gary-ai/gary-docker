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
            #print ("chat_response: " + r['response']['message'].encode("utf8"))
            response = r['response']['message']
    except ValueError:
        print ("chat_response: can't decode json from nlp api")
    return response


def parse_discord_output(discord_output):
    output = discord_output.content
#    if output and len(output) > 0 and 'gary' in output:
    return discord_output.author.id, output.encode("utf8"), discord_output.channel
#    return '', '', ''


@client.event
async def on_message(message):
# we do not want the bot to reply to itself
    if message.author == client.user:
        return
    command = parse_discord_output(message)
    print(message.content)
    print(message.author.id)
    print(message.channel.id)
    rep = 'error :robot:'
    if command:
        rep = handle_command(message.author.id, message.content, message.channel.id)
    await client.send_message(message.channel, rep)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
