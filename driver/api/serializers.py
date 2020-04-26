from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from account.api.serializers import UserSerializer
from driver.models import Driver, Vehicle


class DriverSerializer(ModelSerializer):
    # user = UserSerializer()
    name = ReadOnlyField()
    email = ReadOnlyField()
    phone = ReadOnlyField()

    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'


