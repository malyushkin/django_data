from django.contrib import admin
from .models import Location, Postcard


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = (
        "name",
        "country_alpha2",
        "raw_address",
        "check_by",
    )


class PostcardAdmin(admin.ModelAdmin):
    model = Location
    list_display = (
        "custom_title",
        "custom_distance",
        "sent_date",
        "received_date",
        "status",
    )

    def custom_title(self, obj):
        return f"{obj.from_location_id} – {obj.to_location_id}"

    custom_title.short_description = "Direction"

    def custom_distance(self, obj):
        return f"{round(obj.distance, 2)} km"

    custom_distance.short_description = "Distance"


admin.site.register(Location, LocationAdmin)
admin.site.register(Postcard, PostcardAdmin)
