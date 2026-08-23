# 🗺 Humanoid Loco-Manipulation 学习路线（Roadmap）

> 目标：成为能够**实际研究** humanoid loco-manipulation 的 researcher —— 能读前沿论文、搭 Isaac Lab 环境、训练/修改 locomotion 与 whole-body policy、做 motion retargeting、最终搭 VLA + learned WBC 系统。
> **不是**传统机器人控制理论专家路线。理论 20–30%，代码/实验 70–80%。

## 文件导航

| 文件 | 内容 | 对应你的问题 |
|---|---|---|
| [01-kinematics-dynamics.md](01-kinematics-dynamics.md) | 运动学/动力学：必须掌握 vs 概念理解 vs 实际常用 + Stage 0 | 第 1 节 |
| [02-whole-body-control.md](02-whole-body-control.md) | WBC 全谱系：OSC/WBIK/WBID/分层 QP + Stage 2 | 第 2 节 |
| [03-locomotion-rl.md](03-locomotion-rl.md) | 经典 vs 学习式运动控制 + RL 最短路径 + Stage 1 | 第 3、4 节 |
| [04-isaac-lab.md](04-isaac-lab.md) | Isaac Sim/Lab 概念地图 + 代码入口 | 第 5 节 |
| [05-retargeting-teleop.md](05-retargeting-teleop.md) | 运动重定向 / 全身跟踪系统对比 + Stage 3/4 | 第 6、10 节 |
| [06-loco-manipulation.md](06-loco-manipulation.md) | loco-manipulation 系统架构 + 任务设计 + Stage 5 | 第 7、8 节 |
| [07-vla-humanoid.md](07-vla-humanoid.md) | VLA/VLM × humanoid 三条路线对比 + Stage 6 | 第 9 节 |
| [08-papers.md](08-papers.md) | 全部论文总表（含 Why Read） | Paper 部分 |
| [09-repos.md](09-repos.md) | 全部仓库总表（维护状态/硬件要求/代码入口） | Repository 部分 |

## 六阶段总览

```
Stage 0  Prerequisites（运动学/动力学/Python/环境）          ≈ 1.5 周
Stage 1  Humanoid Locomotion（Isaac Lab 跑通 G1/H1）        ≈ 2 周
Stage 2  Whole-Body Control（目标→关节命令）                ≈ 2 周
Stage 3  Motion Retargeting（人→机器人动作映射）            ≈ 1.5 周
Stage 4  Learned WBC（读懂/修改 OmniH2O/HOVER/SONIC 系）    ≈ 2 周
Stage 5  Loco-Manipulation（走→抓→搬，全身协同）            ≈ 2 周
Stage 6  Vision / VLA（感知/语言→任务→WBC）                ≈ 1 周
```

每个 Stage 的文件内部都含：核心概念 / 必读论文 / 教程 / repo / 代码入口 / 实践项目 / 自测 checklist / 可跳过清单。

## 软件工程栈（第 11 节：实际 humanoid research 的重要性分级）

### 🔴 必须熟练（日常主力）

| 技术 | 用法 |
|---|---|
| **Python** | 一切：训练脚本、环境、数据分析。要达到"写 200 行无 bug 脚本"的水平 |
| **PyTorch** | 读 policy 代码、改网络结构、写 reward 计算（张量思维）。不用会训练大模型 |
| **Linux** | 日常环境（ssh/GPU 机器/包管理）。会用 conda、systemd/nohup 跑长任务 |
| **Isaac Lab** | 你的训练主框架（见 04 篇） |
| **MuJoCo** | 轻量仿真/调试/复现论文（很多论文给 mujoco 版） |

### 🟡 能看懂（不精写）

| 技术 | 需要程度 |
|---|---|
| **C++** | 读 Pinocchio/rsl_rl 源码、跑别人 C++ 工程时能改小地方即可 |
| **CUDA** | 能看懂 `@torch.jit` 脚本与常见 kernel 写法即可（rsl_rl 用 CUDA graph） |
| **ROS2** | 真机部署时用（Unitree 官方 ROS2 包）；仿真阶段用不上 |
| **Eigen** | 读 C++ 控制代码时认识类型即可 |
| **Docker** | 会用 Dockerfile 搭训练环境（避免环境地狱） |

### ⚪ 暂时不用投入

| 技术 | 说明 |
|---|---|
| **实时控制（RT 线程/共享内存/EtherCAT）** | 只有做真机低层控制才需要；G1 官方 SDK 已封装 |
| **仿真器引擎开发** | 不需要 |
| **模型优化/量化** | 不需要 |

## 📅 12 周学习计划（每周 15–20 小时，70–80% 代码）

| 周 | 主题 | 主要产出（每周末必须有的东西） |
|---|---|---|
| **W1** | 运动学/动力学（SE(3)、FK/IK、Jacobian、EoM）| Pinocchio 加载 G1，FK/Jacobian/ID 流水线跑通 |
| **W2** | 接触动力学 + 质心动力学 + ZMP；Isaac Lab 安装与环境入门 | 能解释接触摩擦锥 + Isaac Lab 跑通 demo |
| **W3** | Isaac Lab 内置 humanoid（G1/H1）训练跑通 + PPO/GAE 理论 | **第一个训练收敛的 locomotion policy** |
| **W4** | WBC 理论：OSC/Sentis/Saab/TSID/Herzog；跑 TSID 例子 | 能讲清分层 QP 的机制 |
| **W5** | 手写分层 QP-WBC（Pinocchio + proxsuite），MuJoCo 里让 G1 站住抬手 | **自己写的 QP-WBC 让 G1 平衡+抬手** |
| **W6** | reward 工程：逐项删 reward 重训观察；地形课程；domain randomization | 对 reward 每项有"直觉→行为"的对应经验 |
| **W7** | 学习式 WBC 论文精读（Expressive WBC / Deep WBC / ASAP）+ 复现 | 能说出这些系统 observation/action/reward 设计 |
| **W8** | Motion retargeting：SMPL→G1 工具链 + 动捕/视频数据 | **人形动作重定向 pipeline 跑通（视频→G1 动画）** |
| **W9** | 全身跟踪策略：OmniH2O/HOVER 系论文精读 + 复现（或等价项目） | 理解 reference motion 进 RL 的完整流程 |
| **W10** | Loco-manipulation 环境搭建：G1 拿物体行走任务 | **training G1 边走路边保持手臂目标（sim）** |
| **W11** | 任务升级：reach→grasp→carry / 开门；真机数据采集方案调研（VR/动捕） | 完整 walk→grasp→carry 任务在 sim 里跑通 |
| **W12** | 综合项目 + 答辩：写清系统架构（policy 栈：高层任务→低层 WBC）；补 VLA 概念 | **小型 humanoid loco-manipulation 项目（sim）** |

> 每周节奏：前 3 天概念+读代码（4–6h），后 4 天写代码跑实验（10–14h）。每个 milestone 都要"跑出来"才算过。

## ⚡ 4 周极速版（砍什么）

> 前提：已有 Python/PyTorch 基础。砍掉一切"经典"深度（WBC 手写 QP、MPC、HZD 全删）。

| 周 | 只做这些 |
|---|---|
| **W1** | 快速过 SE(3)/FK/Jacobian（Modern Robotics 3–5 章，不刷题）+ Isaac Lab 安装 + 跑通内置 humanoid demo |
| **W2** | 训练第一个 G1 policy（rsl_rl/Isaac Lab），同时读 Rudin 2022 reward 模板 + PPO 核心（Spinning Up） |
| **W3** | Expressive WBC 或 Humanoid-Gym 复现（改 reward 训练）；读 OmniH2O/HOVER 论文理解"reference motion + RL" |
| **W4** | 小项目：G1 边行走边保持末端目标（在现成环境上加 EE reward）；输出一篇 2 页技术总结 |

**砍掉**：手写 QP-WBC（W5）→ 用 TSID 库理解概念即可；MPC 步态细节；状态估计实现；C++/ROS2；WBIK 手写；所有"经典"论文细读；VLA 实操（只读 GR00T/π0 架构图）。

**4 周版的学习本质**：直接站在 2024–2026 的代码肩膀上（Isaac Lab + rsl_rl + 开源 humanoid 环境），把"改 reward 训练人形"练成肌肉记忆。

## 学习纪律

1. **每个 Stage 以"跑出来的东西"为验收**，不以"读完"为验收
2. **论文只精读有代码/有真机的**；经典论文读摘要+框架图
3. **每周末 30 分钟写周报**（做了什么/卡在哪/下一步），这就是你的研究日志
4. 卡住 1 小时以上 → 先查官方文档/issue，再问社区（Unitree 有官方技术交流）
5. 所有训练实验记录超参与 seed（实验管理从第一天开始）

## 更新记录

- v1.0（2026-08）：初版，基于 2026 年 8 月可核实的公开资源
