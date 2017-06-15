FROM debian:jessie
MAINTAINER nandotk <victor@dekalee.fr>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python2.7 \
    python-pip \
    build-essential \
    python-dev

WORKDIR /bot/gary
RUN mkdir /var/log/connector-slack

CMD pip install -r requirements.txt && /usr/bin/python2.7 /bot/gary/slack_bot_connector.py
