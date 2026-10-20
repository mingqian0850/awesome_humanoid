# 工业操作：移动方式与手部任务分别看

[首页](../README.md) · [English](industrial-task-and-data.en.md)

资料核对：2026-10-20；整理：2026-10-21。工程建议不代表已复现的实验。


## 两个独立的维度

| 维度 | 应当区分的情况 |
| --- | --- |
| 移动 | 固定工位；移动到位再操作；行走与操作持续耦合；轮式底盘协同 |
| 操作 | 取放搬运；准确放入工装；接触装配；多指／手内操作 |

搬运任务不自动等于复杂 loco-manipulation，精确放置也不自动要求灵巧手。这里用“持续耦合”说明协调需求；论文对 loco-manipulation 的定义可能更宽，应读其任务设置。

## 工业证据怎么读

[Figure 02 / BMW](https://www.figure.ai/news/production-at-bmw) 是已结束的钣金上料案例，涉及步态与手眼协调。[龙旗 / G2](https://us.longcheer.com/en/col76/260.html) 描述平板测试上下料及设备通信。这些资料支持具体工序能力，不能推导整个行业的市场占比或通用精密装配能力。

## 数据随任务增加什么

- 工位操作：双臂／手状态、命令、相机、工件／工装坐标和标定。
- 移动到位：补充底座位姿、到位条件、停靠误差和重新标定需求。
- 持续耦合：进一步记录全身参考和反馈、足底接触、负载、控制周期及失败事件。
- 接触装配：根据工艺记录力／力矩或触觉及质量结果；视觉成功与工艺合格分开。

这是建议检查项，并非每个公开数据集都包含这些信号。没有传感器支持的量标为 unknown。

## 阅读练习

先读 [Atlas / TRI 的遥操作与训练说明](https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/)，再看 [GMR](https://github.com/YanjieZe/GMR) 的运动输入。为一个上料任务画出“参考运动—控制器—执行反馈”，指出哪些量只能从机器人获取。

机器人型号未知时，先学习双臂动作语义、坐标和时间同步；确认需要移动后再深入全身跟踪。用一页任务／信号表完成练习，无需训练。

继续：[数据采集五类路线](https://github.com/mingqian0850/awesome_vla_deployment/blob/main/docs/zh/02-data-sources.md) · [重定向输入检查](https://github.com/YanjieZe/GMR)。
