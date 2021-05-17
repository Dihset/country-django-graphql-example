from typing import Any, Dict

from factory import Factory
from factory.base import StubObject


def factory_to_dict(factory: Factory, exclude=()) -> Dict[str, Any]:
    def filter_func(item):
        key, _ = item
        return all(key != "_state", key is not exclude)

    stub_dict = dict(filter(filter_func, factory.__dict__.items()))
    for key, value in stub_dict.items():
        if isinstance(value, StubObject):
            stub_dict[key] = value.to_dict()
    return stub_dict
