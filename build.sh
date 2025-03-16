#!/usr/bin/env bash

# install dependencies
pip install -r requirements.txt

# migrate and collect static files
python manage.py migrate
python manage.py collectstatic --noinput
