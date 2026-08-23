# 06 · 人形 Loco-Manipulation（移动操作）（Stage 5）

> 定位：把 Stage 1–4 的能力**合起来**——人形边移动边操作。这是 2024–2026 最热的研究方向之一，也是你 roadmap 的毕业项目主题。
> 时间预算：2 周（12 周计划 Week 10–11）。
> 前置：Stage 1（locomotion）+ Stage 2/4（WBC）已跑通。

## 6.1 humanoid manipulation vs fixed-base manipulator（第 8 节：先理解差异）

| 维度 | 固定基座机械臂 | 人形移动操作 |
|---|---|---|
| 基座 | 刚性固定 | **浮动基座**：手臂反作用力直接扰动平衡 |
| 工作空间 | 固定 | 移动扩展（大空间任务：搬运、开门、上下楼梯操作） |
| 平衡约束 | 无 | **操作必须"平衡感知"**：手臂伸展改变 CoM、接触力改变动量 |
| 冗余自由度 | 6–7 DoF | 20–43 DoF（全身冗余 → 任务分配的自由度） |
| 接触 | 末端 + 环境 | **多接触**（脚 + 手 + 物体），接触调度复杂 |
| 负载 | 静态标定 | **载荷影响步态**（惯量/重量变化 → 步态参数必须自适应） |

**核心物理直觉（必须内化）**：
1. **手臂动 → 平衡扰**：手臂快速伸出时，质心动量改变，需要腿/躯干补偿（这正是一体化全身策略 vs 分离"腿部策略+臂部 IK"的核心区别）
2. **手接触 → 力路径**：推门/推车时，手与环境的接触力通过全身传递到脚，WBC/策略必须把手的力约束与脚的支撑约束一起求解
3. **载荷 → 动力学变化**：搬运重物时质心偏移、惯性改变，velocity-command locomotion policy 若只在空载训练，实机会晃/摔 → 训练时随机化载荷是标配

## 6.2 主流系统架构（第 7 节：三种耦合方式）

```
Architecture A（解耦流水线，工程最稳）:
  High-level task policy（VLM/规则）
    → desired base velocity + EE target
    → Whole-body controller（QP-WBC 或 RL-WBC）
    → joint command → robot
  代表：GR00T 系列（N1.5 → Decoupled WBC）、经典 QP-WBC 方案
  优点：模块可分别调试；缺点：locomotion/manipulation 接口设计是瓶颈

Architecture B（任务空间轨迹 + 学习式 WBC）:
  Vision policy → task-space trajectory（手/身体轨迹）
    → learned WBC（全身跟踪/全身 RL policy）
    → full-body action → robot
  代表：ExBody2 / HOVER / SONIC（参考运动 + 全身跟踪）、OmniH2O
  优点：轨迹级语义清晰、数据好采；缺点：轨迹规划与运动控制分层调试

Architecture C（VLA → latent action → 低层 policy，研究热点）:
  VLA → latent action / skill representation
    → whole-body controller（学出来的低层）
    → robot
  代表：π0/π0.5、WholeBodyVLA（统一 latent 空间）、LeVERB
  优点：端到端联合优化、数据效率高；缺点：调试难、latent 不可解释
```

**2026 工程判断**：自己做项目选 **A（规则/VLM 高层 + 你的 learned WBC）** 最容易毕业；研究向选 C。

## 6.3 任务设计与训练配方（push / pull / carry / open door）

| 任务 | 难点 | 训练配方建议 |
|---|---|---|
| walk → reach → grasp → carry | 步态与手臂协调、抓取时平衡 | 课程学习：先分别训 locomotion + 臂部策略，再联合；或单一全身策略 + 任务 reward |
| walking while maintaining EE target | 末端位置保持 vs 步态扰动 | 全身策略直接吃 EE 目标进 observation（HOVER 的多模式输入就是干这个的） |
| 开门 | 手接触力 + 门铰链运动学 + 平衡 | 力/接触 reward + 门动力学随机化；参考 [Isaac PickPlace Locomanipulation G1 任务](https://isaac-sim.github.io/IsaacLab/) 的环境模板 |
| push / pull 推车 | 载荷变化 + 摩擦不确定 | domain randomization 载荷/摩擦；reward 用"物体移动速度"任务项 |
| 上下楼梯带物 | 感知（台阶）+ 载荷 + 平衡 | 感知进 observation（高程图）+ 载荷随机化 |

**通用配方（2026 社区共识）**：
- observation 加 **EE 位置/朝向目标**（任务空间量直接进策略，比关节空间目标好训）
- reward：locomotion 基项（速度跟踪）+ EE 跟踪项 + 平衡/姿态正则 + 接触惩罚（手不要乱碰）
- 训练基础设施：Isaac Lab（见 04 篇）+ rsl_rl；轻量验证用 mujoco_playground
- 先仿真全通 → 再考虑真机（G1 是社区最成熟的）

## 6.4 必读论文与代码（详见 08/09 篇）

- 综述：[Humanoid Locomotion and Manipulation（arXiv 2501.02116）](https://arxiv.org/abs/2501.02116) —— 先读这张地图
- 学习式 WBC：[DWBC 2022](https://arxiv.org/abs/2210.10044)（统一策略原型，停更但必读）、[Expressive WBC 2024](https://arxiv.org/abs/2402.16796)
- 全身跟踪（数据→技能）：[HOVER](https://arxiv.org/abs/2410.21229)、[ExBody2](https://arxiv.org/abs/2412.13196)、[SONIC](https://arxiv.org/abs/2511.07820)
- sim2real：[ASAP](https://arxiv.org/abs/2502.01143)
- 现成环境：**Isaac Lab 的 `Isaac-PickPlace-Locomanipulation-G1-Abs-v0`**（[路径见 04 篇](04-isaac-lab.md)）+ isaaclab_mimic 的 locomanipulation_g1

## 6.5 Stage 5 · Milestone

**目标：训练 humanoid 完成 walk → reach → grasp → carry（sim，G1）**

```
Week 10:
  D1–2  跑通 Isaac Lab 的 PickPlace-Locomanipulation-G1 环境，观察默认行为
  D3–4  读它的 reward/observation 配置：EE 目标怎么进策略、怎么切换任务
  D5–7  改任务：换成"walking while maintaining EE target"（砍掉抓取，只保 EE 跟踪）
Week 11:
  D1–3  加"边走边搬运"载荷随机化，训练到稳定
  D4–5  完整 walk→reach→grasp→carry 课程（如时间紧，用现成 G1 环境+改 reward）
  D6–7  分析实验：手臂 reward 权重 vs 步态质量的关系；写实验报告
```

**Milestone 验证**：
- [ ] G1 在 sim 中稳定完成"走到桌子→伸手→抓→搬运→放下"（成功率 ≥ 70%）
- [ ] 能定量说明：去掉 EE 跟踪 reward 后，搬运时步态/平衡如何退化
- [ ] 能画出你的系统架构图并解释为什么选这条路线（A/B/C）
- [ ] 能说出"载荷 +50% 时策略为什么需要重新训练或随机化"

**可以跳过**：接触丰富操作（双手精细装配）的完整实现、多接触攀爬、真机部署（G1 真机作为后续扩展）。
