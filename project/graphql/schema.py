import graphene

from .mutations import Mutation
from .query import Query

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
