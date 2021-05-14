import pytest
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client):
    return lambda *args, **kwargs: graphql_query(*args, **kwargs, client=client)


def test_ok(client_query):
    query = """
        query {
            hello
        }
    """
    response = client_query(query)
    content = response.json()
    assert "errors" not in content
    assert content["data"]["hello"] == "Hi!"
