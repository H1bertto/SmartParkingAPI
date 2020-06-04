from django.test import TestCase

# Create your tests here.

# import redis
# import time
# from random import randint
#
# r = redis.from_url('redis://h:p922bd68c74dc9b926463915c2a70923f99696c5bce3f5b14f22b58cf23dcee40@ec2-35-171-200-85.compute-1.amazonaws.com:23629')
#
#
# pipe = r.pipeline()
#
# x = 10
# while x > 0:
#     pipe.publish(f'Estacionamento: {randint(100, 999)}', f'Vagas: {randint(0, 50)}')
#     pipe.execute()
#     x -= 1
#     time.sleep(2)