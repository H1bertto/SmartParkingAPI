web: gunicorn smartparking.wsgi
worker: celery -A smartparking worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler