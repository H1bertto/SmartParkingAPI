from __future__ import absolute_import, unicode_literals
from django.conf import settings
from django.apps import apps
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartparking.settings')

app = Celery('smartparking', backend=settings.CELERY_RESULT_BACKEND)

# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object(settings, namespace='CELERY')

# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task(bind=True)
def debug_task(self):
    # print('Request: {0!r}'.format(self.request))
    print('Foi')

# celery -A smartparking worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A smartparking worker -l info -P gevent
# celery -A smartparking beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
