# Generated by Django 5.0.6 on 2024-06-06 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0004_delete_umidadedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UmidadeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_smart.sensor')),
            ],
        ),
    ]