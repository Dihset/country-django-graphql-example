from django.db.models.signals import post_save
from django.dispatch import receiver

from project.country.models import Country

from .subscription import OnNewCountry


@receiver(post_save, sender=Country)
def broadcast_country(sender, instance, **kwargs):
    OnNewCountry.new_country(instance)
