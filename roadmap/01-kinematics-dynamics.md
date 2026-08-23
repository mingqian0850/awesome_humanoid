# 01 · 机器人运动学与动力学（Robot Kinematics & Dynamics）

> 定位：这是**所有后续内容的地基**，但不是"传统机器人理论课"。目标是够用且理解物理含义，而不是推导证明。
> 时间预算：1–1.5 周（穿插在 12 周计划 Week 1–2），20–30% 理论 + 70–80% 代码（Pinocchio/MuJoCo 练习）。

## 1.1 内容分级（先看这个）

### 🔴 必须真正掌握（会推导、会写代码）

| 主题 | 为什么必须掌握 | 掌握标准 |
|---|---|---|
| Rotation Matrix / Quaternion / SO(3) / SE(3) | 全身控制所有代码都是刚体变换运算，出错基本都在这里 | 能手写 R→quat 转换、SE(3) 组合、Jacobian 的旋转部分；知道左乘/右乘约定（local vs world frame） |
| Forward / Inverse Kinematics | 末端执行器（手/脚）位置 → 关节角，全身 IK 的核心 | 会用 Pinocchio `frames` / MuJoCo `mj_kinematics` 求 FK；理解解析 IK 与数值 IK（Levenberg-Marquardt）区别 |
| Jacobian / Differential Kinematics | 速度/力映射（$\dot{x}=J\dot{q}$，$\tau=J^T f$），WBC 的数学主干 | 会求几何 Jacobian、任务空间速度；理解 Jacobian 转置=力的映射 |
| Floating-base robot | 人形没有固定底座，6 个虚拟自由度，这是 humanoid 与机械臂的本质区别 | 理解 base pose/velocity 在广义坐标里的位置，浮动基座 vs 固定基座方程差异 |
| Rigid-body dynamics（EoM） | $M(q)\ddot{q}+C(q,\dot{q})\dot{q}+G(q)=\tau+J_c^T\lambda$，所有 WBC/ID 的起点 | 会用 Pinocchio `aba`/`rnnea` 算前向/逆向动力学；能写出含接触力的方程 |
| Mass matrix M / Coriolis C / Gravity G | 逆动力学、QP 约束、MPC 模型都要用 | 知道每一项的物理含义；会用库函数取出来 |
| Contact Jacobian & Friction cone | 接触约束是 humanoid 控制的灵魂（脚不滑动、摩擦锥内） | 理解 $J_c\dot{q}=0$（刚性接触）与锥约束 $\sqrt{f_x^2+f_y^2}\le\mu f_z$；会看 QP 里怎么写成线性/二阶锥约束 |
| Centroidal dynamics / CoM / Momentum | 人形平衡的本质：质心轨迹 + 角动量，ZMP/MPC 都建立在它上面 | 理解质心动量矩阵 $A_G$；能解释 $h_G = A_G \dot{q}$；知道"质心动力学"把全身动力学投影到 6 维 |
| ZMP / support polygon | 经典步态与平衡的判据，所有 MPC 步态论文的术语基础 | 会算 ZMP，理解"ZMP 在支撑多边形内=静态/动态稳定"的直觉与局限 |

### 🟡 只需要理解概念（知道是什么、什么时候用）

| 主题 | 理解到什么程度 |
|---|---|
| 解析 IK（如 6-DoF 臂闭式解） | 知道存在即可；现代工作基本用数值/优化 IK |
| Lie group 形式化（SE(3) 流形、指数映射） | 理解 $SE(3)$ 是流形、$\dot{T}=T\hat\xi$ 的含义即可；不需要推导 BCH 公式 |
| 空间向量（spatial algebra，Featherstone） | 知道 Pinocchio/MuJoCo 底层用它加速即可，不必手推 |
| 能量/拉格朗日 vs 牛顿-欧拉推导 | 理解"两条路殊途同归"，会用库就行 |
| 欠驱动/欠约束系统（HZD 那套） | 了解混合零动力学存在即可；2025 年的主流是 RL/优化，不是纯 HZD 设计 |

### 🟢 humanoid loco-manipulation 中实际最常用的部分（高频）

1. **浮动基座 + 质心动力学**（MPC 步态、balance-aware manipulation 全部建立在这上面）
2. **Jacobian 全家桶**：手/脚的任务空间速度、全身运动学 Jacobian
3. **接触建模**：接触 Jacobian、摩擦锥（QP WBC 的约束主体）
4. **逆动力学（ID）**：WBC 的核心运算（TSID / hierarchical QP 都调 ID）
5. **PD 控制 + 关节空间控制**：RL policy 的底层执行器（`q_des → PD → τ`）
6. **动量/角动量控制**：全身平衡（Lee & Goswami 2012、Herzog 2016）

> 一句话：**你 90% 的日常代码在算 Jacobian、M/C/G、接触约束和 PD 命令**。不要把时间花在闭式 IK 推导或 HZD 稳定性证明上。

## 1.2 教材章节（按优先级）

1. **Modern Robotics**（Lynch & Park）— [免费在线版](http://hades.mech.northwestern.edu/index.php/Modern_Robotics)
   - Ch. 3 刚体运动（SE(3)、指数坐标）· Ch. 4 正运动学 · Ch. 5 速度运动学与 Jacobian · Ch. 6 逆运动学 · Ch. 8 动力学（浮动基座方程！）· Ch. 9 轨迹生成
   - 只读这 6 章，配合书末练习（有答案）
2. **Springer Handbook of Robotics** — [Ch. 48 Modeling and Control of Legged Robots](https://doi.org/10.1007/978-3-319-32552-1_48)（Wieber 执笔）：腿足机器人的动力学/步态/平衡全景
3. **Underactuated Robotics**（Tedrake）— [在线版](https://underactuated.mit.edu/)：Ch. 2–3 动力学与接触建模（浮动基座、接触、摩擦锥讲得非常清楚）
4. **Humanoid Robots: Modeling and Control**（Nenchev et al.）— 全书按需查阅（全身动力学建模最系统的专著）

## 1.3 Lecture / 视频

1. **ETH Robot Dynamics（Hutter）** — [公开录像](https://video.ethz.ch/lectures/d-mavt/2025/autumn/151-0851-00L)：前 8 讲覆盖刚体动力学、浮动基座、[Legged Robotics 专章](https://ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/rsl-dam/documents/RobotDynamics2017/8-leggedrobotics_ex.pdf)
2. **CMU 16-745 Optimal Control（Atkeson）** — [课程页](https://www.cs.cmu.edu/~cga/dynopt/)：Week 1–4 的动力学/轨迹优化部分
3. **KAIST Robot Dynamics（Hwangbo）** — [公开页](https://railab.kaist.ac.kr/sections/education.html)：ABA/CRBA/RNE 的工程实现视角（和 Pinocchio 源码对应着看）

## 1.4 代码实现与开源库（优先顺序）

| 库 | 用途 | 入口 |
|---|---|---|
| **Pinocchio**（[GitHub](https://github.com/stack-of-tasks/pinocchio)） | 首选。FK/IK/Jacobian/M/C/G/ABA/接触约束全有，Python API 简单，文档好 | 官方 [examples](https://github.com/stack-of-tasks/pinocchio/tree/master/examples)：`forward-kinematics.ipynb`、`inverse-kinematics.ipynb`、`dynamics.ipynb`、`contact-dynamics.ipynb`（都带可视化） |
| **MuJoCo**（[mujoco.org](https://mujoco.org/)） | 仿真为主，但也提供完整动力学 API（`mj_forward`、`mj_jac`） | [Python 教程](https://mujoco.readthedocs.io/)；对比 Pinocchio 的 FK/Jacobian 输出（数值一致性练习） |
| **Drake**（[drake.mit.edu](https://drake.mit.edu/)） | 优化/控制工具箱，数学库（`MultibodyPlant`） | [Tutorials](https://drake.mit.edu/doxygen_cxx/group__tutorials.html)（`multibody_plant.ipynb` 等） |
| **Isaac Lab**（[docs](https://isaac-sim.github.io/IsaacLab/)） | 训练环境（第 04 篇详述），资产里自带 H1/G1 的 articulation | 第 04 篇给出确切代码入口 |

**Stage 0 验证任务**（1–2 天）：
> 用 Pinocchio 加载 G1 或 H1 的 URDF（`unitree_ros2` 或 menagerie 模型），实现：① FK 求左手/右手/骨盆在世界系的位置；② 数值 Jacobian vs 解析 Jacobian 对比；③ 施加脚底接触约束求平衡逆动力学（ID）；④ 输出 M/C/G 矩阵并检查质量矩阵对称正定。全部做完，Stage 0 运动学部分即达标。

## 1.5 预计学习顺序（Stage 0）

```
Week 1:
  D1–2  SE(3)/旋转表示（Modern Robotics Ch.3）+ numpy 手写 R↔quat
  D3–4  FK/IK + Pinocchio 入门（官方 notebook 1–3）
  D5    Jacobian + 微分运动学（Ch.5）+ Pinocchio 练习
  D6–7  刚体动力学 EoM + M/C/G（Ch.8 浮动基座部分）+ Pinocchio dynamics notebook
Week 2（与 locomotion 并行）:
  D1–2  接触动力学/摩擦锥（Underactuated Ch.2–3 相关小节）
  D3    质心动力学 + ZMP（Wieber Handbook 章节）
  D4–5  验证任务（上述 4 步）完成
```

## 1.6 Checklist（自测）

- [ ] 能口头解释浮动基座方程与固定基座方程的差别，并指出代码里 base 6-DoF 在哪
- [ ] 用 Pinocchio 30 分钟内写出"FK + Jacobian + 逆动力学"流水线
- [ ] 能解释为什么 WBC 里"任务空间力 = Jᵀf"成立，以及摩擦锥为什么要进约束
- [ ] 能说清 ZMP 与 CoM 的关系、ZMP 判据的适用边界
- [ ] 能说出质心动量矩阵 A_G 的行列维度（6 × (n+6)）和它的用途

## 1.7 暂时可以跳过

- 闭式解析 IK（6-DoF 臂的几何解）
- HZD/混合系统稳定性证明（Westervelt 书的证明部分）
- 空间向量代数的手推（知道 Pinocchio 用了即可）
- 柔性体/柔顺关节动力学（除非做 SEA 硬件）
