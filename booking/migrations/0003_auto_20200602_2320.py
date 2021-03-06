# Generated by Django 3.0.5 on 2020-06-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_book_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='book_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Código da Reserva'),
        ),
        migrations.AddField(
            model_name='booking',
            name='its_coming_in',
            field=models.BooleanField(default=False, verbose_name='Está Entrando?'),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='book_to',
        ),
    ]
