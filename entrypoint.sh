#!/bin/sh


python -m poetry run python manage.py migrate
python -m poetry run python manage.py collectstatic --noinput
python -m poetry run daphne -p ${PORT:-8080} -b ${HOST:-0.0.0.0} project.asgi:application
