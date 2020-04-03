# Generated by Django 3.0.5 on 2020-04-03 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('latitude', models.BigIntegerField(default=0, verbose_name='Latitude')),
                ('longitude', models.BigIntegerField(default=0, verbose_name='Longitude')),
                ('created_date_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_date_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Motorista',
                'verbose_name_plural': 'Motoristas',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=20, verbose_name='Placa')),
                ('type', models.CharField(max_length=20, verbose_name='Tipo do Veiculo')),
                ('brand', models.CharField(max_length=20, verbose_name='Marca')),
                ('vehicle_model', models.CharField(max_length=20, verbose_name='Modelo')),
                ('color', models.CharField(max_length=20, verbose_name='Cor')),
                ('created_date_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_date_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Driver', verbose_name='Motorista')),
            ],
            options={
                'verbose_name': 'Veiculo',
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
