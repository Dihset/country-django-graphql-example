#!/bin/sh


poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput
poetry run daphne -p 8080 -b 0.0.0.0 project.asgi:application