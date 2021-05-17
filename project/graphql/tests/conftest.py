import pytest
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client):
    """Create GraphQL django client."""
    return lambda *args, **kwargs: graphql_query(*args, **kwargs, client=client)
