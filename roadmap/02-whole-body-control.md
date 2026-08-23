# 02 · 全身控制（Whole-Body Control, WBC）

> 定位：从"经典 WBC（QP/分层逆动力学）"到"学习式 WBC（RL policy）"的桥梁。**先理解经典 WBC 为什么存在、解决了什么问题，再学为什么 2024–2026 的主流倾向用 RL 替代它。**
> 时间预算：2 周（12 周计划 Week 4–5），理论 30% / 代码 70%。

## 2.1 概念谱系（先把术语排清楚）

| 术语 | 含义 | 与 WBC 的关系 |
|---|---|---|
| Operational Space Control (OSC) | Khatib 1987 提出：把任务（如手的位置）在动力学层面解耦控制 | WBC 的理论源头（[论文 DOI](https://doi.org/10.1109/JRA.1987.1087068)） |
| Task-space control | 在任务空间（而非关节空间）定义误差并控制 | OSC 的一般化 |
| Whole-Body IK (WBIK) | 运动学层面：同时求解多个任务（手/脚/骨盆/CoM）对应的关节角，通常带优先级 | 轻量方案，适合不追求力矩精度的场景 |
| Whole-Body ID / QP-WBC | 动力学层面：以**关节力矩**为决策变量，最小化任务误差同时满足接触/力矩/关节限位约束 | 力矩控制机器人的标准做法 |
| Hierarchical QP | 按优先级依次求解多个 QP，低优先级任务的解投影到高优先级任务的零空间 | WBC 的主流实现（TSID、HID） |
| Weighted QP | 单一 QP 用权重混合所有任务 | 简单但优先级不严格，工程上常用 |
| Null-space control | 低优先级任务只在高优先级任务的零空间内活动 | 实现"全身同时做事"的机制 |

## 2.2 核心问题：一个 humanoid 如何同时满足所有任务？

以"左手抓杯、右手开门、保持站立"为例，任务清单（按典型优先级从高到低）：

```
P0  接触约束：脚底不滑动、不穿透、法向力≥0、切向力在摩擦锥内   ← 硬约束（等式+不等式）
P1  平衡：CoM 加速度/质心动量跟踪（ZMP/捕获点稳定）            ← 最高优先任务
P2  躯干姿态：骨盆位置+朝向（浮动基座姿态）                    ← 中优先
P3  右手任务（开门把手位置/朝向）                              ← 低优先
P4  左手任务（抓杯）                                          ← 最低优先（两只手冲突时保右手）
P5  关节限位、速度限位、力矩限位                               ← 硬约束
```

**机制（Hierarchical QP / 分层逆动力学）**：

1. 把每个任务写成线性方程：$J_i \ddot{q} + \dot{J}_i \dot{q} = \ddot{x}_i^{des}$（任务加速度 = 参考加速度 + PD 反馈修正）
2. 按优先级依次求解：
   - 第 1 层：minimize $\|J_1\ddot{q} + \dot{J}_1\dot{q} - \ddot{x}_1^{des}\|^2$，约束：接触等式、摩擦锥不等式、关节限位
   - 第 2 层：minimize 任务 2 误差，约束 = 第 1 层约束 + **第 1 层的最优性条件**（即只在其零空间内活动）
   - 依此类推 → 低优先级任务永远不破坏高优先级任务
3. 解出 $\ddot{q}$ 后做逆动力学：$\tau = M\ddot{q} + C\dot{q} + G - J_c^T\lambda$，其中 $\lambda$ 是接触力（也由 QP 解出），得到关节力矩
4. 力矩机器人直接下发 $\tau$；位置机器人把 $\tau$ 的意图转成 PD 目标（或用 WBIK 只算关节角）

**为什么 balance 是 P1 而不是硬约束**：平衡是一个"软目标+硬接触"问题——脚接触是硬约束，CoM 稳定是软目标（因为身体可以通过踝/髋/跨步策略调节，不是非要跟踪某条精确轨迹）。**接触约束 + 摩擦锥 + 力矩限位是硬约束，任务全是软目标**，这是理解 WBC 的关键。

**三件必须懂的物理**：
- **平衡靠接触力**：所有支撑力来自脚底接触 wrench，QP 解出的 $\lambda$ 必须满足接触 wrench cone（CWC）——把 CoM 动力学和接触力约束连起来的正是质心动力学（[Orin et al. 2013](https://doi.org/10.1007/s10514-013-9341-4)）
- **动量控制**：$h_G = A_G \dot{q}$，控制质心线动量 + 全身角动量（[Herzog et al. 2016](https://arxiv.org/abs/1410.7284)）
- **优先级 vs 权重**：严格分层（lexicographic）在数学上干净，但工程上要处理"低优先级任务抖动"；加权 QP 更稳但调参痛苦。TSID 用严格分层，很多工业实现用加权。

## 2.3 必读论文（按阅读顺序）

| 论文 | 为什么读 |
|---|---|
| [Sentis & Khatib, A Whole-Body Control Framework (ICRA 2006)](https://doi.org/10.1109/ROBOT.2006.1642100) | WBC 框架的原始形态（操作空间 + 优先级） |
| [Saab et al., Dynamic WBC under rigid contacts (T-RO 2013)](https://doi.org/10.1109/TRO.2012.2234351) | 第一个把摩擦锥/单边约束写进 QP 的全身运动生成 |
| [Kuindersma et al., QP for stabilizing dynamic locomotion (ICRA 2014)](https://arxiv.org/abs/1311.1839) | Atlas 上 LQR+QP 的力矩分配，工程味道最浓 |
| [Del Prete et al., TSID (RAS 2015)](https://arxiv.org/abs/1410.3863) | 严格分层 QP 的完整数学与实现（TSID 库理论来源） |
| [Herzog et al., Momentum + Hierarchical ID (Autonomous Robots 2016)](https://arxiv.org/abs/1410.7284) | 平衡（动量）与分层逆动力学的结合，读代码前必读 |
| [Kuindersma et al., Atlas system paper (2016)](https://doi.org/10.1007/s10514-015-9479-3) | 完整系统：规划→估计→WBC 怎么拼起来 |
| [Caron et al., HRP-4 admittance WBC (ICRA 2019)](https://arxiv.org/abs/1809.07073) | 接触力直接反馈进 WBC 的工程示范 |

> 论文不必精读公式，重点理解：决策变量是什么、约束是什么、优先级怎么实现。

## 2.4 开源实现（按上手顺序）

1. **TSID**（[GitHub](https://github.com/stack-of-tasks/tsid)）+ **Pinocchio**：分层 QP WBC 的标准实现。读 `python/examples` 里的平衡/行走例子
2. **Crocoddyl**（[GitHub](https://github.com/loco-3d/crocoddyl)）：接触最优控制/MPC，`examples/humanoid` 目录有人形例子
3. **mc_rtc**（IIT，[GitHub](https://github.com/jrl-umi3218/mc_rtc)）：实时全身控制框架（任务栈 + 控制器），支持 HRP/其他平台，有完整教程；**实际做真机 WBC 最接近生产级的开源方案**
4. **OpenSoT**（[GitHub](https://github.com/ADVRHumanoids/OpenSoT)）：任务约束优化（IIT），常与 mc_rtc 配合
5. **Drake**（[GitHub](https://github.com/RobotLocomotion/drake)）：用 `MathematicalProgram` 手写 QP-WBC 的绝佳学习平台（约束 API 清晰）
6. **OCS2**（[GitHub](https://github.com/leggedrobotics/ocs2)）：ETH 的 MPC 工具箱，`ocs2_mpc` 里有人形例子

> ⚠️ **给 RL 学习者的提醒**：经典 WBC 的调试成本高（QP 病态、优先级抖动、接触力噪声）。2024–2026 的主流研究路线是 **"RL 学全身策略 / 学 WBC 残差"**（见 03/05/06 篇）。经典 WBC 的学习价值在于：**它是理解 reward 设计、动作空间设计、接触约束的物理语言**——不建议花超过 2 周。

## 2.5 Stage 2 · 学习路径与 milestone

**目标**：实现 `desired hand/pelvis/foot target → whole-body joint command`

```
Week 4（理论）:
  D1–2  读 Sentis 2006 + Saab 2013（只看问题与框架）
  D3–4  读 Del Prete TSID（数学部分）+ 跑 TSID 库的 python example
  D5–6  读 Herzog 2016 + Kuindersma 2014
Week 5（代码）:
  D1–3  用 Pinocchio + qpOASES/proxsuite 手写一个 2 层分层 QP：
        P0 接触约束 → P1 CoM/平衡 → P2 手目标
  D4–5  在 MuJoCo 里加载 G1：用自己写的 QP-WBC 让机器人站住并抬手
  D6–7  对比：同一任务用 TSID 库实现；写清两种实现的优先级处理差异
```

**Milestone 验证**：
- [ ] 用自己写的分层 QP，G1 在 MuJoCo 中保持平衡的同时，双手到达两个指定位置（脚不动）
- [ ] 能解释为什么降低手目标优先级后平衡更稳
- [ ] 把摩擦系数从 1.0 改到 0.3，能预测并观察到失稳行为
- [ ] 能指出 TSID 源码中"分层"是在哪个函数实现的

**可以跳过**：严格的分层稳定性证明、全身阻抗参数整定、多接触（双手双脚攀爬）QP 的完整实现。
