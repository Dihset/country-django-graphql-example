DC=docker-compose
MY_PWD=/home/dihset/Documents/opensource/country-django-graphql-example

.PHONY: create-network
create-network:
	docker network create country-django-graphql-example-network


.PHONY: up-storages
up-storages:
	${DC} -f docker-compose/storages.yml up -d


.PHONY: setup-dev
setup-dev:
	./manage.py runserver 0.0.0.0:8000


.PHONY: testing
testing:
	pytest --cov-report xml:cov.xml --cov .
	sed -i 's#${PWD}#${MY_PWD}#g' ./cov.xml


.PHONY: linting
linting:
	autopep8 --aggressive --experimental -r -i ./project
	black --fast ./project
	isort ./project
	flake8 ./project
