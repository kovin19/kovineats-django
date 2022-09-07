#!/bin/bash
python3 manage.py makemigrations
sleep 2
python3 manage.py migrate
sleep 2
python3 manage.py seed_data
sleep 2
python3 manage.py runserver
