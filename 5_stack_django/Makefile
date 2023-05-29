SHELL := /bin/bash
.SILENT:
.PHONY: help
.DEFAULT_GOAL := help

SOME_FOLDER := /path/to/folder
DOCKER_CONTAINER_NAME := container_name
DOCKER_IMAGE_NAME := docker_image_name

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)



##@ General Docker UTILS

docker-clean: ## remove all dangling images, containers
	docker system prune


##@ Local Stack Management

up:	## Start development
	@echo ""
	@echo ""
	@echo "#########  Restarting stack #######"
	@echo $(shell date)
	docker-compose  up -d

stop:	## stop the containers
	@echo "Stopping running container"
	docker-compose  stop

down:   ## stop containers and removes the stopped containers as well as any networks that were created.
	docker-compose  down

restart:	down up

logs:   ## show logs of web
	docker-compose -f docker-compose.yml logs web

##@ Code Management

build:	## build web image
	@echo ""
	@echo "Starting docker-compose.yml"
	@echo ""
	@docker-compose build

makemigrations:	## Execute django command makemigrations
	@echo ""
	@echo "Executing command: python manage.py makemigrations"
	@echo ""
	@docker-compose exec web python manage.py makemigrations

migrate:	## Execute django command migrate
	@echo ""
	@echo "Executing command: python manage.py migrate"
	@echo ""
	@docker-compose exec web python manage.py migrate

collectstatic:	## Execute django command collectstatic
	@echo ""
	@echo "Executing command: python manage.py collectstatic"
	@echo ""
	@docker-compose exec web python manage.py collectstatic

