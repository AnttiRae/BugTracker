#!/bin/sh

echo "ENTRYPOINT TEST --- WORKING"

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"