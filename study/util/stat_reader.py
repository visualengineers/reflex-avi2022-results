import csv

from typing import Optional

from . import layerstats as stats
from . import mapping_methods as mm


class StatReader:
    __stats__: list[stats.LayerStats]

    def __init__(self, file: str):
        self.__stats__ = self.__readStats__(file)

    def get_stats(self):
        return self.__stats__

    def __readStats__(self, file: str) -> list[stats.LayerStats]:
        with open(file, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            # skip header by iterating over first row
            # alternative: slicing an iterable -
            # result = [self.__parseRow__(row) for row in islice(reader, 1, None)]
            headers = next(reader)

            result = [self.__parseRow__(row) for row in reader]

        return result

    @staticmethod
    def __parseRow__(row: list[str]) -> Optional[stats.LayerStats]:
        if len(row) != 4:
            return None

        mapping: mm.MappingMethods = mm.MappingMethods[row[1].strip()]
        borders = [float(val) for val in row[3].split(" | ")]

        return stats.LayerStats(mapping, int(row[0]), borders)
