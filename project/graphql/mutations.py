import graphene
from graphql_relay.node.node import from_global_id

from project.country.models import Country as CountryModel
from project.country.models import City as CityModel

from .query import CityType, CountryType


class CreateCountry(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        population = graphene.Int(required=True)

    country = graphene.Field(CountryType)

    @classmethod
    def mutate(cls, root, info, name: str, population: int):
        country = CountryModel(name=name, population=population)
        country.save()
        return cls(country=country)


class CreateCity(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        population = graphene.Int(required=True)
        country_id = graphene.String(required=True)

    city = graphene.Field(CityType)

    @classmethod
    def mutate(cls, root, info, name: str, population: int, country_id: str):
        _type, country_pk = from_global_id(country_id)
        if _type != CountryType.__name__:
            raise Exception("Some_error")
        country = CountryModel.objects.filter(pk=country_pk).first()
        if not country:
            raise Exception("some_error")
        city = CityModel(name=name, population=population, country=country)
        city.save()
        return cls(city=city)


class Mutation(graphene.ObjectType):
    create_country = CreateCountry.Field()
    create_city = CreateCity.Field()
