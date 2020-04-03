from rest_framework.serializers import ModelSerializer, ReadOnlyField
from driver.api.serializers import DriverSerializer
from parking.api.serializers import ParkingSerializer
from booking.models import Booking


class BookingSerializer(ModelSerializer):
    driver = DriverSerializer()
    parking = ParkingSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class LiteBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
