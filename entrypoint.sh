#!/bin/sh


venv/bin/python manage.py migrate
venv/bin/python manage.py collectstatic --noinput
venv/bin/gunicorn --bind :8080 --workers ${WORKERS} project.wsgi:application