from django.db import models
from account.models import User


class Driver(models.Model):
    cpf = models.CharField("CPF", max_length=20)
    latitude = models.FloatField("Latitude", default=0.0)
    longitude = models.FloatField("Longitude", default=0.0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    created_date_at = models.DateTimeField('Registrado em', auto_now_add=True)
    updated_date_at = models.DateTimeField('Atualizado em', auto_now=True)

    @property
    def name(self):
        return self.user.full_name

    @property
    def email(self):
        return self.user.email

    @property
    def phone(self):
        return self.user.phone

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'


class Vehicle(models.Model):
    plate = models.CharField("Placa", max_length=20)
    type = models.CharField("Tipo do Veiculo", max_length=20)
    brand = models.CharField("Marca", max_length=20)
    vehicle_model = models.CharField("Modelo", max_length=20)
    color = models.CharField("Cor", max_length=20)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="Motorista")
    created_date_at = models.DateTimeField('Registrado em', auto_now_add=True)
    updated_date_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.plate

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
