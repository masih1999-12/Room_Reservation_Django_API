# Generated by Django 5.0.4 on 2024-04-26 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_point_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
