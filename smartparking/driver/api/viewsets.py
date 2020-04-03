from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from driver.models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class VehicleViewSet(ModelViewSet):

    serializer_class = VehicleSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Vehicle.objects.filter(driver__user=self.request.user)


class DriverViewSet(ModelViewSet):

    serializer_class = DriverSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Driver.objects.filter(user=self.request.user)
