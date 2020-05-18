from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from booking.models import Booking
from .serializers import BookingSerializer, LiteBookingSerializer


class BookingViewSet(ModelViewSet):

    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return LiteBookingSerializer
        return BookingSerializer
