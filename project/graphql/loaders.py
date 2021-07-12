import logging
from collections import defaultdict

from promise import Promise
from promise.dataloader import DataLoader

from project.country.models import City as CityModel
from project.country.models import Country as CountryModel


class CountryByIdLoader(DataLoader):
    def batch_load_fn(self, keys: list):
        results_by_ids = {
            result.pk: result for result in CountryModel.objects.filter(pk__in=keys)
        }
        return Promise.resolve([results_by_ids.get(key, None) for key in keys])


class CityByCountryIdLoader(DataLoader):
    def batch_load_fn(self, keys: list):
        city_by_article_ids = defaultdict(list)
        for city in CityModel.objects.filter(country_id__in=keys):
            city_by_article_ids[city.country_id].append(city)
        return Promise.resolve([city_by_article_ids.get(key, []) for key in keys])
