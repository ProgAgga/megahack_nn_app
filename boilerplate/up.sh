#!/usr/bin/env bash
python manage.py add_all
python manage.py populate_redis
python manage.py runserver
