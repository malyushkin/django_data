# Generated by Django 4.1.6 on 2023-02-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postcards", "0013_alter_postcard_distance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postcard",
            name="distance",
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
    ]