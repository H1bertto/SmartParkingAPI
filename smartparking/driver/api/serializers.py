from rest_framework.serializers import ModelSerializer
from account.api.serializers import UserSerializer
from driver.models import Driver, Vehicle


class DriverSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'


