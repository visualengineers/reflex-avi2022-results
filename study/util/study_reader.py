import csv

from study.util.study_states import StudyStates


class StudyReader:
    __file: str
    __maxTaskTest = 6
    __maxTaskStudy = 54

    def __init__(self, file: str):
        self.__file = file

    def read(self):
        with open(self.__file, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            headers = next(reader)
            print(headers)

            task_no = 0
            tests_completed = False
            skip = True
            line = 2

            for row in reader:
                t = row[3]
                s = StudyStates[row[1].strip()]
                line += 1
                if s == StudyStates.INTERACTION:
                    continue
                else:
                    print(f'Line: {line} - {row}')
                    break

                if t > task_no:
                    task_no = t

                if task_no == self.__maxTaskTest and t < task_no:
                    tests_completed = True
                    break;



    def __extract_interaction(self, row: list[str]):
        if len(row) != 14:
            print(row)