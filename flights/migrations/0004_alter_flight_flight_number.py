# Generated by Django 3.2.11 on 2022-04-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_flight_flight_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=4),
        ),
    ]
