# 04 · Isaac Sim / Isaac Lab（仿真与训练环境）

> 定位：你的**主战场**。目标不是会用界面，而是能自己改环境、加任务、写 observation/reward。
> 时间预算：贯穿 Week 2–8；本文件是 Week 6 环境搭建的完整指南。
> ⚠️ 本文的"具体代码入口"小节待最新版本核实后填充（见文末更新区）。

## 4.1 概念地图（Isaac 生态的词汇表）

| 概念 | 是什么 | 你需要掌握到什么程度 |
|---|---|---|
| **USD**（Universal Scene Description） | Pixar 的场景描述格式，Isaac 的场景/资产格式 | 能看懂 `.usd` 的层级结构（prim/transform/joint），会用 OmniUSD 或代码查关节名 |
| **Articulation** | 由 link + joint 组成的运动链（G1/H1 就是 articulation） | 知道 `Articulation` API：`num_dofs`、`get_joint_names`、`set_joint_position_targets` |
| **Actuator** | 关节的执行器（位置/速度/力矩模式 + 增益） | 理解 `ImplicitActuatorCfg` 的 `stiffness`/`damping`（=PD 增益），这是 sim 里 PD 的实现 |
| **PD controller** | τ = kp(q_des−q) − kd·q̇ | 必须知道 policy 输出与 PD 增益的配合（见 03 篇） |
| **Contact / Collision** | PhysX 的碰撞体 + 接触求解 | 会查接触力（`ContactSensorCfg`）、会调摩擦系数（`physx_material`） |
| **PhysX** | NVIDIA 物理引擎（Isaac 底层） | 知道仿真步长（dt）、解算器迭代数影响接触稳定性即可 |
| **Sensors** | 相机（RGB/深度）、IMU、接触力 | 会配置 `CameraCfg`/`ImuCfg`/`ContactSensorCfg` 并读数据 |
| **Vectorized simulation** | 同一场景 N 个机器人并行仿真（GPU） | 理解"环境数 × 单环境"的批处理思维：所有 API 都是 (N, D) 张量 |
| **ManagerBasedRLEnv** | 组件化环境（ObservationManager/RewardManager/TerminationManager/CurriculumManager 各自配置） | 初学者首选：改 reward 只需改 yaml/class 配置 |
| **DirectRLEnv** | 全手写环境（reset/observation/reward 全在 class 里） | 想深改/新任务时用；代码更透明 |

## 4.2 学习路线（Isaac 部分）

```
Week 6:
  D1    装 Isaac Lab（官方文档安装指南）+ 跑通自带 demo
  D2    理解 Articulation：加载 G1/H1，用代码读关节名/状态，施加关节目标（官方 tutorial: articulation）
  D3    读一个 DirectRLEnv humanoid 环境的源码：reset/step/observation/reward 全流程
  D4    跑通内置 humanoid velocity 训练（GPU，看 tensorboard 曲线收敛）
  D5    改 reward：加一个"躯干直立"惩罚项，重训对比
  D6    加相机/接触传感器，把感知量加进 observation
  D7    写一个"随机扰动"的 domain randomization 配置，验证鲁棒性变化
```

## 4.3 常见坑（社区高频问题）

1. **版本对应**：Isaac Lab 与 Isaac Sim 版本必须匹配（安装指南里有对应表）；2025+ 版本注意是否已内置 Sim
2. **GPU 依赖**：rsl_rl 训练必须 NVIDIA GPU；RTX 4090 可训 G1 简单任务，更大的 batch 需要 A100/H100
3. **PD 增益移植**：真机 G1 的 PD 增益（官方提供）≠ sim 默认值，sim-to-real 差 10% 就崩
4. **接触抖动**：调 `dt`（1/400s 常见）和解算器迭代；摩擦系数用官方实测值
5. **命令分布**：velocity command 的训练分布要覆盖真机使用范围，否则 sim 里好、真机不会走
6. **reset 姿势**：人形 reset 到站立姿势要小心（重心在脚掌内），否则训练初期大量早死

## 4.4 具体代码入口（2026-08 已实测核实）

### Isaac Lab 安装与版本

- **稳定版 v2.3.2**（2026-02）；beta **v3.0.0-beta2**（2026-07）。文档：[isaac-sim.github.io/IsaacLab/](https://isaac-sim.github.io/IsaacLab/)
- **Isaac Sim 已改为 pip 依赖，无需独立安装**：Isaac Lab 2.3.x → `isaacsim==5.1.0`；3.0 beta → `isaacsim==6.0.1.0`
- 训练硬件（官方）：Isaac Sim 4.5 最低 RTX 3070/8GB，推荐 4080/16GB；Isaac Sim 6.0 最低升到 RTX 4080/16GB。官方基准用 **RTX 4090 / L40**。实践建议 **24GB（4090）起步**，16GB 需减少并行环境数，8GB 只够小规模验证

### 人形 locomotion 任务（G1/H1）—— 正确路径 ⚠️

> 网上流传的 `humanoid_velocity.py` **不存在**（实测 404）。正确位置：

```
source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/velocity/config/
  ├── g1/flat_env_cfg.py、rough_env_cfg.py
  └── h1/flat_env_cfg.py、rough_env_cfg.py
任务名（CLI 里用）：Isaac-Velocity-Flat-G1-v0 / Isaac-Velocity-Rough-G1-v0
                    Isaac-Velocity-Flat-H1-v0 / Isaac-Velocity-Rough-H1-v0
```

- 通用 DirectRLEnv 人形示例：`direct/humanoid/humanoid_env.py`（任务 `Isaac-Humanoid-Direct-v0`）
- **资产**：`isaaclab_assets/isaaclab_assets/robots/unitree.py` 中的 `H1_CFG` / `G1_CFG` / `G1_29DOF_CFG`（`ArticulationCfg` 对象）
- Direct vs Manager 的官方说明页：Task Design Workflows（`task_workflows.html`）
- **Curriculum** 官方页：how-to/curriculums；**domain randomization** 无独立页——用 Event Manager 实现，示例就在上面 `flat_env_cfg.py`/`rough_env_cfg.py` 的 `randomize_rigid_body_*` 与 `push_robot` 事件里

### 人形 manipulation / loco-manipulation 任务

```
source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/locomanipulation/pick_place/
  └── locomanipulation_g1_env_cfg.py   → 任务 Isaac-PickPlace-Locomanipulation-G1-Abs-v0
另有 isaaclab_mimic 的 locomanipulation_g1（动作模仿示例）
```

### 训练框架状态（2026-08 实测）

| 框架 | 状态 | 说明 |
|---|---|---|
| **rsl_rl**（[GitHub](https://github.com/leggedrobotics/rsl_rl)） | ✅ 活跃（v5.4.2, 2026-07） | Isaac Lab 官方三框架之一，人形 locomotion 主力 |
| **skrl**（[GitHub](https://github.com/skrl-project/skrl)） | ✅ 活跃（v2.1.0） | 支持 Isaac Lab + Gymnasium |
| **rl_games**（[GitHub](https://github.com/Denys88/rl_games)） | 🟡 未停更（v1.6.5, 2026-02）但属传统路线 | 新项目不推荐 |
| **legged_gym**（[GitHub](https://github.com/leggedrobotics/legged_gym)） | ⚠️ 停滞（最后提交 2025-05），依赖已废弃的 Isaac Gym | 只读代码学习 |
| **Isaac Gym（旧版）** | ❌ 官方声明 "Now Deprecated" | 一律迁移 Isaac Lab |
| **humanoid-gym**（[GitHub](https://github.com/roboterax/humanoid-gym)） | ⚠️ 停滞，仅 XBot-S/L 资产 | 学习用，不用于 G1/H1 |

### 机器人资产与官方仓库

- **unitree_rl_gym**（[GitHub](https://github.com/unitreerobotics/unitree_rl_gym)）：官方，支持 Go2/G1/H1/H1_2（2025-07 仍在推送），sim + 真机 RL 的官方入口
- **URDF 位置**：`unitree_ros2` 只有 SDK 消息包（无 URDF）；模型在 ROS1 仓库 [unitree_ros](https://github.com/unitreerobotics/unitree_ros) 的 `robots/h1_description/urdf/h1.urdf`、`robots/g1_description/g1_29dof.urdf`
- **mujoco_menagerie**（[GitHub](https://github.com/google-deepmind/mujoco_menagerie)）：含 `unitree_g1` / `unitree_h1` 模型（Pinocchio 练习直接用它）
- **mujoco_playground**（[GitHub](https://github.com/google-deepmind/mujoco_playground)）：活跃；G1/H1 任务在 `_src/locomotion/{g1,h1}/`，注册任务 `G1JoystickFlatTerrain` / `G1JoystickRoughTerrain` / `H1JoystickGaitTracking` / `H1InplaceGaitTracking` —— **想要轻量、快速迭代的训练环境，优先 mujoco_playground**
- **mc_rtc**（[GitHub](https://github.com/jrl-umi3218/mc_rtc)）与 **OpenSoT**（[GitHub](https://github.com/ADVRHumanoids/OpenSoT)）：均活跃，真机 WBC 框架
- **Pinocchio**：文档 [stack-of-tasks.github.io/pinocchio](https://stack-of-tasks.github.io/pinocchio/)，`examples/` 里还有 `g1-constraint-simulation.py`（G1 约束仿真示例，直接可跑）

### 2025–2026 新增热点 repo（已核实存在）

- **Genesis**：生成式物理仿真平台（组织名已改 Embodied-States）：[GitHub](https://github.com/Embodied-States/Genesis)
- **HumanoidVerse**（LeCAR-Lab，清华/LeCAR）：人形机器人开源基准：[GitHub](https://github.com/LeCAR-Lab/HumanoidVerse)
- **ASAP**（LeCAR-Lab）：sim-to-real 对齐框架：[GitHub](https://github.com/LeCAR-Lab/ASAP)

