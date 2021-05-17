from django.contrib import admin

from .models import City, Country


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "population",
    )


class CityAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "population",
    )


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
