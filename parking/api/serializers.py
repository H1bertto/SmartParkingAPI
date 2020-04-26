from rest_framework.serializers import ModelSerializer, ReadOnlyField
from account.api.serializers import UserSerializer
from parking.models import ParkingSpot, Parking


class ParkingSerializer(ModelSerializer):
    user = UserSerializer()
    full_address = ReadOnlyField()
    amount_parking_spots = ReadOnlyField()
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

    class Meta:
        model = ParkingSpot
        fields = '__all__'


