import factory

from ..models import City, Country


class CountryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("pystr")
    population = factory.Faker("pyint")

    class Meta:
        model = Country


class CityFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("pystr")
    population = factory.Faker("pyint")

    class Meta:
        model = City
