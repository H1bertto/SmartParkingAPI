from django.db import models
from account.models import User
from driver.models import Driver
from core.models import Status


class Parking(models.Model):
    cnpj = models.CharField("CNPJ", max_length=20, unique=True)
    parking_name = models.CharField("Nome do Estacionamento", max_length=150)
    country = models.CharField("País", max_length=50)
    state = models.CharField("Estado", max_length=50)
    city = models.CharField("Cidade", max_length=100)
    place = models.CharField("Logradouro", max_length=200)
    place_number = models.PositiveIntegerField("Número do Logradouro")
    complement = models.CharField("Complemento", max_length=200, blank=True, null=True)
    latitude = models.BigIntegerField("Latitude", default=0)
    longitude = models.BigIntegerField("Longitude", default=0)
    opening_time = models.TimeField("Horairo de Abertura")
    closing_time = models.TimeField("Horairo de Fechamento")
    price_per_hour = models.FloatField("Preço por Hora")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    created_date_at = models.DateTimeField('Registrado em', auto_now_add=True)
    updated_date_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.cnpj

    @property
    def full_address(self):
        return f'{self.place}, Nº{self.place_number}, {self.city}, {self.state} - {self.country}'

    @property
    def amount_parking_spots(self):
        return len(ParkingSpot.objects.filter(parking__cnpj=self.cnpj).values_list(flat=True))

    @property
    def available_parking_spots(self):
        return len(ParkingSpot.objects.filter(parking__cnpj=self.cnpj, status=1).values_list(flat=True))

    class Meta:
        verbose_name = 'Estacionamento'
        verbose_name_plural = 'Estacionamentos'


class ParkingSpot(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status")
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, verbose_name="Estacionamento")
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, verbose_name="Motorista", blank=True, null=True)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
