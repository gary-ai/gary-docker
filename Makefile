DOCKER_IMAGE=victorbalssa/nlp-container:v1.0.0

all:
	@make pull
	@make build
	@make test

pull:
	docker pull $(DOCKER_IMAGE)

build:
	docker-compose up -d --build
	docker-compose ps
	sh -c 'docker exec gary_nlp_1 python fixture.py &>/dev/null'
	sh -c 'docker exec gary_nlp_1 python training.py &>/dev/null'

test:
	sh -c 'docker exec -it gary_nlp_1 py.test -svv test_chatbot.py'

stop:
	sh -c 'docker stop `docker ps -a -q`'

local_train_ai:
	docker-compose start
	sh -c 'docker exec gary_nlp_1 python training.py &>/dev/null'

local_test:
	docker-compose start
	sh -c 'docker exec -it gary_nlp_1 py.test -svv test_chatbot.py'

local_remove:
	@make stop
	sh -c 'docker rm `docker ps -a -q`'
