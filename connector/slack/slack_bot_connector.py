import os
import asyncio
import requests
from slackclient import SlackClient
import time
import datetime as dt
from bot_id_getter import bot_id_getter
from slackclient import SlackClient


# min required is SLACK_BOT_TOKEN
BOT_ID = os.environ.get("SLACK_BOT_ID")

if __name__ == "__main__":
    print("Connection failed. Invalid Slack token or bot ID?")
    while True:
        pass
