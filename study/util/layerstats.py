from . import mapping_methods as mm

from typing import Tuple


class LayerStats:
    __mapping_method: mm.MappingMethods
    __num_layers: int
    __borders: list[float]

    def __init__(self, method: mm.MappingMethods, num_layers: int, borders: list[float]):
        self.__mapping_method = method
        self.__num_layers = num_layers
        self.__borders = borders

    def get(self) -> Tuple[int, mm.MappingMethods, list[float]]:
        return self.__num_layers, self.__mapping_method, self.__borders

    def __str__(self):
        return f'{self.__num_layers} ({self.__mapping_method}): [ {" | ".join([str(bd) for bd in self.__borders])} ]'

    def __repr__(self):
        return self.__str__()
