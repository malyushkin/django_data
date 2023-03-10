# Generated by Django 4.1.6 on 2023-02-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=128)),
                ("full_name", models.CharField(max_length=128)),
                ("raw_address", models.TextField()),
                ("check_by", models.CharField(blank=True, max_length=128, null=True)),
                ("google_place_id", models.TextField(blank=True, null=True)),
                ("country_alpha2", models.CharField(max_length=2)),
                ("country_alpha3", models.CharField(max_length=3)),
                ("lat", models.FloatField()),
                ("lng", models.FloatField()),
            ],
            options={
                "ordering": ["country_alpha2", "country_alpha3", "full_name"],
            },
        ),
    ]
