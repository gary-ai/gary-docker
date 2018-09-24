
import os
import asyncio
import requests
from slackclient import SlackClient
import time, datetime as dt
from bot_id_getter import bot_id_getter
from slackclient import SlackClient


# min required is SLACK_BOT_TOKEN
BOT_ID = os.environ.get("SLACK_BOT_ID")
sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


@asyncio.coroutine
def handle_command(user_id, user_entry, user_chan):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    yield from asyncio.sleep(1)
    print (user_id, user_entry, user_chan)
    response = "Hum ... I can't access to natural language processing service. :robot_face:"
    try:
        r = requests.get('http://nlp:5000/api/message/' + user_id + '/' + user_chan + '/' + user_entry + '/').json()
        print (r)
        if r and 'response' in r and r['response']['message']:
            response = r['text']
    except ValueError:
        print ("chat_response: can't decode json from nlp api")
    return response


@asyncio.coroutine
def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    yield from asyncio.sleep(1)
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                return output['user'], output['text'], output['channel']
    return None, None, None


@asyncio.coroutine
def listen():
    yield from asyncio.sleep(1)
    # rtm_read() read everything from websocket !
    rtm_message = sc.rtm_read()
    print (rtm_message)
    user_id, command, channel = yield from parse_slack_output(rtm_message)
    if command and channel and user_id != BOT_ID:
        msg = yield from handle_command(user_id, command, channel)
        sc.rtm_send_message(channel, msg)

    asyncio.async(listen())


def main():
    print('here we go')
    sc.rtm_connect()
    loop = asyncio.get_event_loop()
    asyncio.async(listen())
    loop.run_forever()


if __name__ == '__main__':
    main()
