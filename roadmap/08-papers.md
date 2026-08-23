# 08 · 论文总表（Papers）

> 全部条目经核实（arXiv/DOI/官方页面），**优先 2023–2026、有代码、有真机、G1/H1 可复现**。按主题分组；每条附"为什么读"。
> 完整年代线（1972–2025 经典+前沿）见仓库根的 [papers.md](../papers.md)。

## 8.1 综述（先读地图）

| Paper | Year | Problem | Method | Controller | RL? | Real Robot? | Code | Why Read |
|---|---|---|---|---|---|---|---|---|
| [Humanoid Locomotion and Manipulation: Current Progress and Challenges](https://arxiv.org/abs/2501.02116) | 2025 | loco-manip 全景 | 控制/规划/学习三路线综述 | — | — | — | 无 | 你的 roadmap 地图 |
| [Learning-based Legged Locomotion SOTA](https://arxiv.org/abs/2406.01152) | 2024 | 学习式腿足控制 | 全面综述 | — | — | — | 无 | 补历史脉络 |
| [MPC of Legged and Humanoid Robots](https://doi.org/10.1080/01691864.2023.2168134) | 2023 | 腿足 MPC | 模型+算法综述 | MPC | — | — | 无 | 经典路线速览 |
| [WBC: Past, Present, Future（Del Prete）](https://inria.hal.science/hal-02456663v1) | 2022 | WBC 发展 | 权威综述 | WBC | — | — | 无 | 入门第一读 |

## 8.2 经典运动学/动力学/WBC 基础（少量精读）

| Paper | Year | Problem | Method | Controller | RL? | Real Robot? | Code | Why Read |
|---|---|---|---|---|---|---|---|---|
| [Operational Space Formulation (Khatib)](https://doi.org/10.1109/JRA.1987.1087068) | 1987 | 任务空间控制 | OSC | OSC | 否 | 否 | 无 | WBC 理论源头 |
| [3D LIPM (Kajita)](https://doi.org/10.1109/IROS.2001.973365) | 2001 | 步态建模 | LIPM | 规划 | 否 | 是 | 无 | 所有 MPC 步态的模型 |
| [ZMP Preview Control (Kajita)](https://doi.org/10.1109/ROBOT.2003.1241826) | 2003 | 步态跟踪 | 预览控制 | 规划+跟踪 | 否 | 是 | 无 | 经典步态生成标准 |
| [Resolved Momentum Control (Kajita)](https://doi.org/10.1109/IROS.2003.1248880) | 2003 | 全身动量控制 | 动量分解 | WBC | 否 | 是 | 无 | 动量类 WBC 起点 |
| [Centroidal Dynamics (Orin)](https://doi.org/10.1007/s10514-013-9341-4) | 2013 | 质心动力学 | 质心动量矩阵 | — | 否 | — | 无 | 全身控制的物理语言 |
| [TSID (Del Prete)](https://arxiv.org/abs/1410.3863) | 2015 | 分层 QP WBC | 任务空间逆动力学 | WBC | 否 | 是 | [TSID](https://github.com/stack-of-tasks/tsid) | 读代码必读 |
| [Momentum+HID (Herzog)](https://arxiv.org/abs/1410.7284) | 2016 | 平衡+分层 | 动量控制+HID | WBC | 否 | 是 | 无 | 平衡 WBC 代表作 |
| [Atlas System (Kuindersma)](https://doi.org/10.1007/s10514-015-9479-3) | 2016 | 完整系统 | 规划+估计+QP | WBC | 否 | 是（Atlas） | [drake](https://drake.mit.edu/) 相关 | 系统集成范本 |

## 8.3 学习式 Locomotion（2023–2026 主线）

| Paper | Year | Problem | Method | Controller | RL? | Real Robot? | Code | Why Read |
|---|---|---|---|---|---|---|---|---|
| [Hwangbo: Agile Motor Skills](https://arxiv.org/abs/1901.08652) | 2019 | 腿足 RL 起点 | 并行 RL | learned | 是 | 是（四足） | [rsl_rl](https://github.com/leggedrobotics/rsl_rl) | 范式源头 |
| [Lee: Challenging Terrain](https://arxiv.org/abs/2010.11251) | 2020 | 地形泛化 | 教师-学生 | learned | 是 | 是 | [legged_gym](https://github.com/leggedrobotics/legged_gym) | sim2real 配方 |
| [Rudin: Walk in Minutes](https://arxiv.org/abs/2109.11978) | 2022 | 训练提速 | GPU 并行 RL | learned | 是 | 是 | [rsl_rl](https://github.com/leggedrobotics/rsl_rl) | **reward 模板来源** |
| [Siekmann: Memory-based Cassie](https://arxiv.org/abs/2006.02402) | 2020 | 双足 RL | RNN 记忆 | learned | 是 | 是（Cassie） | 无 | 双足 vs 四足差异 |
| [Radosavovic: Real-World Humanoid](https://arxiv.org/abs/2303.03381) | 2024 | 真机直训 | RL | learned | 是 | 是（Digit） | 无 | 真机人形 RL 代表 |
| [Haarnoja: Agile Soccer](https://arxiv.org/abs/2304.13653) | 2024 | 双足敏捷 | RL | learned | 是 | 是（双足） | 无 | 双足技能上限 |
| [Next Token Prediction](https://arxiv.org/abs/2402.19469) | 2024 | 运动即语言 | 自回归 token | learned | 是 | 是（Digit） | 无 | 新范式启发 |
| [Expressive WBC (H1)](https://arxiv.org/abs/2402.16796) | 2024 | 全身表达 | 运动先验+RL | learned | 是 | 是（H1） | [humanoid-bench](https://github.com/chengxuxin/humanoid-bench) | **H1 全身运动范本** |
| [Agile But Safe](https://arxiv.org/abs/2401.17583) | 2024 | 高速+安全 | 安全滤波器 | learned | 是 | 是（四足） | [agile-but-safe](https://github.com/LeCAR-Lab/agile-but-safe) | 安全约束思路 |
| [Li: Versatile Bipedal IJRR](https://arxiv.org/abs/2401.16889) | 2024 | 双足多样技能 | 双历史输入 | learned | 是 | 是（Cassie） | 无 | 技能覆盖广 |

## 8.3b 2023–2026 补充核实表（含重要勘误，2026-08 核验）

> ⚠️ 社区流传的以下工作**经多方检索不存在**：FLEX: Full-Body Grasping for Humanoid Teleoperation（arXiv 2409.14800 是 WMT 机器翻译）、Sieve（2406.03781 是量子物理）、Bolt: Fast and Agile Bipedal Locomotion（2506.16375 是天体物理；"Bolt" 实为镜识科技 2026 全尺寸人形硬件）。相关可核实工作：ODRI 点足双足 Bolt 的 [MPC 版](https://arxiv.org/abs/2412.01713) 与 [约束 RL 版](https://arxiv.org/abs/2508.02194)（[BoltLocomotion](https://gepetto.github.io/BoltLocomotion/)）。
> 另有同名合并："Learning Humanoid Locomotion with Transformers" 是 [2303.03381](https://arxiv.org/abs/2303.03381) v1 原名，后更名 Real-World Humanoid Locomotion with RL（Digit，非 2025/H1/G1）。

| Paper | Year | Problem | Method | Controller | RL? | Real Robot? | Code | Why Read |
|---|---|---|---|---|---|---|---|---|
| [H2O](https://arxiv.org/abs/2403.04436) | 2024 IROS | 实时全身遥操作 | 动捕→retarget→RL 跟踪 | learned+PD | 是 | H1 | [human2humanoid](https://github.com/LeCAR-Lab/human2humanoid) | H1 遥操作数据管线 |
| [PhysHSI](https://arxiv.org/abs/2510.11072) | 2025 | 真实场景全身交互 | 统一全身 RL+课程/域随机化 | learned+PD | 是 | G1 | [InternRobotics/PhysHSI](https://github.com/InternRobotics/PhysHSI) | G1 六任务交互开源 |
| [HumanUP (Getting-Up)](https://arxiv.org/abs/2502.12152) | 2025 RSS | 躺姿起身 | RL+参考引导+课程 | learned+PD | 是 | G1 | [RunpeiDong/humanup](https://github.com/RunpeiDong/humanup) | G1 起身技能开源 |
| [AGILE / WBC-AGILE](https://arxiv.org/abs/2603.20147) | 2026 | loco-manip 学习引擎 | Isaac Lab 全身 RL 工作流 | learned+PD | 是 | G1 (+T1) | [nvidia-isaac/WBC-AGILE](https://github.com/nvidia-isaac/WBC-AGILE) | NVIDIA 官方人形工作流 |

**平台纠正**：Humanoid-Gym 官方验证平台是 RobotEra **XBot-S/L**（非 G1/H1）；H2O/OmniH2O 是 **H1**；Agile But Safe（ABS）是四足 **Go1**。

**G1/H1 代码可复现性排序（易→难）**：
1. **humanoid-gym**（文档最全、依赖最轻，社区广泛移植 G1，起步首选）
2. **LeCAR-Lab/ASAP**（G1 官方、README 分步完整，但需真机数据校正）
3. **PhysHSI / humanup**（legged_gym/rsl_rl 栈、G1 单机任务，clone 即训）
4. **exbody2 / expressive-humanoid**（需 AMASS 动捕 + 重定向管线，依赖重）
5. **WBC-AGILE**（功能最全但要求 Isaac Lab 3.0/Isaac Sim 6.0 最新环境）

## 8.4 全身跟踪 / 数据→技能（Stage 3–4 核心）

| Paper | Year | Problem | Method | Controller | RL? | Real Robot? | Code | Why Read |
|---|---|---|---|---|---|---|---|---|
| [AMP](https://arxiv.org/abs/2104.02180) | 2021 | 风格化运动 | 对抗先验 | learned | 是 | 否 | [MimicKit](https://github.com/xbpeng/MimicKit) | 对抗模仿奠基 |
| [ASE](https://arxiv.org/abs/2205.01906) | 2021 | 技能嵌入 | 对抗+潜空间 | learned | 是 | 否 | MimicKit | 技能库思想 |
| [PHC](https://arxiv.org/abs/2305.06456) | 2023 | SMPL 全身跟踪 | RL+动捕 | learned | 是 | 否 | [PHC](https://github.com/ZhengyiLuo/PHC) | 人形角色跟踪 |
| [DWBC](https://arxiv.org/abs/2210.10044) | 2022 | 统一操作+运动 | 单策略 | learned | 是 | 否 | [DWBC](https://github.com/zhangxuelei86/Deep-Whole-Body-Control) | 统一策略原型 |
| [OmniH2O](https://arxiv.org/abs/2406.08858) | 2024 | 全身遥操作 | 视频→全身策略 | learned | 是 | 是（H1） | [human2humanoid](https://github.com/LeCAR-Lab/human2humanoid) | **数据飞轮范式** |
| [HumanPlus](https://arxiv.org/abs/2406.10454) | 2024 | 影子跟随 | 模仿+RL | learned | 部分 | 是（H1） | [humanplus](https://github.com/MarkFzp/humanplus) | 单目数据采集 |
| [HOVER](https://arxiv.org/abs/2410.21229) | 2024 | 多模式全身控制 | 速度跟踪 | learned | 是 | 是（H1/H2） | [HOVER](https://github.com/NVlabs/HOVER) | **全身跟踪必读** |
| [ExBody2](https://arxiv.org/abs/2412.13196) | 2025 | 解耦全身跟踪 | 速度+地标解耦 | learned | 是 | 是（G1） | [exbody2](https://github.com/edpsw/exbody2) | G1 真机范本 |
| [BeyondMimic](https://arxiv.org/abs/2508.08241) | 2025 | 扩散全身控制 | 引导扩散 | learned | 否 | 是（G1） | [whole_body_tracking](https://github.com/HybridRobotics/whole_body_tracking) | 扩散路线代表 |
| [SONIC](https://arxiv.org/abs/2511.07820) | 2025 | 全身速度控制 | GR00T 线 | learned | 是 | 是（G1） | [GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl) | **2026 主线** |
| [ASAP](https://arxiv.org/abs/2502.01143) | 2025 | sim2real 对齐 | 延迟动力学对齐 | learned | 是 | 是（G1） | [ASAP](https://github.com/LeCAR-Lab/ASAP) | **sim2real 必读** |

## 8.5 VLA × Humanoid（Stage 6）

| Paper | Year | Problem | Method | Controller | RL? | Real Robot? | Code | Why Read |
|---|---|---|---|---|---|---|---|---|
| [π0](https://arxiv.org/abs/2410.24164) | 2024 | 通用 VLA | flow matching | latent→policy | 部分 | 是 | 🟡 权重状态未核实 | VLA 路线 C 源头 |
| [HPT](https://arxiv.org/abs/2409.20537) | 2024 | 跨本体骨干 | 预训练 transformer | 表征 | — | 否 | [HPT](https://github.com/liruiw/HPT) | latent 表征 |
| [GR00T N1](https://arxiv.org/abs/2503.14734) | 2025 | 开源人形 VLA | 双系统 | joint | 是 | 是（GR-1） | [Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) + HF 权重 | 路线 A 代表 |
| [Gemini Robotics](https://arxiv.org/abs/2503.20020) | 2025 | 通用 VLA+推理 | Gemini 2.0 | EE/joint | — | 是 | 无 | 大厂路线参考 |
| [WholeBodyVLA](https://arxiv.org/abs/2512.11047) | 2025 | 统一 latent 全身 | latent 动作空间 | latent→policy | 是 | 未核实 | [WholebodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) | **路线 C 代表（研究热点）** |
| [LeVERB](https://arxiv.org/abs/2506.13751) | 2025 | latent 指令全身 | latent VLM 指令 | latent→WBC | 是 | 是 | 未核实 | 语义-运动解耦 |
| [GR00T N1.5](https://research.nvidia.com/labs/gear/gr00t-n1_5/) | 2025 | VLA+WBC 标准形态 | 关节速度→Decoupled WBC | WBC | 是 | 是 | HF 权重 | **工程主流形态**（无论文，官方页） |
| [Helix (Figure)](https://www.figure.ai/news/helix) | 2025 | 高频全身 VLA | 双系统 200Hz | joint | 是 | 是（02/03） | 无 | 路线 A/B 工程化 |
| [1X World Model](https://www.1x.tech/discover/1x-world-model) | 2024 | 世界模型仿真 | 视频 WM | — | — | NEO 数据 | 无 | 合成数据思路 |

> ⚠️ **FLEX 澄清**：流传的 "FLEX: Full-Body Grasping"（arXiv 2409.14800）是无关论文；同名 "FLEX"（arXiv 2211.11903, CVPR 2023）是**虚拟人抓取合成**（avatar 动画），非机器人工作，本表不收录。

## 8.6 阅读优先级建议（时间有限先读这些）

1. **综述**：Humanoid Loco-Manipulation survey（2501.02116）+ WBC survey（HAL）
2. **RL 配方**：Rudin 2022 → Lee 2020 → ASAP 2025
3. **全身跟踪**：HOVER → ExBody2 → SONIC
4. **系统**：GR00T N1（架构图即可）→ GR00T-WholeBodyControl 代码
5. **数据**：OmniH2O → HumanPlus
