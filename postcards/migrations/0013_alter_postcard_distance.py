# Generated by Django 4.1.6 on 2023-02-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postcards", "0012_alter_postcard_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postcard",
            name="distance",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
