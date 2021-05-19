import channels_graphql_ws
import graphene

from project.country.models import Country as CountryModel

from .query import CountryType


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


class Subscription(graphene.ObjectType):
    """GraphQL subscriptions."""

    on_new_country = OnNewCountry.Field()
