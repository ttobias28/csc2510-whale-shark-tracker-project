IMAGE_NAME = whale-shark-tracker
DOCKER_USER = ttobias42
TAG = latest

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

build:
	docker build -t $(DOCKER_USER)/$(IMAGE_NAME):$(TAG) .

test-docker:
	docker run --rm $(DOCKER_USER)/$(IMAGE_NAME):$(TAG) python -m pytest tests/ -v

run:
	docker run -p 5000:5000 $(DOCKER_USER)/$(IMAGE_NAME):$(TAG)

push:
	docker push $(DOCKER_USER)/$(IMAGE_NAME):$(TAG)

deploy: build push

clean:
	docker system prune -f

.PHONY: install test build test-docker run push deploy clean