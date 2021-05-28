import csv
from typing import Optional, Tuple

from .layerstats import LayerStats
from .mapping_methods import MappingMethods
from .study_states import StudyStates


class StudyReader:
    __file: str
    __maxTaskTest = 6
    __maxTaskStudy = 54

    __stats: list[LayerStats]

    def __init__(self, file: str, stats: list[LayerStats]):
        self.__file = file
        self.__stats = stats

    def read(self):
        with open(self.__file, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            task_no = 0
            tests_completed = False
            skip = True
            line = 0

            for row in reader:
                t = int(row[3].strip())
                s = self.__extract_state__(row)
                line += 1

                if t > task_no:
                    task_no = t

                if task_no == self.__maxTaskTest and t < task_no:
                    tests_completed = True

                if s == StudyStates.INTERACTION and tests_completed:
                    continue
                else:
                    print(f'Task: {task_no} | Line: {line} - {row}')

    @staticmethod
    def __extract_interaction__(row: list[str]):
        if len(row) != 14:
            print(row)

    @staticmethod
    def __extract_state__(row: list[str]) -> StudyStates:
        return StudyStates[row[1].strip()]

    @staticmethod
    def __extract_mapping_method__(row: list[str]) -> MappingMethods:
        return MappingMethods[row[2].strip()]

    def __get_depths(self, layer: int, num_layers: int, mm: MappingMethods) -> Optional[Tuple[float, float]]:
        result = None
        for stat in self.__stats:
            if stat.is_associated_stat(num_layers, mm):
                result = stat.get_depth_range(layer)

        return result
