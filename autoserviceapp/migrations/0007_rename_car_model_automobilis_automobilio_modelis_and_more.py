# Generated by Django 4.2.13 on 2024-05-13 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("autoserviceapp", "0006_alter_automobilis_vin"),
    ]

    operations = [
        migrations.RenameField(
            model_name="automobilis",
            old_name="car_model",
            new_name="automobilio_modelis",
        ),
        migrations.RemoveField(
            model_name="uzsakymas",
            name="car",
        ),
        migrations.RemoveField(
            model_name="uzsakymoeilutes",
            name="order",
        ),
        migrations.RemoveField(
            model_name="uzsakymoeilutes",
            name="service",
        ),
        migrations.AddField(
            model_name="uzsakymas",
            name="automobilis",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="autoserviceapp.automobilis",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="uzsakymoeilutes",
            name="paslauga",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="autoserviceapp.paslauga",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="uzsakymoeilutes",
            name="uzsakymas",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="autoserviceapp.uzsakymas",
            ),
            preserve_default=False,
        ),
    ]