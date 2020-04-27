from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from driver.models import Driver, Vehicle
from account.models import User
from .serializers import DriverSerializer, VehicleSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class VehicleViewSet(ModelViewSet):

    serializer_class = VehicleSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        # return Vehicle.objects.filter(driver__user=self.request.user.id)
        return Vehicle.objects.all()


class DriverViewSet(ModelViewSet):

    serializer_class = DriverSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        # if self.request.user.id:
        #     return Driver.objects.filter(user=self.request.user)
        # else:
        return Driver.objects.all()

    def create(self, request, *args, **kwargs):
        f_name = request.data["name"].split(' ')[0]
        l_name = request.data["name"].split(' ')[1:]
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