FROM python:3.5
MAINTAINER victorbalssa <balssa_v@etna-alternance.net>

ADD ./requirements.txt /bot/requirements.txt
WORKDIR /bot
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./slack_bot_connector.py"]
