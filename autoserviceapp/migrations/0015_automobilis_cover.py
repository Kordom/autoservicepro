# Generated by Django 4.2.13 on 2024-05-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autoserviceapp", "0014_alter_automobiliomodelis_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="automobilis",
            name="cover",
            field=models.ImageField(
                blank=True, null=True, upload_to="covers", verbose_name="Virselis"
            ),
        ),
    ]