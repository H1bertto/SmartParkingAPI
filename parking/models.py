from django.db import models
from account.models import User
from driver.models import Driver
from core.models import Status
from django.dispatch import receiver
from django.db.models.signals import post_save


class Parking(models.Model):
    cnpj = models.CharField("CNPJ", max_length=20, unique=True)
    parking_name = models.CharField("Nome do Estacionamento", max_length=150)
    country = models.CharField("País", max_length=50)
    state = models.CharField("Estado", max_length=50)
    city = models.CharField("Cidade", max_length=100)
    place = models.CharField("Logradouro", max_length=200)
    place_number = models.PositiveIntegerField("Número do Logradouro")
    complement = models.CharField("Complemento", max_length=200, blank=True, null=True)
    latitude = models.FloatField("Latitude", default=0.0)
    longitude = models.FloatField("Longitude", default=0.0)
    opening_time = models.TimeField("Horairo de Abertura")
    closing_time = models.TimeField("Horairo de Fechamento")
    price_per_hour = models.FloatField("Preço por Hora")
    amount_parking_spots = models.IntegerField("Total de Vagas", default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    created_date_at = models.DateTimeField('Registrado em', auto_now_add=True)
    updated_date_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.cnpj

    @property
    def name(self):
        return self.user.full_name

    @property
    def email(self):
        return self.user.email

    @property
    def phone(self):
        return self.user.phone

    @property
    def full_address(self):
        return f'{self.place}, Nº{self.place_number}, {self.city}, {self.state} - {self.country}'

    @property
    def available_parking_spots(self):
        return ParkingSpot.objects.filter(parking__cnpj=self.cnpj, status=1).count()

    class Meta:
        verbose_name = 'Estacionamento'
        verbose_name_plural = 'Estacionamentos'


@receiver(post_save, sender=Parking)
def create_spots(sender, instance, **kwargs):
    new_amount_spots = instance.amount_parking_spots
    old_amount_spots = ParkingSpot.objects.filter(parking=instance).count()
    status = Status.objects.get(pk=1)
    add_spots = False
    if kwargs['created']:
        amount_spots = instance.amount_parking_spots
        add_spots = True
    elif new_amount_spots > old_amount_spots:
        new_amount_spots -= old_amount_spots
        add_spots = True
    if add_spots:
        ParkingSpot.objects.bulk_create([
            ParkingSpot(parking=instance, status=status) for x in range(0, new_amount_spots)
        ],
            batch_size=new_amount_spots
        )


class ParkingSpot(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status")
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, verbose_name="Estacionamento")
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, verbose_name="Motorista", blank=True, null=True)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
