FROM node:argon

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install pm2 -g

VOLUME ["/usr/src/app"]
ADD ./docker/start.sh /start.sh
RUN chmod 755 /start.sh
EXPOSE 8080
ENTRYPOINT ["/start.sh"]
