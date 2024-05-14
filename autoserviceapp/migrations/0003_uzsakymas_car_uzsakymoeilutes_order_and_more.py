# Generated by Django 4.2.13 on 2024-05-13 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("autoserviceapp", "0002_paslauga_uzsakymas_uzsakymoeilutes_automobilis"),
    ]

    operations = [
        migrations.AddField(
            model_name="uzsakymas",
            name="car",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="autoserviceapp.automobilis",
            ),
        ),
        migrations.AddField(
            model_name="uzsakymoeilutes",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="autoserviceapp.uzsakymas",
            ),
        ),
        migrations.AddField(
            model_name="uzsakymoeilutes",
            name="service",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="autoserviceapp.paslauga",
            ),
        ),
        migrations.AlterField(
            model_name="uzsakymas",
            name="data",
            field=models.DateField(blank=True, null=True, verbose_name="Data"),
        ),
    ]
