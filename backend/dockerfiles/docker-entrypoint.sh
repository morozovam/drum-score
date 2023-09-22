#!/bin/sh
python /app/manage.py collectstatic --noinput
python manage.py migrate --noinput || exit 1
python manage.py ensure_adminuser --no-input
#gunicorn backend.wsgi:application --bind 0.0.0.0:8000
exec "$@"
