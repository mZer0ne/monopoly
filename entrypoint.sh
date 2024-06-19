#!/bin/bash

# Go to app folder
cd /app

# Init django database
python manage.py migrate

# Create .po files with new messages
python manage.py makemessages -l ru_RU
#python manage.py makemessages -l ru_SP

# Compile .mo files
python manage.py compilemessages -l ru_RU
#python manage.py compilemessages -l ru_SP

# Run server
python manage.py runserver 0.0.0.0:8000