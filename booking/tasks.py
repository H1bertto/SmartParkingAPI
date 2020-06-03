from __future__ import absolute_import, unicode_literals
from celery import shared_task

from smartparking.settings import CELERY_BROKER_URL
import redis

r = redis.from_url(CELERY_BROKER_URL)
pipe = r.pipeline()


@shared_task
def realtime_update_spots(parking_id):
    from parking.models import Parking
    park = Parking.objects.get(pk=parking_id)

    pipe.publish(park.pk, park.available_parking_spots)
    pipe.execute()
