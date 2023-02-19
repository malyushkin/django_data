# Generated by Django 4.1.6 on 2023-02-15 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("postcards", "0008_alter_location_check_by_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postcard",
            name="to_location_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="to_location_id",
                to="postcards.location",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="postcard",
            name="from_location_id",
            field=models.ForeignKey(
                default=22,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="from_location_id",
                to="postcards.location",
            ),
        ),
    ]