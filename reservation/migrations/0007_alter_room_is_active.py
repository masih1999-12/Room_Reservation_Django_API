# Generated by Django 5.0.4 on 2024-08-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_room_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
