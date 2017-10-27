DOCKER_IMAGE=victorbalssa/tflearn-nltk:latest

all:
	@make pull
	@make local_test

test:
	@make pull
	@make local_test

travis:
	@make pull
	@make travis_test

pull:
	docker pull $(DOCKER_IMAGE)

local_test:
	docker-compose start
	sleep 1
	sh -c 'docker exec -it gary_nlp ps -eaf'
	sh -c 'docker exec -it gary_nlp py.test -svv test_chatbot.py'

travis_test:
	docker-compose build
	sleep 1
	docker-compose up -d
	sleep 1
	sh -c 'docker exec -it gary_nlp ps -eaf'
	sh -c 'docker exec -it gary_nlp py.test -svv test_chatbot.py'
	@make stop

stop:
	sh -c 'docker stop `docker ps -a -q`'

local_remove:
	@make stop
	sh -c 'docker rm `docker ps -a -q`'
