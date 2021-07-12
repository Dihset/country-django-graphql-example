from .loaders import CityByCountryIdLoader, CountryByIdLoader


class Loaders:
    country_by_id = CountryByIdLoader()
    city_by_country_id = CityByCountryIdLoader()


class LoaderMiddleware:
    def resolve(self, next, root, info, **args):
        if not hasattr(info.context, "loaders"):
            info.context.loaders = Loaders()
        return next(root, info, **args)
