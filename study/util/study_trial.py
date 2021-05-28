from datetime import datetime

from .study_trial_result import StudyTrialResult
from .interaction import Interaction
from .study_depth_layer import StudyDepthLayer


class StudyTrial:
    __start: datetime
    __finish: datetime
    __result: StudyTrialResult
    __interactions: list[Interaction]

    __trial_index: int
    __layer: StudyDepthLayer

    def __init__(self):
        pass

    def add_interaction(self, i: Interaction):
        self.__interactions.append(i)

    def get_duration(self) -> int:
        return (self.__finish - self.__start).microseconds

