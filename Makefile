DC=docker-compose
MY_PWD=/home/dihset/Documents/opensource/country-django-graphql-example

.PHONY: create-network
create-network:
	docker network create country-django-graphql-example-network


.PHONY: up-storages
up-storages:
	${DC} -f docker-compose/storages.yml up -d


.PHONY: build
build:
	docker build -t country-django-graphql-example-django .


.PHONY: setup-dev
setup-dev:
	poetry run python manage.py runserver 0.0.0.0:8000


.PHONY: testing
testing:
	poetry run pytest --cov-report xml:cov.xml --cov .
	sed -i 's#${PWD}#${MY_PWD}#g' ./cov.xml


.PHONY: linting
linting:
	python -m poetry run autopep8 --aggressive --experimental -r -i ./project
	python -m poetry run black --fast ./project
	python -m isort ./project
	python -m pflake8 ./project
