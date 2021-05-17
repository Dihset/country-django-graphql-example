import pytest
from pytest_factoryboy import register

from project.country.tests.factories import CityFactory, CountryFactory
from project.helpers.dict_factoy import factory_to_dict

register(CountryFactory, "country_1")
register(CountryFactory, "country_2")
register(CountryFactory, "country_3")
register(CountryFactory, "country_4")

register(CityFactory, "city_1")
register(CityFactory, "city_2")
register(CityFactory, "city_3")
register(CityFactory, "city_4")


@pytest.mark.usefixtures("client_query")
@pytest.mark.django_db
def test_get_one_country(client_query, country_1):
    query = """
        query ($countryId: ID!) {
            country(id: $countryId) {
                name
                population
            }
        }
    """
    variables = {"countryId": f"CountryType:{country_1.pk}"}
    response = client_query(query, variables=variables)
    content = response.json()
    assert content["data"]["country"] == factory_to_dict(country_1, exclude=["id"])


@pytest.mark.usefixtures("client_query")
@pytest.mark.django_db
def test_get_one_city(client_query, city_1):
    query = """
        query ($cityId: ID!) {
            city(id: $countryId) {
                name
                population
            }
        }
    """
    variables = {"cityId": f"CityType:{city_1.pk}"}
    response = client_query(query, variables=variables)
    content = response.json()
    assert content["data"]["country"] == factory_to_dict(city_1, exclude=["id"])
