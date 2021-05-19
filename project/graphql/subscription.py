import channels_graphql_ws
import graphene

from project.country.models import City as CityModel
from project.country.models import Country as CountryModel

from .query import CityType, CountryType
from .utils import CustomNode


class OnNewCountry(channels_graphql_ws.Subscription):
    """Subscription triggers on a new country."""

    country = graphene.Field(CountryType)

    def publish(self, info, **kwargs):
        return OnNewCountry(country=self.get("country"))

    @classmethod
    def new_country(cls, country: CountryModel):
        cls.broadcast(
            payload={"country": country},
        )


class OnNewCity(channels_graphql_ws.Subscription):
    """Subscription triggers on a new city."""

    class Arguments:
        country_id = graphene.String(required=True)

    city = graphene.Field(CityType)

    def publish(self, info, country_id, **kwargs):
        _type, _country_id = CustomNode.from_global_id(country_id)
        if _type != CountryType.__name__:
            raise Exception("some error")
        city = self.get("city")
        if city.country_id != int(_country_id):
            return OnNewCity.SKIP
        return OnNewCity(city=city)

    @classmethod
    def new_city(cls, city: CityModel):
        cls.broadcast(
            payload={"city": city},
        )


class Subscription(graphene.ObjectType):
    """GraphQL subscriptions."""

    on_new_country = OnNewCountry.Field()
    on_new_city = OnNewCity.Field()
