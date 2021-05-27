# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from util import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reader = stat_reader.StatReader('../data/depthlayers.csv')
    stats = reader.get_stats()
    for stat in stats:
        print(stat)

    data_reader = study_reader.StudyReader('../data/01.csv')
    data_reader.read()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
