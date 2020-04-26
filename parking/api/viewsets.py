from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from parking.models import ParkingSpot, Parking
from .serializers import ParkingSerializer, LiteParkingSerializer, ParkingSpotSerializer


class ParkingViewSet(ModelViewSet):

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return LiteParkingSerializer
        return ParkingSerializer

    def get_queryset(self):
        if self.request.user.id:
            return Parking.objects.filter(user=self.request.user)
        else:
            return Parking.objects.all()

    def create(self, request, *args, **kwargs):
        amount_parking_spots = request.data.pop("amount_parking_spots")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        parking_pk = Parking.objects.get(cnpj=request.data.get("cnpj")).pk
        ParkingSpot.objects.bulk_create([
            ParkingSpot(parking=parking_pk, status=1)],
            batch_size=int(str(amount_parking_spots))
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ParkingSpotViewSet(ModelViewSet):

    serializer_class = ParkingSpotSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    http_method_names = ['get', 'patch']

    def get_queryset(self):
        if self.request.user.id:
            return ParkingSpot.objects.filter(parking__user=self.request.user)
        else:
            return ParkingSpot.objects.all()