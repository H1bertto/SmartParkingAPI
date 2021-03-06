from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from driver.models import Driver, Vehicle
from account.models import User
from .serializers import DriverSerializer, VehicleSerializer, PostVehicleSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class VehicleViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return PostVehicleSerializer
        return VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.filter(driver=self.request.user.driver)
        # return Vehicle.objects.all()


class DriverViewSet(ModelViewSet):

    serializer_class = DriverSerializer
    permission_classes = []
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        if self.action == 'create':
            return Driver.objects.filter(user=self.request.user)
        else:
            self.permission_classes = [IsAuthenticated]
            return Driver.objects.filter(user=self.request.user)

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
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)