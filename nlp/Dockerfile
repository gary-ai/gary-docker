FROM debian:jessie
MAINTAINER nandotk <victor@dekalee.fr>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python2.7 \
    python-pip \
    build-essential \
    python-dev

WORKDIR /bot
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

CMD /usr/bin/python2.7 api.py
ENTRYPOINT ["/entrypoint.sh"]
