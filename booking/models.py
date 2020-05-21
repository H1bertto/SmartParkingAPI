from django.db import models
from driver.models import Driver
from parking.models import Parking, ParkingSpot
from core.models import Status
from django.dispatch import receiver
from django.db.models.signals import post_save


class Booking(models.Model):
    check_in = models.DateTimeField('Check In', auto_now_add=True)
    check_out = models.DateTimeField('Check Out', auto_now=True)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, verbose_name="Estacionamento")
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE, verbose_name="Vaga")
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="Motorista")
    book_to = models.TimeField('Reserva para às', blank=True, null=True)
    total_time = models.TimeField("Tempo Total", blank=True, null=True)
    total_price = models.FloatField("Preço Total", default=0)
    its_coming_out = models.BooleanField("Está Saindo?", default=False)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Livro de Registro'
        verbose_name_plural = 'Livro de Registros'


@receiver(post_save, sender=Booking)
def update_total_time(sender, instance, **kwargs):
    if instance.its_coming_out:
        # Gera o Valor total a Pagar
        instance.total_time = instance.check_out - instance.check_in
        instance.total_price = (
            int(instance.total_time.seconds//3600) +
            1 if int((instance.total_time.seconds//60) % 60) > 10 else 0
        ) * instance.parking.price_per_hour
        instance.total_time = f'{instance.total_time}'
        instance.its_coming_out = False
        instance.save()
        # Libera a Vaga
        instance.parking_spot.status = Status.objects.get(pk=1)
        instance.parking_spot.driver = None
        instance.parking_spot.save()
    if not instance.its_coming_out and instance.parking_spot.status.pk == 1 and instance.total_time is None:
        instance.parking_spot.status = Status.objects.get(pk=2)
        instance.parking_spot.driver = instance.driver
        instance.parking_spot.save()
    if not instance.its_coming_out and instance.parking_spot.status.pk == 4 and instance.total_time is None:
        instance.parking_spot.status = Status.objects.get(pk=2)
        instance.parking_spot.save()
