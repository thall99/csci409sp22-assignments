# Generated by Django 3.2.11 on 2022-02-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20220222_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_number',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
