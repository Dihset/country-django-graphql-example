import channels_graphql_ws
import graphene

from .mutations import Mutation
from .query import Query
from .subscription import Subscription


class GraphqlWsConsumer(channels_graphql_ws.GraphqlWsConsumer):
    """Channels WebSocket consumer which provides GraphQL API."""

    schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
