from .mapping_methods import MappingMethods

from typing import Tuple


class LayerStats:
    __mapping_method: MappingMethods
    __num_layers: int
    __borders: list[float]

    def __init__(self, method: MappingMethods, num_layers: int, borders: list[float]):
        self.__mapping_method = method
        self.__num_layers = num_layers
        self.__borders = borders

    def get(self) -> Tuple[int, MappingMethods, list[float]]:
        return self.__num_layers, self.__mapping_method, self.__borders

    def is_associated_stat(self, num_layers: int, mm: MappingMethods) -> bool:
        return self.__num_layers == num_layers and self.__mapping_method == mm

    def get_depth_range(self, layer_idx: int) -> Tuple[float, float]:
        return self.__borders[layer_idx], self.__borders[layer_idx + 1]

    def __str__(self):
        return f'{self.__num_layers} ({self.__mapping_method}): [ {" | ".join([str(bd) for bd in self.__borders])} ]'

    def __repr__(self):
        return self.__str__()
