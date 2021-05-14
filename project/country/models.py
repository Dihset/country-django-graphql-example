from django.db import models


class Country(models.Model):
    name = models.CharField("Название", max_length=64)
    population = models.IntegerField("Население")

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField("Название", max_length=64)
    population = models.IntegerField("Население")
    country = models.ForeignKey(
        Country,
        verbose_name="Страна",
        related_name="cities",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name
