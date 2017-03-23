# gary-docker

## Container

- gary/gary-nlp : NLP python Real time messaging API

## Launch garybot

`$ git clone git@github.com:gary-ai/gary-docker.git`

`$ git clone git@github.com:gary-ai/gary-nlp.git`

`$ cd gary-docker`

`$ touch .env`

Checkout your token on slack api info :

`$ echo "SLACK_BOT_TOKEN=xxx" > .env`

`$ echo "BOT_ID=xxx" >> .env`

`$ docker-compose build`

`$ docker-compose create`

`$ docker-compose start`

Garybot should be started

To see container running :

`$ docker-compose ps`


### How to restart bot manually:

`$ docker exec -it garydocker_application_1 bash`

`/# cd /bot/gary/`

`/# python starterbot.py`
