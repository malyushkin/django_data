# Generated by Django 4.1.6 on 2023-02-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postcards", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("name", models.CharField(max_length=1)),
            ],
        ),
    ]
