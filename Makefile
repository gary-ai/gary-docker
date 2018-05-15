DOCKER_IMAGE=victorbalssa/tflearn-nltk:latest

all:
	@make pull
	@make build
	@make test

pull:
	docker pull $(DOCKER_IMAGE)

build:
	docker-compose up -d --build
	sh -c 'docker exec gary_nlp python training.py'

test:
	sh -c 'docker exec -it gary_nlp py.test -svv test_chatbot.py'

stop:
	sh -c 'docker stop `docker ps -a -q`'

local_train_ai:
	docker-compose start
	sh -c 'docker exec gary_nlp python training.py &>/dev/null'

local_test:
	docker-compose start
	sh -c 'docker exec -it gary_nlp py.test -svv test_chatbot.py'

local_remove:
	@make stop
	sh -c 'docker rm `docker ps -a -q`'
