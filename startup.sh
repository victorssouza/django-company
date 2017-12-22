#!/bin/sh

SERVER_HOST='0.0.0.0'
SERVER_PORT=8000

if [[ ! -f db.sqlite3  ]]; then
    echo 'sqllite3 database is not created yet. Starting Django Migrations...'
    python3 manage.py makemigrations employees
    python3 manage.py migrate
    python3 manage.py loaddata employees/fixtures.json
fi

python3 manage.py test

echo 'Running server at port 8000'
python3 manage.py runserver ${SERVER_HOST}:${SERVER_PORT}