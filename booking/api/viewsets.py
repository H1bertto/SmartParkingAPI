from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from booking.models import Booking
from .serializers import BookingSerializer, LiteBookingSerializer
from parking.models import ParkingSpot
from driver.models import Driver
from core.models import Status
from random import randint
from booking.tasks import realtime_update_spots


class BookingViewSet(ModelViewSet):

    # queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return LiteBookingSerializer
        return BookingSerializer

    def get_queryset(self):
        # book_code = self.request.query_params.get('book_code', False)
        booked = self.request.query_params.get('booked', False)
        busy = self.request.query_params.get('busy', False)
        if booked:
            spots = ParkingSpot.objects.filter(parking__user=self.request.user, status_id=4)
            return Booking.objects.filter(parking__user=self.request.user, parking_spot__in=spots)
        elif busy:
            spots = ParkingSpot.objects.filter(parking__user=self.request.user, status_id=2)
            return Booking.objects.filter(parking__user=self.request.user, parking_spot__in=spots)
        else:
            return Booking.objects.filter(parking__user=self.request.user)

    def create(self, request, *args, **kwargs):
        if ParkingSpot.objects.filter(driver_id=request.data['driver']).count():
            return Response({'401 - Não Autorizado': 'Motorista Já Está no Estacionamento'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.data.get('book_to', False):
            if ParkingSpot.objects.filter(driver_id=request.data['driver']).count():
                return Response({'401 - Não Autorizado': 'Vaga Já Reservada'}, status=status.HTTP_401_UNAUTHORIZED)
            request.data['book_code'] = randint(100000, 999999)
            spot = ParkingSpot.objects.filter(status_id=1, parking_id=request.data['parking']).first()
            spot.driver = Driver.objects.get(pk=request.data['driver'])
            spot.status = Status.objects.get(pk=4)
            spot.save()
            request.data['parking_spot'] = spot.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        realtime_update_spots.delay(request.data['parking'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
