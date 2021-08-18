import graphene

from .mutations import Mutation
from .query import Query
from .subscription import Subscription

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
)
