# Industrial manipulation: separate mobility from hand tasks

[Home](../README.md) · [中文](industrial-task-and-data.zh-CN.md)

Sources reviewed: 2026-10-20; compiled: 2026-10-21. Engineering recommendations are not reproduced experiments.


## Two independent dimensions

| Dimension | Cases to distinguish |
| --- | --- |
| Mobility | Station work; move then manipulate; continuously coupled locomotion/manipulation; wheeled-base coordination |
| Manipulation | Transport/pick-and-place; fixture placement; contact assembly; multifinger/in-hand manipulation |

Transport does not automatically imply complex loco-manipulation, and accurate placement need not require a dexterous hand. “Continuously coupled” describes coordination demand here; papers may use broader definitions, so read their task setup.

## Reading industrial evidence

[Figure 02 / BMW](https://www.figure.ai/news/production-at-bmw) is a completed sheet-metal loading case involving stepping and hand–eye coordination. [Longcheer / G2](https://us.longcheer.com/en/col76/260.html) describes tablet-test loading/unloading and equipment communication. These establish specific process capabilities, not industry market share or general precision assembly.

## Signals added by the task

- Station work: arm/hand states, commands, cameras, part/fixture frames and calibration.
- Move then manipulate: add base pose, arrival criteria, docking error and recalibration requirements.
- Continuous coupling: add whole-body references and feedback, foot contacts, payload, control timing and failures.
- Contact assembly: record force/torque or tactile signals as required and quality outcomes; visual completion and process acceptance differ.

These are suggested checks, not fields present in every public dataset. Mark unsupported measurements unknown.

## Reading exercise

Read [Atlas / TRI's teleoperation and training description](https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/), then inspect motion inputs in [GMR](https://github.com/YanjieZe/GMR). Draw reference motion → controller → execution feedback for a loading task, marking quantities only available from the robot.

With an unknown embodiment, start with bimanual action semantics, frames and synchronization; study whole-body tracking when mobility is required. Produce a one-page task/signal table without training.

Continue: [five capture routes](https://github.com/mingqian0850/awesome_vla_deployment/blob/main/docs/02-data-sources.md) · [retargeting input checks](https://github.com/YanjieZe/GMR).
