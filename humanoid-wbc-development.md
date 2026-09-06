# 人形机器人全身控制（Whole-Body Control）发展路线与技术分析

> 版本：2026-08 · 所有引用论文/系统均经核实并附链接（DOI / arXiv / 官方页）。
> 配套资源：[论文时间线](papers.md) · [学习路线](roadmap/README.md) · [公开课程](courses.md)

---

## 1. 问题定义：什么是 Whole-Body Control

人形机器人有 20–43 个自由度（G1 为 29/43 DoF，H1 为 23 DoF），底座是**浮动基座**（6 个虚拟自由度，不与地面固连）。全身控制（WBC）解决的问题是：

> **在欠驱动（浮动基座）、高度冗余、强接触约束（脚/手与地面和环境）的条件下，同时满足多个互相冲突的任务：平衡、脚底接触、骨盆姿态、躯干朝向、双手末端目标、CoM 稳定，并输出全身关节命令（位置或力矩）。**

核心难点（按重要性排序）：
1. **平衡**：没有固定底座，所有支撑力来自脚底接触，必须显式建模接触约束（摩擦锥、单边法向力）
2. **任务优先级**：多个任务互相冲突（如双手目标冲突、手臂运动扰动平衡），需要优先级/零空间机制
3. **欠驱动**：6 个底座自由度不可直接驱动，只能通过接触反作用力间接控制
4. **接触-运动耦合**：手脚接触力与全身运动互相影响，push/pull/carry 等操作任务必须"平衡感知"

---

## 2. 发展时间线（四代演进）

| 代际 | 时期 | 主题 | 里程碑 |
|---|---|---|---|
| 第一代 | 1970s–1990s | 理论基础 | ZMP、操作空间、LIPM、被动行走 |
| 第二代 | 2000s | 平台+框架形成 | ASIMO/HRP-2、ZMP 预览控制、动量控制、OSC→WBC |
| 第三代 | 2010s | 优化控制成熟 | 质心动力学、QP-WBC、TSID、步态 MPC、DRC 工程验证 |
| 第四代 | 2020s | 学习式控制变革 | RL 全身策略、数据驱动、VLA×WBC 分层 |

### 2.1 第一代（1970s–1990s）：理论奠基

**核心贡献：把"双足稳定"从直觉变成数学。**

- **ZMP 理论**：[Vukobratović & Stepanenko 1972](https://doi.org/10.1016/0025-5564(72)90061-2) 提出零力矩点（ZMP）与稳定性判据——此后 50 年双足步态控制的基本语言
- **动态行走雏形**：[Miura & Shimoyama 1984](https://doi.org/10.1177/027836498400300206)（BIPER 动态行走）、[Raibert 1984](https://doi.org/10.1177/027836498400300207)（单腿跳跃平衡）
- **操作空间理论**：[Khatib 1987](https://doi.org/10.1109/JRA.1987.1087068)：任务空间（而非关节空间）的动力学控制——WBC 的数学源头
- **LIPM 线性倒立摆**：[Kajita & Tani 1991](https://doi.org/10.1109/ROBOT.1991.131811)：把双足动力学简化为线性模型，步态生成的标准工具
- **被动行走**：[McGeer 1990](https://doi.org/10.1177/027836499000900206)：无主动控制也能稳定行走，揭示了行走的能量学本质
- **硬件萌芽**：早稻田 WL 系列（[Takanishi 1990](https://doi.org/10.1109/IROS.1990.262408) 躯干补偿 ZMP）、[本田 P2/P3（1998）](https://doi.org/10.1109/ROBOT.1998.677288)——第一个自主行走的全尺寸人形

### 2.2 第二代（2000s）：人形平台与全身控制框架形成

**核心贡献：人形硬件成熟 + WBC 从"单任务"走向"多任务全身协调"。**

- **平台**：[ASIMO（2002）](https://doi.org/10.1109/IRDS.2002.1041641)、[HRP-2（2004）](https://doi.org/10.1109/ROBOT.2004.1307969)——全身控制研究的标准实验平台
- **步态生成成熟**：[ZMP 预览控制（Kajita 2003）](https://doi.org/10.1109/ROBOT.2003.1241826)：利用未来参考输入，成为步行生成事实标准
- **动量控制起点**：[Resolved Momentum Control（Kajita 2003）](https://doi.org/10.1109/IROS.2003.1248880)：以线/角动量为全身运动的规划与跟踪量，开启动量类 WBC 路线
- **动力学滤波器**：[Yamane & Nakamura 2003](https://doi.org/10.1109/TRA.2003.810579)：运动学目标实时投影到动力学可行空间
- **WBC 框架诞生**：[Sentis & Khatib 2005](https://doi.org/10.1142/S0219843605000594)（优先级分层行为合成）→ [2006 全身控制框架](https://doi.org/10.1109/ROBOT.2006.1642100)：操作空间 + 任务优先级 + 零空间的统一框架
- **平衡的全身化**：[Sugihara & Nakamura 2002](https://doi.org/10.1109/IRDS.2002.1041658)（质心雅可比全身平衡）、[Hirukawa 2006 adios ZMP](https://doi.org/10.1109/ROBOT.2006.1641995)（任意接触构型的稳定判据）
- **柔顺交互**：[Hyon 2007](https://doi.org/10.1109/TRO.2007.904896)：全身柔顺/阻抗控制下的人机交互平衡
- **并行路线（HZD）**：[Westervelt et al. 2003](https://doi.org/10.1109/TAC.2002.806653) 混合零动力学，用虚拟约束形式化设计动态步态（后在 [Ames 2014](https://doi.org/10.1109/TAC.2014.2299342) 达到顶峰，但 2020s 后不再是主流）

### 2.3 第三代（2010s）：QP 优化与 MPC 的黄金十年

**核心贡献：全身控制从"启发式"走向"实时优化"，并在 DRC（DARPA 机器人挑战赛）中得到残酷的工程验证。**

- **质心动力学**：[Orin, Goswami & Lee 2013](https://doi.org/10.1007/s10514-013-9341-4)：质心动量矩阵 A_G，把全身动力学投影到 6 维——全身控制与步态规划的基石模型
- **QP-WBC 定型**：
  - [Saab et al. 2013](https://doi.org/10.1109/TRO.2012.2234351)：刚性接触 + 摩擦锥单边约束下的 QP 全身运动生成（HRP-2 验证）
  - [Kuindersma et al. 2014](https://arxiv.org/abs/1311.1839)：LQR + 可高效求解 QP 的全身力矩分配（Atlas 平衡核心）
  - [Feng et al. 2015](https://doi.org/10.1002/rob.21559)（CMU DRC）、[Kuindersma et al. 2016](https://doi.org/10.1007/s10514-015-9479-3)（MIT Atlas 系统论文：规划+估计+QP 控制一体化）
- **分层逆动力学**：[Herzog et al. 2014](https://arxiv.org/abs/1305.2042)（HID 平衡实验）→ [2016 动量+分层 ID](https://arxiv.org/abs/1410.7284)
- **TSID**：[Del Prete et al. 2015](https://arxiv.org/abs/1410.3863)：任务空间逆动力学，严格分层 QP 的完整数学与开源实现
- **步态 MPC 成熟**：
  - [Wieber 2006](https://doi.org/10.1109/ICHR.2006.321375)（线性 MPC 源头）→ [Herdt 2010](https://doi.org/10.1163/016918610X493552)（落脚点进决策变量）
  - [Englsberger 2011](https://doi.org/10.1109/IROS.2011.6094435)（Capture Point）→ [2013 三维 DCM](https://doi.org/10.1109/IROS.2013.6696723) → [2015 T-RO 期刊版](https://doi.org/10.1109/TRO.2015.2405592)
  - [Koolen/Pratt 2012](https://doi.org/10.1177/0278364912452673)：capturability 理论（N 步可捕获区域）
- **动量平衡**：[Lee & Goswami 2012](https://doi.org/10.1007/s10514-012-9294-z)（质心动量平衡控制器）
- **全身 MPC 实机**：[Koenemann et al. 2015](https://doi.org/10.1109/IROS.2015.7353843)（HRP-2 全身 MPC）、[Fallon et al. 2015](https://doi.org/10.1109/HUMANOIDS.2015.7363465)（Atlas 立体视觉+落脚点+全身控制）
- **多接触运动**：[Carpentier & Mansard 2018](https://doi.org/10.1109/TRO.2018.2862902)：双手双脚多接触规划/控制框架
- **DRC 工程沉淀**：[IHMC 经验总结 2015](https://doi.org/10.1002/rob.21571)、[DRC 决赛官方总结 2017](https://doi.org/10.1002/rob.21683)——力矩控制 + 全身 QP 在灾难现场环境的极限测试

### 2.4 第四代（2020s）：学习式控制的范式变革

**核心贡献：从"建模-优化"转向"数据-学习"，RL 成为人形运动控制的研究主流；2025 起 VLA 与 WBC 分层融合。**

- **RL 腿足突破**：[Hwangbo 2019](https://arxiv.org/abs/1901.08652)（并行 RL 训四足）→ [Lee 2020](https://arxiv.org/abs/2010.11251)（教师-学生特权学习）→ [Rudin 2022](https://arxiv.org/abs/2109.11978)（GPU 并行训练，分钟级收敛）
- **人形 RL 实机**：[Radosavovic 2024](https://arxiv.org/abs/2303.03381)（Digit 真机直训）、[Haarnoja 2024](https://arxiv.org/abs/2304.13653)（双足足球，Sci. Robotics）
- **统一全身策略**：[DWBC 2022](https://arxiv.org/abs/2210.10044)：单策略统一移动+操作（学习式 WBC 的原型）
- **全身跟踪/数据飞轮**（2024–2025 主线）：
  - [OmniH2O 2024](https://arxiv.org/abs/2406.08858)（人→人形全身遥操作，H1）、[HumanPlus 2024](https://arxiv.org/abs/2406.10454)（影子跟随）
  - [Expressive WBC 2024](https://arxiv.org/abs/2402.16796)（H1 跑跳舞蹈）、[HOVER 2024](https://arxiv.org/abs/2410.21229)（多模式全身速度控制）
  - [ExBody2 2025](https://arxiv.org/abs/2412.13196)（G1 真机全身跟踪）、[BeyondMimic 2025](https://arxiv.org/abs/2508.08241)（扩散全身控制）、[SONIC 2025](https://arxiv.org/abs/2511.07820)（NVIDIA GR00T 线）
- **sim2real 对齐**：[ASAP 2025](https://arxiv.org/abs/2502.01143)：真实数据驱动的延迟与物理残差校正（RSS 2025）
- **VLA × WBC 分层**（2025–2026）：
  - [GR00T N1 2025](https://arxiv.org/abs/2503.14734)（开源人形 VLA）→ [GR00T N1.5](https://research.nvidia.com/labs/gear/gr00t-n1_5/)（关节速度→Decoupled WBC 的标准形态）
  - [π0 2024](https://arxiv.org/abs/2410.24164)（flow matching VLA）、[WholeBodyVLA 2025](https://arxiv.org/abs/2512.11047)（统一 latent 动作空间）、[LeVERB 2025](https://arxiv.org/abs/2506.13751)（latent 指令全身控制）
  - 大厂：Figure [Helix](https://www.figure.ai/news/helix)、DeepMind [Gemini Robotics](https://arxiv.org/abs/2503.20020)
- **世界模型/合成数据**：1X [World Model](https://www.1x.tech/discover/1x-world-model)、Genesis 生成式仿真

---

## 3. 核心技术体系分解

### 3.1 建模技术（WBC 的物理基础）

| 技术 | 内容 | 用途 |
|---|---|---|
| 浮动基座刚体动力学 | $M(q)\ddot{q}+C(q,\dot{q})\dot{q}+G(q)=\tau+J_c^T\lambda$ | 逆动力学、QP 约束、MPC 模型 |
| 质心动力学 | 质心动量矩阵 $A_G$，$h_G=A_G\dot{q}$ | 平衡任务、步态规划（[Orin 2013](https://doi.org/10.1007/s10514-013-9341-4)） |
| 接触建模 | 接触 Jacobian、摩擦锥 $\sqrt{f_x^2+f_y^2}\le\mu f_z$、接触 wrench cone（CWC） | 脚/手接触的硬约束 |
| 关节限位/力矩限位 | 不等式约束 | QP 的可行域 |

### 3.2 平衡理论演化（一条清晰的学术主线）

```
ZMP（1972）─┬─→ FRI（Goswami 1999）──→ adios ZMP（2006，多接触）
            ├─→ LIPM（1991/2001）──→ ZMP 预览控制（2003）──→ 落脚点 MPC（2006-2010）
            └─→ 捕获点/CP（2006 SRI）──→ DCM 3D（2011-2015）──→ capturability 理论（2012）
                                                        └─→ 动量平衡控制（2012-2016）
```

关键认知：**平衡从"判据"（ZMP）走向"控制量"（捕获点/DCM），再走向"动力学投影"（质心动量）**。

### 3.3 控制架构演化

```
操作空间控制 OSC（1987）          ← 单任务动力学解耦
   ↓
任务优先级分层（2005-2006）        ← 多任务 + 零空间
   ↓
QP 全身控制（2013-2016）           ← 接触约束 + 摩擦锥 + 限位进优化
   ├─ 加权 QP（工程简单，调参痛苦）
   └─ 分层 QP（TSID 2015 / HID 2016：严格优先级，数学干净）
   ↓
全身 MPC（2015）                   ← 滚动时域 + 预测模型
   ↓
学习式 WBC（2022-2026）            ← RL 策略替代 QP 求解
```

**核心机制（无论哪一代都成立）**：
- 硬约束 vs 软任务：接触/摩擦锥/限位是硬约束，任务全是软目标
- 优先级 = 低优先级任务只在高优先级任务的零空间内活动
- 平衡永远是最高优先级的"软目标"（可通过踝/髋/跨步调节，不是精确轨迹）

### 3.4 步态与运动规划

- 经典：LIPM 步态生成 → ZMP 预览控制 → 落脚点 MPC（Herdt 2010）→ 全身轨迹优化（[Dai 2014](https://doi.org/10.1109/HUMANOIDS.2014.7041375) 质心动力学+全身运动学 direct transcription）
- 学习式：policy 隐式学习步态与接触调度，velocity-command 策略为标准形态

### 3.5 学习式控制技术栈（2026 标准配方）

```
Observation：关节位置/速度 + IMU/重力向量 + base 速度 + previous action + command（+感知）
Action：joint target（PD 位置控制）| torque | residual
低层：PD controller τ = kp(q_des−q) − kd·q̇
训练：PPO + GAE（rsl_rl / Isaac Lab）+ reward 工程
sim2real：domain randomization + 特权学习/教师-学生（Lee 2020）+ 课程学习
         + 真实数据校正（ASAP 2025）
风格/参考动作：AMP/ASE 对抗模仿（[AMP 2021](https://arxiv.org/abs/2104.02180) · [ASE 2021](https://arxiv.org/abs/2205.01906)）
```

### 3.6 数据与遥操作（第四代的关键基础设施）

- 运动重定向：人体（SMPL/动捕/视频）→ 人形参考动作（[GMR](https://github.com/YanjieZe/GMR) 等工具链）
- 全身遥操作：[OmniH2O](https://arxiv.org/abs/2406.08858)（视频/VR → H1）、[Open-TeleVision](https://arxiv.org/abs/2407.01512)（立体视觉沉浸遥操作）
- 全身跟踪策略：把参考动作变成可执行 skill（HOVER/ExBody2/SONIC/BeyondMimic）

### 3.7 VLA × WBC 分层架构（2025–2026 主流形态）

```
路线 A：VLA ──直接出 20–40 DoF joint──▶ robot        （GR00T N1、Helix，仅数据充分的单一本体）
路线 B：VLA ──EE/body 命令──▶ WBC ──joint──▶ robot    （GR00T N1.5 + Decoupled WBC，工程主流）
路线 C：VLA ──latent action──▶ 低层全身 policy──▶ robot（π0、WholeBodyVLA、LeVERB，研究热点）
```

趋势：**B+C 融合**（统一 latent VLA + 可学习/解耦的 WBC 低层），人视频预训练 + RL 微调成为标准数据配方。

---

## 4. 两条技术路线对比

| 维度 | 模型优化路线（QP/MPC） | 学习路线（RL） |
|---|---|---|
| 模型依赖 | 需要精确动力学模型 | 无模型（或世界模型辅助） |
| 鲁棒性来源 | 反馈回路 + 保守参数 | 大规模随机化训练 |
| 地形/感知适应 | 需要显式规划 | 感知直接进 observation，端到端 |
| 真机部署 | 力矩控制 + 状态估计要求高 | PD 位置控制即可，sim2real 成熟 |
| 可解释性 | 好（物理量明确） | 差（黑盒） |
| 数据需求 | 低 | 高（仿真可大规模生成） |
| 2026 现状 | 工业界仍在使用（MPC 步态） | **研究绝对主流** |
| 融合方向 | MPC 生成参考 → RL 跟踪；RL 学 WBC 残差；真实数据校正动力学（ASAP） | |

---

## 5. 2026 现状：代表系统与事实标准

- **开源事实标准**：[GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl)（SONIC + GEAR，3398★ 极活跃）——VLA→WBC 落地范本
- **sim2real 标杆**：[ASAP](https://github.com/LeCAR-Lab/ASAP)（G1 真机）
- **训练框架**：Isaac Lab（v2.3.2 稳定）+ rsl_rl；轻量验证用 MuJoCo Playground
- **真机平台**：Unitree G1/H1 是社区最成熟的开源生态（[unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym)）
- **NVIDIA 官方工作流**：[WBC-AGILE](https://github.com/nvidia-isaac/WBC-AGILE)（Isaac Lab 3.0 全身 RL 工作流）

## 6. 关键挑战与未来方向

1. **数据**：真机数据的获取成本（遥操作/动捕/视频）仍是瓶颈 → 世界模型与合成数据（1X WM、Genesis）
2. **sim2real 差距**：延迟、动力学误差、接触参数 → ASAP 式真实数据校正成为标配
3. **VLA 与 WBC 的接口**：命令空间设计（速度？末端？latent？）是 B 路线的核心瓶颈
4. **接触丰富操作**：多接触（双手双脚）、力控操作仍是 QP 与 RL 都困难的领域
5. **实时性与计算**：端侧 VLA + 高频 WBC 的算力分配（Helix 200Hz 上身控制是参考）
6. **可解释性与安全**：学习式策略的稳定性保证、安全滤波器（如 [Agile But Safe](https://arxiv.org/abs/2401.17583) 思路）

## 7. 简版学习路径（完整版见 [roadmap](roadmap/README.md)）

```
理论基础（Underactuated / CMU 16-745 / Modern Robotics）
  → WBC 综述（[Del Prete 2022](https://inria.hal.science/hal-02456663v1)）建立全局
  → 三代论文按序读（本文件第 2 节）
  → Isaac Lab 跑通 G1/H1 locomotion（训练配方：Rudin 2022 → Lee 2020 → ASAP）
  → 全身跟踪系统复现（HOVER → ExBody2 → SONIC）
  → VLA 分层（GR00T-WholeBodyControl 代码 + π0/WholeBodyVLA 论文）
```

## 8. 关键参考文献索引

- 综述：[Humanoid Loco-Manipulation 2025](https://arxiv.org/abs/2501.02116) · [Learning-based Legged 2024](https://arxiv.org/abs/2406.01152) · [MPC for Legged 2023](https://doi.org/10.1080/01691864.2023.2168134) · [WBC: Past Present Future 2022](https://inria.hal.science/hal-02456663v1) · [行为基础模型综述 2025](https://arxiv.org/abs/2506.20487)
- 完整 222 篇论文时间线（1972–2026，全部附链接）：[papers.md](papers.md)
- 书籍：[books.md](books.md)（Kajita 教材、Nenchev WBC 专著、Humanoid Robotics: A Reference 等）
