# 09 · 仓库总表（Repositories）

> 全部经 2026-08 实测核实（GitHub API/页面）。⚠️ 维护状态随时会变，用前再看一眼 last commit。

## 9.1 训练框架与环境

| Repo | 官方/第三方 | 维护状态 | Sim 框架 | 支持机器人 | 训练硬件 | Checkpoint | 复现难度 | 推荐阅读入口 |
|---|---|---|---|---|---|---|---|---|
| [rsl_rl](https://github.com/leggedrobotics/rsl_rl) | 官方（ETH RSL） | ✅ v5.4.2 (2026-07) | Isaac Lab / 任意 Gym | 通用（G1/H1 常用） | NVIDIA GPU（24GB 推荐） | 无（训练用） | 低 | `rsl_rl/rl/ppo.py`（核心算法） |
| [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) | 官方（NVIDIA） | ✅ v2.3.2 稳定 / v3.0 beta | PhysX（Isaac Sim 内置） | G1/H1/通用 | RTX 4090 起步 | 无 | 中（版本匹配坑多） | `source/isaaclab_tasks/.../velocity/config/g1/flat_env_cfg.py` |
| [mujoco_playground](https://github.com/google-deepmind/mujoco_playground) | 官方（DeepMind） | ✅ 活跃 | MuJoCo | G1/H1 等 | CPU 可跑，GPU 更好 | 有 | **低（首选快速迭代）** | `_src/locomotion/g1/` 的 joystick 任务 |
| [skrl](https://github.com/skrl-project/skrl) | 第三方 | ✅ v2.1.0 | Isaac Lab / Gymnasium | 通用 | NVIDIA GPU | 无 | 中 | `skrl/agents/ppo/` |
| [rl_games](https://github.com/Denys88/rl_games) | 第三方 | 🟡 v1.6.5 (2026-02)，传统路线 | Isaac Gym/Lab | 通用 | NVIDIA GPU | 部分 | 中 | 新项目不推荐 |
| [legged_gym](https://github.com/leggedrobotics/legged_gym) | 官方（ETH RSL） | ⚠️ 停滞（2025-05），依赖废弃 Isaac Gym | Isaac Gym（已废弃） | 四足为主 | NVIDIA GPU | 有 | — | **只读代码学习，别用于新项目** |
| [Humanoid-Gym](https://github.com/roboterax/humanoid-gym) | 第三方 | ⚠️ 停滞，仅 XBot | Isaac Gym（废弃） | XBot-S/L | NVIDIA GPU | 有 | — | 学习用 |

## 9.2 机器人资产与 SDK

| Repo | 说明 | 状态 |
|---|---|---|
| [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) | Unitree 官方 RL 训练（Go2/G1/H1/H1_2），sim→真机官方通道 | ✅ 2025-07 仍在推送 |
| [unitree_ros](https://github.com/unitreerobotics/unitree_ros) | **URDF 在这里**：`robots/h1_description/urdf/h1.urdf`、`robots/g1_description/g1_29dof.urdf`（unitree_ros2 只有 SDK 消息，无模型） | ✅ |
| [mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie) | 官方模型库，含 `unitree_g1` / `unitree_h1` | ✅ |

## 9.3 全身跟踪 / 重定向 / 遥操作系统

| Repo | 系统 | 维护 | 说明 |
|---|---|---|---|
| [NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl) | SONIC + GEAR | ✅✅ 3398★, 2026-08 极活跃 | **2026 全身控制主线**，VLA→WBC 落地范本 |
| [LeCAR-Lab/ASAP](https://github.com/LeCAR-Lab/ASAP) | ASAP | ✅✅ 2097★, 2026-01 | sim2real 延迟对齐，G1 |
| [HybridRobotics/whole_body_tracking](https://github.com/HybridRobotics/whole_body_tracking) | BeyondMimic | ✅ 2330★, 2025-10 | 扩散全身控制，G1 |
| [NVlabs/HOVER](https://github.com/NVlabs/HOVER) | HOVER | ✅ 756★, 2025-07 | 多模式全身速度跟踪，H1/H2 |
| [LeCAR-Lab/human2humanoid](https://github.com/LeCAR-Lab/human2humanoid) | OmniH2O | 🟡 1058★, 2025-02 | 全身遥操作/学习，H1 |
| [MarkFzp/humanplus](https://github.com/MarkFzp/humanplus) | HumanPlus | ⚠️ 850★, 停更 | 影子跟随+模仿 |
| [edpsw/exbody2](https://github.com/edpsw/exbody2) | ExBody2 | 🟡 67★, 2025-06 | 真机 G1 全身跟踪 |
| [chengxuxin/expressive-humanoid](https://github.com/chengxuxin/expressive-humanoid) | ExBody | ⚠️ 498★ | 仅仿真（被 ExBody2 替代） |
| [xbpeng/MimicKit](https://github.com/xbpeng/MimicKit) | AMP/ASE | ✅✅ 2242★, 2026-06 | 对抗模仿学习基准 |
| [ZhengyiLuo/PHC](https://github.com/ZhengyiLuo/PHC) | PHC | 🟡 1279★, 2025-08 | SMPL 全身跟踪（仿真） |
| [zhangxuelei86/Deep-Whole-Body-Control](https://github.com/zhangxuelei86/Deep-Whole-Body-Control) | DWBC | ⚠️ 停更 | 必读论文的参考实现 |
| [OpenTeleVision/TeleVision](https://github.com/OpenTeleVision/TeleVision) | Open-TeleVision | ⚠️ 1300★, 停更 | VR 遥操作 G1/H1 |
| [j96w/DexCap](https://github.com/j96w/DexCap) | DexCap | ⚠️ 停更 | 手部动捕采集 |
| [MarkFzp/mobile-aloha](https://github.com/MarkFzp/mobile-aloha) | Mobile ALOHA | ⚠️ 4464★, 停更 | 移动双臂采集（非人形） |
| [YanjieZe/GMR](https://github.com/YanjieZe/GMR) | GMR | ✅ 2617★, ICRA 2026 | **CPU 实时重定向，首选** |
| [XinLang2019/Humanoid-Motion-Retargeting](https://github.com/XinLang2019/Humanoid-Motion-Retargeting) | HMR | 🟡 129★ | 经典重定向实现 |
| [edpsw/amass_g1_retargeting](https://github.com/edpsw/amass_g1_retargeting) | AMASS→G1 | 🟡 30★ | AMASS 数据→G1，社区常用 |
| [Renforce-Dynamics/trackerLab](https://github.com/Renforce-Dynamics/trackerLab) | trackerLab | ✅ 244★, 2025-11 | 人形运动跟踪工具箱 |

## 9.4 VLA / 基础模型

| Repo | 说明 | 状态 |
|---|---|---|
| [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | GR00T 生态（数据管线+模型） | ✅ 活跃 |
| [OpenDriveLab/WholebodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) | WholeBodyVLA（统一 latent VLA） | ✅ 活跃 |
| [liruiw/HPT](https://github.com/liruiw/HPT) | HPT（跨本体预训练骨干） | ✅ |
| HF `nvidia/GR00T-N1-2B` / `nvidia/GR00T-N1.5-3B` / `nvidia/GEAR-SONIC` | 官方权重 | ✅ 已确认存在 |

## 9.5 动力学/控制库（WBC 实现）

| 库 | 说明 | 状态 |
|---|---|---|
| [Pinocchio](https://github.com/stack-of-tasks/pinocchio)（[文档](https://stack-of-tasks.github.io/pinocchio/)） | FK/IK/动力学/接触，examples 含 `g1-constraint-simulation.py` | ✅ 活跃 |
| [TSID](https://github.com/stack-of-tasks/tsid) | 分层 QP 全身控制（理论来源：[Del Prete 2015](https://arxiv.org/abs/1410.3863)） | ✅ 活跃 |
| [Crocoddyl](https://github.com/loco-3d/crocoddyl) | 接触最优控制/MPC | ✅ 活跃 |
| [mc_rtc](https://github.com/jrl-umi3218/mc_rtc) | 实时全身控制框架（任务栈） | ✅ 活跃 |
| [OpenSoT](https://github.com/ADVRHumanoids/OpenSoT) | 任务约束优化 | ✅ 活跃 |
| [OCS2](https://github.com/leggedrobotics/ocs2) | 腿足 MPC 工具箱 | ✅ |
| [Drake](https://github.com/RobotLocomotion/drake) | 优化/控制工具箱 | ✅ 活跃 |

## 9.6 2025–26 新热点

| Repo | 说明 |
|---|---|
| [Embodied-States/Genesis](https://github.com/Embodied-States/Genesis) | 生成式物理仿真平台（组织已改名） |
| [LeCAR-Lab/HumanoidVerse](https://github.com/LeCAR-Lab/HumanoidVerse) | 人形开源基准 |
