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


class BookingViewSet(ModelViewSet):

    queryset = Booking.objects.all()
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return LiteBookingSerializer
        return BookingSerializer

    def create(self, request, *args, **kwargs):
        if request.data.get('book_to', False):
            if ParkingSpot.objects.filter(driver_id=request.data['driver']).count():
                return Response({'401 - Não Autorizado': 'Vaga Já Reservada'}, status=status.HTTP_401_UNAUTHORIZED)
            spot = ParkingSpot.objects.filter(status_id=1, parking_id=request.data['parking']).first()
            spot.driver = Driver.objects.get(pk=request.data['driver'])
            spot.status = Status.objects.get(pk=4)
            spot.save()
            request.data['parking_spot'] = spot.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
