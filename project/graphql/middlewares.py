from .loaders import CityByCountryIdLoader, CountryByIdLoader


class Loaders:
    def __init__(self):
        self.country_by_id = CountryByIdLoader()
        self.city_by_country_id = CityByCountryIdLoader()


def loader_middleware(next, root, info, **args):
    if not hasattr(info.context, "loaders"):
        info.context.loaders = Loaders()
    return next(root, info, **args)
