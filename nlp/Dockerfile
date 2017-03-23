FROM debian:jessie
MAINTAINER nandotk <victor@dekalee.fr>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python2.7 \
    python-pip \
    virtualenv \
    && apt-get autoremove \
    && apt-get clean

RUN pip install slackclient

CMD ["/usr/bin/python2.7", "/bot/gary/starterbot.py"]
