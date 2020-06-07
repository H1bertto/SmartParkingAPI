from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from account.models import User
from rest_framework import status
from rest_framework import filters
from parking.models import ParkingSpot, Parking
from booking.models import Booking
from django.contrib.auth.hashers import make_password
from .serializers import ParkingSerializer, LiteParkingSerializer, ParkingSpotSerializer
import math


class ParkingViewSet(ModelViewSet):

    permission_classes = []
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return LiteParkingSerializer
        return ParkingSerializer

    def get_queryset(self):
        # if self.request.user.id:
        #     return Parking.objects.filter(user=self.request.user)
        # else:
        # return Parking.objects.all()

        # ------------ = ---lat---,---lon---
        # Point format = 99.999999,99.999999
        public = self.request.query_params.get('public', False)
        point = self.request.query_params.get('point', False)
        km = int(self.request.query_params.get('km', '5')) * 1000
        if point and public:
            lat, lon = (float(i) for i in point.split(','))
            r_earth = 6378000
            lat_const = 180 / math.pi
            lon_const = lat_const / math.cos(lat * math.pi / 180)
            min_latitude = lat - (km / r_earth) * lat_const
            max_latitude = lat + (km / r_earth) * lat_const
            min_longitude = lon - (km / r_earth) * lon_const
            max_longitude = lon + (km / r_earth) * lon_const
            return Parking.objects.filter(latitude__range=[min_latitude, max_latitude], longitude__range=[min_longitude, max_longitude])
        elif public or self.action == 'create':
            try:
                int(public)
                return Parking.objects.filter(pk=public)
            except ValueError:
                return Parking.objects.all()
        else:
            self.permission_classes = [IsAuthenticated]
            return Parking.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        f_name = request.data["name"].split(' ')[0]
        l_name = request.data["name"].split(' ')[1:]
        l_name = ' '.join(l_name)
        user = User.objects.create(
            email=request.data["email"],
            username=request.data["email"],
            first_name=f_name,
            last_name=l_name,
            phone=request.data["phone"],
            password=make_password(request.data["password"]),
        )
        request.data['user'] = user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # parking_pk = Parking.objects.get(cnpj=request.data.get("cnpj")).pk
        # ParkingSpot.objects.bulk_create([
        #     ParkingSpot(parking=parking_pk, status=1)],
        #     batch_size=int(str(request.data["amount_parking_spots"]))
        # )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ParkingSpotViewSet(ModelViewSet):

    serializer_class = ParkingSpotSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'patch']

    def get_queryset(self):
        return ParkingSpot.objects.filter(parking__user=self.request.user).order_by('id')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.data.get("its_coming_out", False):
            register = Booking.objects.filter(parking_spot_id=instance.pk, driver_id=instance.driver.pk, total_price=0, parking_spot__status_id=2)
            if register.count() == 1:
                book = Booking.objects.get(parking_spot_id=instance.pk, driver_id=instance.driver.pk, total_price=0, parking_spot__status_id=2)
                book.its_coming_out = True
                book.save()
                return Response({"Exit": "Successful"})
            return Response({"Exit": "Fail"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
