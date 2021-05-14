import graphene
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from project.country.models import City as CityModel
from project.country.models import Country as CountryModel


class CountryType(DjangoObjectType):
    class Meta:
        model = CountryModel
        fields = ("id", "name", "population", "cities")
        filter_fields = {}
        interfaces = (relay.Node,)


class CityType(DjangoObjectType):
    class Meta:
        model = CityModel
        fields = ("id", "name", "population", "country")
        filter_fields = {}
        interfaces = (relay.Node,)


class Query(ObjectType):
    all_countries = DjangoFilterConnectionField(CountryType)
    country = relay.Node.Field(CountryType)
    all_cities = DjangoFilterConnectionField(CityType)
    city = relay.Node.Field(CityType)
    debug = graphene.Field(DjangoDebug, name="_debug")
