# Generated by Django 5.0.6 on 2024-05-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Temperatura', 'Temperatura'), ('Umidade', 'Umidade'), ('Contador', 'Contador'), ('Luminosidade', 'Luminosidade')], max_length=50)),
                ('mac_address', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('localizacao', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=100)),
                ('unidade_medida', models.CharField(blank=True, max_length=20, null=True)),
                ('observacao', models.TextField(blank=True)),
            ],
        ),
    ]
