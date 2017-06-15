#!/bin/sh

cd /bot
pip install -r requirements.txt

# some other deploy stuff

exec "$@"
