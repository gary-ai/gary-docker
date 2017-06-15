# gary-docker

## Container

- ./slack-connector : NLP python Real time messaging API Slack
- ./messenger-connector : NLP python Real time messaging API Messenger
- ./mongo : MongoDB

## Launch garybot on your slack

`$ git clone git@github.com:gary-ai/gary-docker.git`

`$ git clone git@github.com:gary-ai/gary-connector-slack.git`

`$ cd gary-docker`

`$ touch .env`

Checkout your token on slack api info and paste them in .env file:

`$ echo "SLACK_BOT_TOKEN=xxx" > .env`

`$ echo "SLACK_BOT_ID=xxx" >> .env`

`$ docker-compose build`

`$ docker-compose create`

`$ docker-compose start`

Garybot should be started

To see container running :

`$ docker-compose ps`


### How to restart slackbot manually:

`$ docker exec -it garydocker_slackconnector_1 bash`

`$ cd /bot/gary/`

`$ python slack_bot_connector.py`
