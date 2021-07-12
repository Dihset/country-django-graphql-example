from __future__ import annotations

import logging

import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from project.country.models import City as CityModel
from project.country.models import Country as CountryModel

from .utils import CustomNode


class CountryType(DjangoObjectType):
    class Meta:
        model = CountryModel
        fields = ("id", "name", "population", "cities")
        filter_fields = {}
        interfaces = (CustomNode,)
        use_connection = True

    @staticmethod
    def resolve_cities(root: CountryType, info, **kwargs):
        return info.context.loaders.city_by_country_id.load(root.pk)


class CityType(DjangoObjectType):
    class Meta:
        model = CityModel
        fields = ("id", "name", "population", "country")
        filter_fields = {}
        interfaces = (CustomNode,)
        use_connection = True

    @staticmethod
    def resolve_country(root: CityType, info, **kwargs):
        return info.context.loaders.country_by_id.load(root.country_id)


class Query(ObjectType):
    all_countries = DjangoFilterConnectionField(CountryType)
    country = CustomNode.Field(CountryType)
    all_cities = DjangoFilterConnectionField(CityType)
    city = CustomNode.Field(CityType)
    debug = graphene.Field(DjangoDebug, name="_debug")
