#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py add_data
#python manage.py runserver

 gunicorn musical.wsgi:application --bind 0.0.0.0:8000

