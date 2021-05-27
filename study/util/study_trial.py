from datetime import datetime

from . import study_trial_result as st, interaction as it


class StudyTrial:
    __start: datetime
    __finish: datetime
    __result: st.StudyTrialResult
    __interactions: list[it.Interaction]

    def __init__(self):
        pass

    def get_duration(self) -> int:
        return (self.__finish - self.__start).microseconds
