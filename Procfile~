web: gunicorn game.wsgi --log-file -
web: python manage.py collectstatic --noinput ; gunicorn game.wsgi
