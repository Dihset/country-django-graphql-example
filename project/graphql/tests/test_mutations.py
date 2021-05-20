import pytest
from pytest_factoryboy import register

from project.country.models import City, Country
from project.country.tests.factories import CountryFactory
from project.graphql.query import CountryType
from project.graphql.utils import CustomNode

register(CountryFactory, "country_1")


@pytest.mark.usefixtures("client_query")
@pytest.mark.django_db
def test_create_country(client_query, faker):
    query = """
        mutation($name:String!, $population: Int!){
          createCountry(name: $name, population: $population){
            country{
              id
            }
          }
        }
    """
    variables = {
        "name": faker.pystr(),
        "population": faker.pyint(),
    }
    response = client_query(query, variables=variables)
    content = response.json()
    country_node_id = content["data"]["createCountry"]["country"]["id"]
    (
        _,
        country_id,
    ) = CustomNode.from_global_id(country_node_id)
    assert Country.objects.filter(
        pk=country_id,
        name=variables["name"],
        population=variables["population"],
    ).exists()


@pytest.mark.usefixtures("client_query")
@pytest.mark.django_db
def test_create_city(client_query, faker, country_1):
    query = """
        mutation ($name: String!, $population: Int!, $country_id: String!) {
          createCity(name: $name, population: $population, countryId: $country_id) {
            city {
              id
            }
          }
        }
    """
    variables = {
        "name": faker.pystr(),
        "population": faker.pyint(),
        "country_id": CustomNode.to_global_id(CountryType.__name__, country_1.pk),
    }
    response = client_query(query, variables=variables)
    content = response.json()
    city_node_id = content["data"]["createCity"]["city"]["id"]
    (
        _,
        city_id,
    ) = CustomNode.from_global_id(city_node_id)
    assert City.objects.filter(
        pk=city_id,
        country_id=country_1.pk,
        name=variables["name"],
        population=variables["population"],
    ).exists()
