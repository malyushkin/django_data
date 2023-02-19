import geopy.distance

from django.db import models
from django.urls import reverse
from .config import (
    LOCATION_TYPE_CHOICES,
    LOCATION_CHECK_BY_CHOICES,
    POSTCARD_STATUS_CHOICES,
)
from .utils import fetch_country_codes


class Location(models.Model):
    """Location object"""

    name = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Name",
    )

    full_name = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Full Name",
    )

    country_alpha2 = models.CharField(
        max_length=2,
        choices=fetch_country_codes(),
        null=False,
        verbose_name="Country",
    )

    raw_address = models.TextField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=16,
        choices=LOCATION_TYPE_CHOICES,
        null=False,
        default="person",
    )

    check_by = models.CharField(
        max_length=128,
        choices=LOCATION_CHECK_BY_CHOICES,
        null=True,
    )

    google_place_id = models.TextField(
        null=True,
        default=None,
        blank=True,
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=False,
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=False,
    )

    class Meta:
        ordering = ["country_alpha2", "full_name"]

    def get_absolute_url(self):
        return reverse("location", args=[str(self.id)])

    def __str__(self):
        return f"{self.name}"


class Postcard(models.Model):
    """Postcard object"""

    from_location_id = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="from_location_id",
    )

    to_location_id = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="to_location_id",
    )

    distance = models.FloatField(
        null=True,
        blank=True,
        editable=False,
    )

    status = models.CharField(
        max_length=16, choices=POSTCARD_STATUS_CHOICES, null=False, default="sent"
    )

    sent_date = models.DateField(auto_now=False)

    received_date = models.DateField(auto_now=False, null=True, blank=True)

    class Meta:
        ordering = ["sent_date", "received_date"]

    def get_absolute_url(self):
        return reverse("postcard", args=[str(self.id)])

    def save(self, *args, **kwargs):
        location_from = Location.objects.get(id=self.from_location_id_id)
        location_to = Location.objects.get(id=self.to_location_id_id)

        from_point = (location_from.latitude, location_from.longitude)
        to_point = (location_to.latitude, location_to.longitude)

        self.distance = geopy.distance.geodesic(from_point, to_point).km

        super(Postcard, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.from_location_id} – {self.to_location_id}"
