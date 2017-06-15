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

WORKDIR /bot/nlp
RUN mkdir /var/log/nlp
RUN touch /var/log/nlp/output.txt

CMD pip install -r requirements.txt && /usr/bin/python2.7 /bot/nlp/app.py > /var/log/nlp/output.txt
