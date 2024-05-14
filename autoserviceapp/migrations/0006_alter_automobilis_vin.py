# Generated by Django 4.2.13 on 2024-05-13 06:18

import autoserviceapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autoserviceapp", "0005_alter_automobilis_vin_alter_paslauga_kaina_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="automobilis",
            name="vin",
            field=models.IntegerField(
                default=autoserviceapp.models.make_random_vin, verbose_name="VIN code"
            ),
        ),
    ]