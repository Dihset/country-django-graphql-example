from django.apps import AppConfig


class GraphqlConfig(AppConfig):
    name = "project.graphql"

    def ready(self):
        import project.graphql.signals  # noqa
