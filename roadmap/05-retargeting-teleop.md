# 05 · 运动重定向（Motion Retargeting）与全身跟踪（Whole-Body Tracking）（Stage 3–4）

> 定位：**人形数据飞轮的入口**。人的动作（动捕/视频/VR）→ 人形机器人的参考动作 → 全身跟踪 policy。这是 OmniH2O/HumanPlus/SONIC 这类系统的基础设施。
> 时间预算：2 周（Stage 3 ≈ 1.5 周 + Stage 4 ≈ 2 周，部分并行，12 周计划 Week 8–9）。
> ⚠️ 本文系统表待核实版填充（见 5.4）。

## 5.1 概念链（先理解整条流水线）

```
人的动作数据
  ├─ 动捕（MoCap：光学/惯性）→ SMPL 或骨架序列
  ├─ 视频（RGB/单目）→ 2D/3D 姿态估计（如 MediaPipe/4D-Humans）
  └─ VR 遥操作（Quest 手柄/头显）→ 手+躯干轨迹
        │
        ▼
  Motion Retargeting（人体→人形）
  ├─ 形态差异：骨骼长度/关节数/自由度不同（人 20+DoF vs G1 29DoF/43DoF）
  ├─ 关节对应（joint correspondence）：SMPL 关节 ↔ URDF 关节映射表
  ├─ 约束：脚不穿地、手不穿物、关节限位、自碰撞
  ├─ 方法：数值 IK（逐帧解）或优化（平滑+物理约束，如 GMR）
  └─ 输出：参考关节轨迹（reference motion）
        │
        ▼
  Whole-Body Tracking Policy（RL）
  ├─ observation：当前状态 + 参考动作（当前帧/未来几帧）
  ├─ reward：姿态/速度跟踪误差 + 平衡正则 + 风格
  ├─ 方法：AMP/ASE（对抗模仿）、轨迹跟踪 reward、VAE 潜空间
  └─ 输出：关节命令（PD 目标）
        │
        ▼
  真机（G1/H1）执行
```

**三个必须回答的问题**（读每篇论文时都问）：
1. 输入是**什么数据**（MoCap/视频/VR）？
2. retargeting 是**离线优化**还是**在线实时**？
3. 跟踪 policy 用 **RL + reference motion reward** 还是**对抗学习（AMP）**还是**纯 IK**？

## 5.2 Retargeting 工具链（2026-08 已核实存在）

| 工具 | 说明 | 链接 |
|---|---|---|
| **GMR**（Generalized Motion Retargeting） | ICRA 2026，CPU 实时重定向，2617★ | [YanjieZe/GMR](https://github.com/YanjieZe/GMR) |
| **Humanoid-Motion-Retargeting** | 经典开源实现 | [XinLang2019/Humanoid-Motion-Retargeting](https://github.com/XinLang2019/Humanoid-Motion-Retargeting) |
| **amass_g1_retargeting** | AMASS 动捕数据集 → G1（Unitree 社区常用） | [edpsw/amass_g1_retargeting](https://github.com/edpsw/amass_g1_retargeting) |
| **CoRe** | 语义对应重定向（TPAMI 2023） | [tmjeong1103/CoRe](https://github.com/tmjeong1103/CoRe) |
| **trackerLab** | 人形运动跟踪工具箱（动捕/重定向/分析） | [Renforce-Dynamics/trackerLab](https://github.com/Renforce-Dynamics/trackerLab) |
| **BVH2SMPL** | BVH 动捕格式 → SMPL | [EmptyBlueBox/BVH2SMPL](https://github.com/EmptyBlueBox/BVH2SMPL) |

**Stage 3 实践项目**：用 AMASS 或自己的动捕/视频数据 → `amass_g1_retargeting` 或 GMR 重定向到 G1 → 在 MuJoCo/Isaac 里播放参考动作验证不穿模、不违背关节限位。

## 5.3 遥操作与数据采集（第 10 节）

| 系统 | 用途 | 适用机器人 | 链接 |
|---|---|---|---|
| **Open-TeleVision** | 立体视觉 + 头戴沉浸反馈遥操作（G1/H1） | G1/H1 | [OpenTeleVision/TeleVision](https://github.com/OpenTeleVision/TeleVision) |
| **DexCap** | 手部动捕 + 便携数据采集 | 人形（手部重点） | [j96w/DexCap](https://github.com/j96w/DexCap) |
| **MOBILE-ALOHA** | 移动双臂数据采集（低成本，人形双臂任务参考） | 轮式双臂 | [MarkFzp/mobile-aloha](https://github.com/MarkFzp/mobile-aloha) |
| **OmniH2O（VR 遥操作）** | 人→人形全身实时遥操作（H1） | H1 | 见 5.4 表 |

> 2026 年真机数据采集主流方案：**VR 遥操作（Quest 3/Vision Pro）+ 全身动捕（惯性套装）**，G1/H1 社区已有成熟的采集-重定向-训练闭环（unitree_rl_gym + 社区脚本）。

## 5.4 核心系统核实表（2026-08 核验，arXiv ID 均已勘误）

> ⚠️ 社区流传的很多 arXiv ID 是错的（如 HOVER 实为 2410.21229、SONIC 实为 2511.07820、ASAP 实为 2502.01143、BeyondMimic 实为 2508.08241、PHC 实为 2305.06456、ExBody 实为 2402.16796、ASE 实为 2205.01906、DexCap 实为 2403.07788）。下表全部为修正后 ID。

| 系统 | 年份 | 论文 | 输入 | 输出 | policy 控制什么 | RL? | reference motion? | retargeting? | 真机 | 开源 |
|---|---|---|---|---|---|---|---|---|---|---|
| **OmniH2O** | 2024 CoRL | [arXiv 2406.08858](https://arxiv.org/abs/2406.08858) | 人类 RGB 视频 | 全身+手部关节目标 | 全身+灵巧手（H1） | ✅ PPO | 遥操作数据（隐式） | ✅ | H1 | [LeCAR-Lab/human2humanoid](https://github.com/LeCAR-Lab/human2humanoid)（1058★, 2025-02） |
| **HumanPlus** | 2024 | [arXiv 2406.10454](https://arxiv.org/abs/2406.10454) | 单目 RGB 视频 | 全身+手部动作 | 步态+臂+手 | 部分（RL 全身+扩散手） | ✅ | ✅ | H1 | [MarkFzp/humanplus](https://github.com/MarkFzp/humanplus)（850★, 停更） |
| **HOVER** | 2024-25 | [arXiv 2410.21229](https://arxiv.org/abs/2410.21229) | 全身目标（速度/关节角多模式） | 全身关节速度 | 全身速度跟踪 | ✅ PPO (IsaacLab) | ✅ | ✅ | H2/H1 | [NVlabs/HOVER](https://github.com/NVlabs/HOVER)（756★, 2025-07） |
| **ExBody** | 2024 RSS | [arXiv 2402.16796](https://arxiv.org/abs/2402.16796) | 人类动捕（CMU） | 全身关节动作 | 全身跟踪 | ✅ | ✅ | ✅ | 仅仿真 | [chengxuxin/expressive-humanoid](https://github.com/chengxuxin/expressive-humanoid)（498★） |
| **ExBody2** | 2025 | [arXiv 2412.13196](https://arxiv.org/abs/2412.13196) | 动捕+仿真数据 | 全身关节速度 | 速度跟踪解耦+SDF 正则 | ✅ | ✅ | ✅ | **G1** | [edpsw/exbody2](https://github.com/edpsw/exbody2)（67★） |
| **SONIC** | 2025 | [arXiv 2511.07820](https://arxiv.org/abs/2511.07820) | 全身速度目标 | 全身关节速度 | 全身（GR00T 线） | ✅ | ✅ | ✅ | **G1** | [NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl)（3398★, **2026-08 极活跃**）+ [HF nvidia/GEAR-SONIC](https://huggingface.co/nvidia/GEAR-SONIC) |
| **BeyondMimic** | 2025 | [arXiv 2508.08241](https://arxiv.org/abs/2508.08241) | 人类视频/动捕 | 全身关节动作 | 引导扩散（零样本换技能） | ❌ 扩散模仿 | ✅ | ✅ | **G1** | [HybridRobotics/whole_body_tracking](https://github.com/HybridRobotics/whole_body_tracking)（2330★, 2025-10） |
| **ASAP** | 2025 RSS | [arXiv 2502.01143](https://arxiv.org/abs/2502.01143) | 参考运动/动捕 | 全身动作 | 速度跟踪+sim2real 动力学对齐 | ✅ | ✅ | ✅ | **G1**（+A1） | [LeCAR-Lab/ASAP](https://github.com/LeCAR-Lab/ASAP)（2097★, **2026-01 极活跃**） |
| **PHC** | 2023 ICCV | [arXiv 2305.06456](https://arxiv.org/abs/2305.06456) | 人类动捕（SMPL） | 全身关节 | 全身跟踪（仿真角色） | ✅ | ✅ | ✅（SMPL→机器人） | 仅仿真 | [ZhengyiLuo/PHC](https://github.com/ZhengyiLuo/PHC)（1279★） |
| **ASE** | 2021 SIGGRAPH Asia | [arXiv 2205.01906](https://arxiv.org/abs/2205.01906) | 技能标签/嵌入 | 角色全身动作 | 技能嵌入（仿真） | ✅ 对抗模仿 | 技能库 | ❌ | 仅仿真 | [xbpeng/MimicKit](https://github.com/xbpeng/MimicKit)（2242★, 2026-06） |
| **AMP** | 2021 SIGGRAPH | [arXiv 2104.02180](https://arxiv.org/abs/2104.02180) | 参考运动（风格） | 角色全身动作 | 对抗运动先验 | ✅ | ✅ | ❌ | 仅仿真 | 同上 MimicKit |
| **DWBC** | 2022 CoRL | [arXiv 2210.10044](https://arxiv.org/abs/2210.10044) | 任务（操作+行走） | 全身关节 | 统一策略（操作+运动） | ✅ | ❌ 任务奖励 | ❌ | 仅仿真 | [zhangxuelei86/Deep-Whole-Body-Control](https://github.com/zhangxuelei86/Deep-Whole-Body-Control)（停更） |

**ExBody ↔ ExBody2**：同团队续作。ExBody 仅仿真；ExBody2 加入"全身速度跟踪与身体地标跟踪解耦" + teacher policy 自动过滤不可行动作 + SDF 正则化，成功 sim2real 到 G1 —— 读 ExBody2 即可，ExBody 可作为理解过渡。

**2025–26 主线判断**：NVIDIA GR00T 线（SONIC + GR00T-WholeBodyControl，最活跃）、ASAP（sim2real 对齐）、BeyondMimic（扩散全身控制）、ExBody2/HOVER（真机全身跟踪）。**已过时/被替代**：DWBC、Mobile ALOHA、ExBody（被 ExBody2 取代）、PHC/ASE/AMP（仿真奠基作）。**G1/H1 复现难度（易→难）**：现成 retargeting 脚本 → BeyondMimic → ExBody2 → HOVER/GR00T-WBC（Isaac Lab 全家桶）→ ASAP（延迟 sim2real 最复杂）；H1 生态公开资料明显少于 G1。

## 5.5 Stage 3 · Milestone

**目标：human/reference motion → humanoid motion，并理解 whole-body tracking policy**

```
Week 8:
  D1–2  读 retargeting 基础（GMR 论文 + CoRe）+ 跑通 amass_g1_retargeting
  D3–4  用视频/动捕数据重定向 G1，在 MuJoCo 检查质量（穿模/限位）
  D5–7  读 AMP（[arXiv 2104.02180](https://arxiv.org/abs/2104.02180)）与 ASE：对抗学习如何让 policy 学风格
Week 9:
  D1–2  读 HOVER / ExBody2（全身跟踪 policy 代表作）
  D3–4  复现/运行一个 tracking policy 训练（用 reference motion reward）
  D5–7  综合：你的 retargeting + tracking 流水线跑通（人动作→G1 复现）
```

**Milestone 验证**：
- [ ] 能把一段人类动作（MoCap 或视频提取）重定向为 G1 参考轨迹并可视化
- [ ] 能解释 AMP 的判别器在学什么、为什么能保留风格
- [ ] 能说清 HOVER/SONIC 的输入输出与 policy 结构
- [ ] 跑通一个"参考动作 + RL 跟踪"的训练（sim）

**可以跳过**：SMPL 参数化细节（知道 24 关节/形状参数即可）、动捕硬件标定、视觉姿态估计网络训练。
