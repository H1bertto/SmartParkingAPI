from django.test import TestCase

# Create your tests here.
# import math
# from geopy.distance import geodesic
#
# location = '50.966086,5.502027'
# lat, lon = (float(i) for i in location.split(','))
# r_earth = 6378000
# lat_const = 180 / math.pi
# lon_const = lat_const / math.cos(lat * math.pi / 180)
#
# # dx = distance in meters on x axes (longitude)
# dx = 5000
# new_longitude = lon + (dx / r_earth) * lon_const
# # new_longitude = round(new_longitude, 6)
#
# # dy = distance on y axes (latitude)
# dy = 5000
# new_latitude = lat + (dy / r_earth) * lat_const
# # new_latitude = round(new_latitude, 6)
# new_location = ','.join([str(new_latitude), str(new_longitude)])
#
# dist_to_location = geodesic(location, new_location)
# print(location)
# print(new_location)
# print(dist_to_location)
#
# print('---')
#
# # dx = distance in meters on x axes (longitude)
# dx = 5000
# new_longitude = lon + (dx / r_earth) * lon_const
# new_longitude = round(new_longitude, 6)
#
# # dy = distance on y axes (latitude)
# dy = -5000
# new_latitude = lat + (dy / r_earth) * lat_const
# new_latitude = round(new_latitude, 6)
#
# new_location = ','.join([str(new_latitude), str(new_longitude)])
#
# dist_to_location = geodesic(location, new_location)
# print(location)
# print(new_location)
# print(dist_to_location)
