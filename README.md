# Zelasto Study 1

Python project to evaluate study log files

1. [Log files Structure](#log-files-structure)
2. [Values](#values)

## Log files Structure

`2021-05-11T14:55:08.419Z; INTERACTION; direct;18;14,9,5,1,17;18;1; 0.5099127;0.5482645;-0.449999869;637563489084131200;1;8`

| DateTime (LogServer)     | STATE          | mapping method | Task-No. | Target Layers | Layer-Count | Trial-Idx | PosX             | PosY                                                  | PosZ         | TimeStamp (Server) | InteractionType | CurrentLayer |
| ------------------------ | -------------- | -------------- | --------- | ------------- | ----------- | --------- | ---------------- | ----------------------------------------------------- | ------------ | ------------------ | --------------- | ------------ |
| 2021-05-11T14:55:08.419Z | INTERACTION    | direct         | 18        | 14,9,5,1,17   | 18          | 1         | 0.5099127        | 0.5482645                                             | -0.449999869 | 637563489084131200 | 1               | 8            |
| 2021-05-10T12:14:37.259Z | VIEW           | direct         | 2         | 7,8,1,5,2     | 9           | 0         | TASK_DESCRIPTION |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:37.259Z | TASK           | direct         | 2         | 7,8,1,5,2     | 9           | 0         |                  |                                                       |              |                    |                 |              |
| 2021-05-10T12:13:51.730Z | MAPPING_METHOD | direct         | 1         | 4,5,3,1,2     | 6           | 0         |                  |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:37.264Z | SUBTASK        | direct         | 2         | 7,8,1,5,2     | 9           | 0         | 2                |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:37.265Z | SUBTASK_STATE  | direct         | 2         | 7,8,1,5,2     | 9           | 0         | START            |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:39.587Z | VIEW           | direct         | 2         | 7,8,1,5,2     | 9           | 0         | TASK_VIEW        |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:45.064Z | SUBTASK_STATE  | direct         | 2         | 7,8,1,5,2     | 9           | 0         | HOLD             |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:46.565Z | SUBTASK_STATE  | direct         | 2         | 7,8,1,5,2     | 9           | 0         | COMPLETED        |                                                       |              |                    |                 |              |
| 2021-05-10T12:10:39.115Z | SUBTASK_STATE  | direct         | 1         | 1,5           | 6           | 0         | FAILED           | wrong level approved                                  |              |                    |                 |              |
| 2021-05-10T12:13:38.243Z | SUBTASK_STATE  | densening      | 6         | 3,12          | 14          | 0         | TERMINATED       | switched to other level before hold timeout completed |              |                    |                 |              |

## Values

* Tasks:
  * 1-6 (Test)
  * 1-18 (Block 1)
  * 19-36 (Block 2)
  * 37 - 54 (Block 3)
* 3 Blocks for any mapping method
* STATE:
  
    | State Value    | Description                                       | SubTypes           |
    | -------------- | ------------------------------------------------- | ------------------ |
    | INTERACTION    | Trial interaction                                 | -                  |
    | VIEW           | switched view (describe Task)                     | TASK_VIEW          |
    | VIEW           | switched view (describe Task)                     | Test Run TASK_VIEW |
    |                |                                                   | TASK_DESCRIPTION   |
    | TASK           |                                                   |                    |
    | MAPPING_METHOD | starting to next large block (mapping method)     |                    |
    | SUBTASK        | same as the next: starting to next task           |                    |
    | SUBTASK_STATE  | start of the trial after Subtask                  | START              |
    |                | dwell time in a layer exceeded: hold-timer starts | HOLD               |
    |                | end of the trial (Success)                        | COMPLETED          |
    |                | end of the trial (hold failure                    | TERMINATED         |
    |                | end of the trial (wrong level ?)                  | FAILED             |


