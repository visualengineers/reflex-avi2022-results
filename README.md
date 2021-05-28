# Zelasto Study 1

Python project to evaluate study log files

1. [Log files Structure](#log-files-structure)
2. [Values](#values)
3. [order of states](#order-of-states)
4. [Layers Statistics file](#layers-statistics-file)

## Log files Structure

`2021-05-11T14:55:08.419Z; INTERACTION; direct;18;14,9,5,1,17;18;1; 0.5099127;0.5482645;-0.449999869;637563489084131200;1;8`

| DateTime (LogServer)     | STATE          | mapping method | Task-No. | Target Layers | Layer-Count | Trial-Idx | PosX             | PosY                                                  | PosZ         | TimeStamp (Server) | InteractionType | CurrentLayer |
| ------------------------ | -------------- | -------------- | -------- | ------------- | ----------- | --------- | ---------------- | ----------------------------------------------------- | ------------ | ------------------ | --------------- | ------------ |
| 2021-05-11T14:55:08.419Z | INTERACTION    | direct         | 18       | 14,9,5,1,17   | 18          | 1         | 0.5099127        | 0.5482645                                             | -0.449999869 | 637563489084131200 | 1               | 8            |
| 2021-05-10T12:14:37.259Z | VIEW           | direct         | 2        | 7,8,1,5,2     | 9           | 0         | TASK_DESCRIPTION |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:37.259Z | TASK           | direct         | 2        | 7,8,1,5,2     | 9           | 0         |                  |                                                       |              |                    |                 |              |
| 2021-05-10T12:13:51.730Z | MAPPING_METHOD | direct         | 1        | 4,5,3,1,2     | 6           | 0         |                  |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:37.264Z | SUBTASK        | direct         | 2        | 7,8,1,5,2     | 9           | 0         | 2                |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:37.265Z | SUBTASK_STATE  | direct         | 2        | 7,8,1,5,2     | 9           | 0         | START            |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:39.587Z | VIEW           | direct         | 2        | 7,8,1,5,2     | 9           | 0         | TASK_VIEW        |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:45.064Z | SUBTASK_STATE  | direct         | 2        | 7,8,1,5,2     | 9           | 0         | HOLD             |                                                       |              |                    |                 |              |
| 2021-05-10T12:14:46.565Z | SUBTASK_STATE  | direct         | 2        | 7,8,1,5,2     | 9           | 0         | COMPLETED        |                                                       |              |                    |                 |              |
| 2021-05-10T12:10:39.115Z | SUBTASK_STATE  | direct         | 1        | 1,5           | 6           | 0         | FAILED           | wrong level approved                                  |              |                    |                 |              |
| 2021-05-10T12:13:38.243Z | SUBTASK_STATE  | densening      | 6        | 3,12          | 14          | 0         | TERMINATED       | switched to other level before hold timeout completed |              |                    |                 |              |

## Values

* Tasks:
  * 1-6 (Test)
  * 1-18 (Block 1)
  * 19-36 (Block 2)
  * 37 - 54 (Block 3)
* 3 Blocks for any mapping method
* STATE:
  
    | State Value        | Description                                       | SubTypes           |
    | ------------------ | ------------------------------------------------- | ------------------ |
    | __INTERACTION__    | Trial interaction                                 | -                  |
    | __VIEW__           | switched view (describe Task)                     | TASK_VIEW          |
    |                    | switched view in test runs (describe Task)        | Test Run TASK_VIEW |
    |                    |                                                   | TASK_DESCRIPTION   |
    | __TASK__           |                                                   |                    |
    | __MAPPING_METHOD__ | starting to next large block (mapping method)     |                    |
    | __SUBTASK__        | same as the next: starting to next task           |                    |
    | __SUBTASK_STATE__  | start of the trial after Subtask                  | START              |
    |                    | dwell time in a layer exceeded: hold-timer starts | HOLD               |
    |                    | end of the trial (Success)                        | COMPLETED          |
    |                    | end of the trial (hold failure                    | TERMINATED         |
    |                    | end of the trial (wrong level ?)                  | FAILED             |

* mapping method  
  describes, how layers are aligned:
  * __direct__ (equivalent distance)
  * __densening__ (larger distance on top, decreasing with depth value)
  * __widening__ (narrower distance on top, increasing with depth value)
* Task-No.
  * running number of tasks
* Target Layers, Trial-Idx
  * array of targets for each layer in current Task
  * trial-Index (zero based) describes target layer for current trial
* Layer-Count
  * number of max layers in Task
* PosX, PosY, PosZ
  * Positions received from Tracking Server
  * PosX / PosY in range [0, 1]
  * PosZ in range [-1, 1] with 0 = on the surface / no interaction, -1 max push, +1 max pull
* Timestamp (Server)
  * timestamp received from Tracking server: miliseconds based unix time stamp
* InteractionType
  * type recognized from server (1 = PUSH)
* current layer
  * layer associated with received depth value

## order of states

1. START (missing on first trial !) OR
   * start of an new task
2. TASK_VIEW / TASK_DESCRIPTION
   
3. HOLD
4. COMPLETED / TERMINATED / FAILED
   

## Layers Statistics file

__Location:__ `data/depthlayers.csv` [File](data/depthlayers.csv)

`6; direct; 0 | 1 | 2 | 3 | 4 | 5 | 6; 0 | 0.0834 | 0.25 | 0.4167 | 0.5834 | 0.75 | 0.9167 | 1`

| NUM_LAYERS       | MAPPING_METHOD            | DEPTH_LAYER_ID                         | DEPTH_LAYER_BORDER              |
| ---------------- | ------------------------- | -------------------------------------- | ------------------------------- |
| number of layers | mapping method for  block | idx of the depth layer in border array | start depths for each layer idx |

* mapping of layers to depth ranges for better evaluation how "good" a depth layer has been hit
