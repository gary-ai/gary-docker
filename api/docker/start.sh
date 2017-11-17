#!/bin/bash

if [ -z "$NODE_ENV" ]; then
    export NODE_ENV=development
fi

cd /usr/src/app
npm install
cd /usr/src/app
pm2 start -x $APP --name="app" --no-daemon --watch
