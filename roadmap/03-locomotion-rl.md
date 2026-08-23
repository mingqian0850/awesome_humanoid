# 03 · 人形运动控制（Locomotion）与强化学习（RL）

> 定位：这是 roadmap 的**主干**。两条路线并行理解：经典（ZMP/MPC）作为物理语言，学习式（RL）作为 2024–2026 的主流武器。
> 时间预算：3 周（12 周计划 Week 2–3 起步、Week 6–7 深化），代码占比 75%+。

## 3.1 经典路线 vs 学习路线（先建立坐标系）

| 维度 | 经典（ZMP + MPC + WBC） | 学习式（RL policy） |
|---|---|---|
| 模型 | LIPM / 质心动力学简化模型 | 无模型（或世界模型辅助） |
| 步态生成 | 离线/在线规划 ZMP+落脚点，MPC 滚动优化 | policy 直接输出关节命令 |
| 鲁棒性来源 | 反馈回路（踝/髋/跨步）+ 保守参数 | 大规模随机化训练（扰动、地形、延迟） |
| 地形适应 | 需要感知 → 落脚点规划 | 感知（高程图/深度）进 observation，端到端 |
| 真机部署 | 力矩控制 + 状态估计要求高 | PD 位置控制 + 少量状态即可，sim-to-real 成熟 |
| 2026 现状 | 仍是 MPC 步态的主流（工业），但研究热点已转移 | **研究绝对主流**，Unitree G1/H1 社区全部走这条 |

**结论：两条都要懂，但 70% 精力给 RL**。经典路线是解释性语言（ZMP/CoM/落脚点），RL 是工程实现。

## 3.2 经典概念速查（每个都要能说出"这是什么、为什么用"）

- **ZMP / support polygon**：动态稳定判据（见 01 篇）
- **LIPM / 3D-LIPM**：把质心动力学简化成线性倒立摆（[Kajita 2001](https://doi.org/10.1109/IROS.2001.973365)），MPC 步态的内核
- **MPC 步态**：滚动时域优化落脚点 + ZMP（[Wieber 2006](https://doi.org/10.1109/ICHR.2006.321375)、[Herdt 2010](https://doi.org/10.1163/016918610X493552)）
- **DCM / Capture Point**：不稳定模态的显式表达，落脚点调节的物理直觉（[Englsberger 2011/2013](https://doi.org/10.1109/IROS.2011.6094435)）
- **质心动力学 + 动量控制**：平衡的动力学语言（[Orin 2013](https://doi.org/10.1007/s10514-013-9341-4)、[Lee & Goswami 2012](https://doi.org/10.1007/s10514-012-9294-z)）
- **接触调度（contact scheduling）**：行走=支撑相/摆动相切换；MPC 里是模式切换，RL 里是隐式学出来的
- **状态估计**：浮动基座位姿 + 速度估计（IMU + 腿部运动学 + 接触检测），实机 RL 的 observation 依赖它。经典参考：[MIT Cheetah 状态估计](https://arxiv.org/abs/2102.05433)（不精读，知道 pipeline 即可）

## 3.3 现代 RL locomotion policy 的标准结构（必须背下来）

```
Observation（典型 60–100 维）:
  joint position / joint velocity（全身关节）
  IMU 角速度、重力向量（base 姿态）
  base 线速度（估计值）
  previous action（动作历史）
  command（速度指令 vx, vy, ωyaw，或目标位姿）
  （地形感知时）高程图 / 深度图

Action:
  joint target position（关节目标角）← 最常见
  或 joint torque（力矩，较少）
  或 residual action（叠加在 PD 目标上）

Low-level:
  PD controller: τ = kp(q_des − q) − kd·q̇
  → 位置控制人形（G1/H1）的标配，policy 只出 q_des
```

**三个关键设计决策**：
1. **动作空间用 joint target 而非 torque**：真机 PD 增益稳定、sim-to-real 更容易；代价是策略学不到精确力控
2. **reward 设计**：`tracking velocity command + 姿态/关节正则 + 能量惩罚 + 周期奖励`是基线；[Rudin 2022](https://arxiv.org/abs/2109.11978) 的 reward 模板几乎被所有 repo 复用
3. **sim-to-real 三板斧**：domain randomization（摩擦/质量/延迟/PD 增益随机化）+ 特权学习/教师-学生（[Lee 2020](https://arxiv.org/abs/2010.11251)）+ 课程学习（先平地后地形/扰动）

## 3.4 必读论文（有代码优先，按顺序）

| 论文 | 代码 | 读什么 |
|---|---|---|
| [Hwangbo 2019, Learning agile motor skills (Sci. Robotics)](https://arxiv.org/abs/1901.08652) | [rsl_rl](https://github.com/leggedrobotics/rsl_rl) | 并行 RL 训腿足的开端 |
| [Lee 2020, Quadrupedal locomotion over challenging terrain](https://arxiv.org/abs/2010.11251) | [legged_gym](https://github.com/leggedrobotics/legged_gym) | 教师-学生特权学习范式 |
| [Rudin 2022, Learning to walk in minutes](https://arxiv.org/abs/2109.11978) | [rsl_rl](https://github.com/leggedrobotics/rsl_rl) | 现代训练基础设施 + reward 模板 |
| [Siekmann 2020, Memory-based Cassie control](https://arxiv.org/abs/2006.02402) | 无 | 双足（非四足）RL 的关键差异 |
| [Radosavovic 2024, Real-world humanoid locomotion (Digit)](https://arxiv.org/abs/2303.03381) | 无 | 真机直训人形 |
| [Expressive WBC (H1, 2024)](https://arxiv.org/abs/2402.16796) | [humanoid-bench](https://github.com/chengxuxin/humanoid-bench) | H1 上跑、跳、舞；观察/奖励工程范本 |

（2023–2026 完整论文表见 [08-papers.md](08-papers.md)，含 ASAP/FLEX/Bolt/Sieve 等）

## 3.5 RL：你到底需要学多少？（最短路径）

> 目标不是成为 RL 理论家。目标：**能读懂 policy 代码、能改 reward、能训练收敛**。

**必须亲手实现/推一遍（~10 小时）**：
1. **Policy Gradient → PPO**：只理解"最大化带 clip 的 surrogate objective"这 5 行核心公式（[OpenAI Spinning Up PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html)）
2. **Actor-Critic**：两个网络分别干什么（π 输出动作分布，V 输出价值/优势估计）
3. **GAE**：$\hat{A}_t = \sum(\gamma\lambda)^l \delta_{t+l}$，知道 λ 是偏差-方差权衡旋钮即可

**能读懂即可（不深究）**：policy/value 网络结构细节、entropy bonus、clip 参数敏感性、value clipping。
**直接用库（不自己写）**：PPO 的工程实现 —— **rsl_rl** 或 Isaac Lab 内置。

**最短路径清单**：
1. Spinning Up 的 PPO 页（1 小时）
2. CleanRL 的 [ppo.py](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo.py) 通读（2 小时，注释极好）——理解通用 PPO 实现
3. 跑通一个 Isaac Lab 内置 humanoid 训练（1 天，见 04 篇）
4. 改 reward 重训，观察行为变化（1 天）
5. 需要时再补：privileged info / teacher-student / curriculum / domain randomization（跟着 legged_gym 或 humanoid 例子学，不单独啃理论）

> **结论：PPO+GAE 理解到"能解释代码每一行"即可，其他 RL 技术（SAC、offline RL、model-based）2026 年做 humanoid locomotion 都用不上**。真正常学的是"奖励工程 + 环境工程"，这才是 humanoid RL 的护城河。

## 3.6 训练框架现状（2026 视角）

| 框架 | 状态 | 用途 |
|---|---|---|
| **rsl_rl**（[GitHub](https://github.com/leggedrobotics/rsl_rl)） | ✅ 活跃，腿足 RL 事实标准 | 人形 locomotion 主力；Isaac Lab 官方适配 |
| **Isaac Lab 内置 RL**（[docs](https://isaac-sim.github.io/IsaacLab/)） | ✅ 活跃，官方推荐 | 不用装 rsl_rl 也行（`--agent rsl_rl` 参数） |
| **rl_games**（[GitHub](https://github.com/Denys88/rl_games)） | ⚠️ 基本停止活跃开发 | 老项目在用；新项目不推荐 |
| **SKRL**（[GitHub](https://github.com/skrl-project/skrl)） | ✅ 活跃，通用 Gymnasium 框架 | 想用标准 Gym 接口时选它 |
| **legged_gym**（[GitHub](https://github.com/leggedrobotics/legged_gym)） | ⚠️ 依赖旧版 Isaac Gym（已废弃），但代码仍是学习范本 | 读代码学习，别在新项目里用 |
| **Isaac Gym（旧版）** | ❌ 已废弃 | 官方迁移到 Isaac Lab |

## 3.7 Stage 1 · Milestone

**目标：在 Isaac Lab 中跑通并理解一个 Unitree G1/H1 locomotion policy**

```
Week 6–7（在 04 篇环境搭建完成后）:
  D1–2  跑通 Isaac Lab 内置 humanoid（G1/H1）velocity 任务，训练到稳定行走
  D3–4  逐行读 reward 函数：每个 reward 项删掉后重训，观察行为退化
  D5    加地形（斜坡/台阶/碎石），理解课程学习怎么调度
  D6    加 domain randomization（摩擦/质量/PD 增益），观察鲁棒性变化
  D7    换动作空间（joint target vs residual action）对比收敛
```

**Milestone 验证**：
- [ ] 能说出 observation 每一维的物理含义和来源（哪些是估计的、哪些是特权量）
- [ ] 改 reward 权重后能预测性地改变行为（如压低 energy penalty → 步频变化）
- [ ] 训出的 policy 在随机地形上不摔（中等难度）
- [ ] 能解释 PPO 代码里 clip、GAE、entropy 各自作用

**可以跳过**：SAC/DDPG 等 off-policy 算法、reward shaping 的理论分析、HZD 步态设计、MPC 的数值求解器细节。
