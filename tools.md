# 🛠 开源工具与仿真器 (Tools & Simulators)

## 仿真器与训练环境

- **MuJoCo** — DeepMind 开源物理引擎（免费），人形机器人仿真的事实标准之一。 [mujoco.org](https://mujoco.org/)
- **MuJoCo Menagerie** — 官方机器人模型库（含人形机器人模型）。 [GitHub](https://github.com/google-deepmind/mujoco_menagerie)
- **MuJoCo Playground** — 基于 MuJoCo 的足式/人形 RL 训练环境（H1、G1 等任务）。 [playground.mujoco.org](https://playground.mujoco.org/)
- **Isaac Lab** — NVIDIA 开源 RL 仿真框架（基于 Isaac Sim），含人形机器人任务。 [isaac-sim.github.io/IsaacLab](https://isaac-sim.github.io/IsaacLab/)
- **Genesis** — 生成式物理仿真平台（可微分仿真、生成式数据）。 [GitHub](https://github.com/Genesis-Embodied-AI/Genesis)
- **Drake** — MIT（Tedrake）开源机器人仿真/优化工具箱，人形机器人研究常用。 [drake.mit.edu](https://drake.mit.edu/)

## 动力学与控制库（WBC 实现）

- **Pinocchio** — 刚性多体动力学库（ABA/CRBA 等），全身控制与最优控制的标准底层库。 [GitHub](https://github.com/stack-of-tasks/pinocchio)
- **TSID (Task Space Inverse Dynamics)** — 任务空间逆动力学，优先级全身控制实现。 [GitHub](https://github.com/stack-of-tasks/tsid)
- **Crocoddyl** — 接触约束下的最优控制/MPC 求解库。 [GitHub](https://github.com/loco-3d/crocoddyl)
- **OCS2** — 足式机器人 MPC/最优控制工具箱（ETH RSL）。 [GitHub](https://github.com/leggedrobotics/ocs2)

## 强化学习训练框架（腿足/人形）

- **rsl_rl / rl_gpu** — ETH RSL 的 GPU 并行 RL 训练框架（isaac 系任务常用）。 [GitHub](https://github.com/leggedrobotics/rsl_rl)
- **legged_gym** — ETH RSL 腿足机器人 RL 训练环境。 [GitHub](https://github.com/leggedrobotics/legged_gym)
- **Humanoid-Gym** — 人形机器人 RL 训练 + 零样本 sim2real 迁移。 [GitHub](https://github.com/roboterax/humanoid-gym)

## 动作重定向、跟踪与部署（2026-10-05 增量核验）

- **GMR (General Motion Retargeting)** — 将人体动作实时重定向到多种人形机器人，在 CPU 上运行；可作为动作模仿训练的输入前端。 [官方 GitHub](https://github.com/YanjieZe/GMR)
- **MimicKit** — 动作模仿控制器训练工具，包含 DeepMimic、AMP、ASE 等方法，并提供 GMR 到自身动作格式的转换脚本。 [官方 GitHub](https://github.com/xbpeng/MimicKit)
- **Unitree RL Lab** — 宇树官方 Isaac Lab 训练环境，支持 Go2、H1、G1-29dof；文档包含 MuJoCo 验证和真机部署流程。 [官方 GitHub](https://github.com/unitreerobotics/unitree_rl_lab)

使用顺序可从 GMR 生成参考动作、在 MimicKit 中训练跟踪控制器开始；Unitree RL Lab 提供另一套平台训练与部署入口。不同项目的动作格式、关节顺序和策略接口需要分别适配，不能直接互换权重。

# 🌐 中文资源 (Chinese Resources)

- **DMbot 机器人教程 · 经典人形全身控制（LIPM/DCM + TSID + 动量 WBC）** — 中文推导教程。 [robotics-tutorial.dmbot.cn](http://robotics-tutorial.dmbot.cn/05_%E8%BF%90%E5%8A%A8%E6%8E%A7%E5%88%B6/30_%E5%A4%8D%E5%90%88/220_%E7%BB%8F%E5%85%B8%E4%BA%BA%E5%BD%A2%E5%85%A8%E8%BA%AB%E6%8E%A7%E5%88%B6/)
- **达摩院开发者社区 · 具身智能 Locomotion 教程（学习方法和大纲）** — 中文学习路线。 [damodev.csdn.net](https://damodev.csdn.net/6a6ddeac662f9a54cb96e199.html)
