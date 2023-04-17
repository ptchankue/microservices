#!/bin/bash

echo yes | python manage.py collectstatic

sleep 5

python manage.py makemigrations --merge && python manage.py migrate

sleep 2

gunicorn microservices.wsgi:application -b 0:8000 -w 1 --log-level DEBUG --reload
