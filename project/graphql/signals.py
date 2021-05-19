from django.db.models.signals import post_save
from django.dispatch import receiver

from project.country.models import City, Country

from .subscription import OnNewCity, OnNewCountry


@receiver(post_save, sender=Country)
def broadcast_country(sender, instance, **kwargs):
    OnNewCountry.new_country(instance)


@receiver(post_save, sender=City)
def broadcast_city(sender, instance, **kwargs):
    OnNewCity.new_city(instance)
