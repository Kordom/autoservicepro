# Generated by Django 4.2.13 on 2024-05-13 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("autoserviceapp", "0010_uzsakymas"),
    ]

    operations = [
        migrations.CreateModel(
            name="UzsakymoEilutes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("kiekis", models.IntegerField(verbose_name="Kiekis")),
                ("kaina", models.FloatField(verbose_name="Kaina")),
                (
                    "paslauga",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autoserviceapp.paslauga",
                    ),
                ),
                (
                    "uzsakymas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="autoserviceapp.uzsakymas",
                    ),
                ),
            ],
        ),
    ]