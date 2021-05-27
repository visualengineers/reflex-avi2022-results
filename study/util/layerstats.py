from . import mapping_methods as mm

from typing import Tuple


class LayerStats:
    __mapping_method__: mm.MappingMethods
    __num_layers__: int
    __borders__: list[float]

    def __init__(self, method: mm.MappingMethods, num_layers: int, borders: list[float]):
        self.__mapping_method__ = method
        self.__num_layers__ = num_layers
        self.__borders__ = borders

    def get(self) -> Tuple[int, mm.MappingMethods, list[float]]:
        return self.__num_layers__, self.__mapping_method__, self.__borders__

    def __str__(self):
        return f'{self.__num_layers__} ({self.__mapping_method__}): [ {" | ".join([str(bd) for bd in self.__borders__])} ]'

    def __repr__(self):
        return self.__str__()
