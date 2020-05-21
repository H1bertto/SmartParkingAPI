from rest_framework.serializers import ModelSerializer, ReadOnlyField
from account.api.serializers import UserSerializer
from parking.models import ParkingSpot, Parking


class ParkingSerializer(ModelSerializer):
    # user = UserSerializer()
    name = ReadOnlyField()
    email = ReadOnlyField()
    phone = ReadOnlyField()
    full_address = ReadOnlyField()
    available_parking_spots = ReadOnlyField()

    class Meta:
        model = Parking
        fields = '__all__'


class LiteParkingSerializer(ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'


class ParkingSpotSerializer(ModelSerializer):
    # parking = ParkingSerializer()
    driver_name = ReadOnlyField()
    status_title = ReadOnlyField()

    class Meta:
        model = ParkingSpot
        fields = '__all__'


