FROM debian:jessie
MAINTAINER nandotk <victor@dekalee.fr>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python2.7 \
    python-pip \
    build-essential \
    python-dev

WORKDIR /bot/nlp
RUN mkdir /var/log/nlp

CMD pip install -r requirements.txt && /usr/bin/python2.7 api.py > /var/log/nlp/output.txt
