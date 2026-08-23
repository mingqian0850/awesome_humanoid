# 📄 论文 (Papers)

> 人形机器人 / 全身控制（WBC）方向论文，按时间线组织：**综述 → 经典时期（~2009）→ 2010s → 2020s**。
> 所有条目均经核实并附可点击链接（DOI / arXiv / 开放获取）。有中文一句话说明。

## 📋 综述 (Surveys)

- **Learning-Based Legged Locomotion; State of the Art and Future Perspectives** — S. Ha et al., *arXiv:2406.01152*, 2024. [arXiv](https://arxiv.org/abs/2406.01152) — 基于学习的腿足运动控制最全面综述（硬件、学习框架、基准）。
- **Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning** — Z. Gu et al. (18 位作者), *arXiv:2501.02116*, 2025. [arXiv](https://arxiv.org/abs/2501.02116) — 人形运动与操控在控制/规划/学习三路线的最新进展综述。
- **Model Predictive Control of Legged and Humanoid Robots: Models and Algorithms** — S. Katayama, M. Murooka, Y. Tazaki, *Advanced Robotics* 37(5):298–315, 2023. [DOI](https://doi.org/10.1080/01691864.2023.2168134) — 腿足与人形机器人 MPC 建模与算法综述。
- **A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots** — M. Yuan et al., *arXiv:2506.20487*, 2025. [arXiv](https://arxiv.org/abs/2506.20487) — 面向人形全身控制的行为基础模型综述。
- **Whole-Body Control of Humanoid Robots: Past, Present, and Future** — A. Del Prete et al., *IEEE Robotics & Automation Magazine*（HAL 开放版）, 2022. [HAL](https://inria.hal.science/hal-02456663v1) — WBC 发展脉络权威综述，建议作为入门第一读。


## 🕰 经典时期 1960s–2009：ZMP / LIPM / 操作空间 / 全身控制起源

### 1970s

- **On the Stability of Anthropomorphic Systems** — M. Vukobratović, J. Stepanenko, *Mathematical Biosciences*, 1972. [DOI](https://doi.org/10.1016/0025-5564(72)90061-2) — 提出零力矩点（ZMP）概念与双足稳定性判据，奠定此后数十年双足步态控制的基石。

### 1980s

- **Dynamic Walk of a Biped** — H. Miura, I. Shimoyama, *The International Journal of Robotics Research*, 1984. [DOI](https://doi.org/10.1177/027836498400300206) — BIPER 系列双足机器人的动态行走研究，早期动态双足步行代表作。
- **Experiments in Balance with a 3D One-Legged Hopping Machine** — M. Raibert, H. Brown, M. Chepponis, *The International Journal of Robotics Research*, 1984. [DOI](https://doi.org/10.1177/027836498400300207) — 三维单腿跳跃机器人动态平衡实验，确立腿部动态平衡控制的经典框架。
- **Control of a Dynamical Biped Locomotion System for Steady Walking** — J. Furusho, M. Masubuchi, *Journal of Dynamic Systems, Measurement, and Control*, 1986. [DOI](https://doi.org/10.1115/1.3143752) — 线性化模型 + 反馈控制的早期动态双足稳态行走。
- **A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation** — O. Khatib, *IEEE Journal on Robotics and Automation*, 1987. [DOI](https://doi.org/10.1109/JRA.1987.1087068) — 操作空间（operational space）公式，全身控制的动力学理论基础。

### 1990s

- **Passive Dynamic Walking** — T. McGeer, *The International Journal of Robotics Research*, 1990. [DOI](https://doi.org/10.1177/027836499000900206) — 被动动态行走：无主动控制的双足可沿重力稳定下行，催生高效行走研究路线。
- **Realization of Dynamic Biped Walking Stabilized by Trunk Motion on a Sagittally Uneven Surface** — A. Takanishi et al., *IEEE/RSJ IROS*, 1990. [DOI](https://doi.org/10.1109/IROS.1990.262408) — WL 系列双足机器人用躯干运动补偿 ZMP，实现不平地面动态行走。
- **Study of Dynamic Biped Locomotion on Rugged Terrain — Derivation and Application of the Linear Inverted Pendulum Mode** — S. Kajita, K. Tani, *IEEE ICRA*, 1991. [DOI](https://doi.org/10.1109/ROBOT.1991.131811) — **线性倒立摆模型（LIPM）首次提出**，将双足动力学简化为线性模型，成为步态生成的标准工具。
- **Dynamic Walking Control of a Biped Robot Along a Potential Energy Conserving Orbit** — S. Kajita et al., *IEEE Transactions on Robotics and Automation*, 1992. [DOI](https://doi.org/10.1109/70.149940) — 沿势能守恒轨道的动态行走控制。
- **Development of a Biped Walking Robot Compensating for Three-Axis Moment by Trunk Motion** — J. Yamaguchi, A. Takanishi, I. Kato, *IEEE/RSJ IROS*, 1993. [DOI](https://doi.org/10.1109/IROS.1993.583168) — 躯干运动补偿三轴力矩，ZMP 补偿控制早期实践。
- **Experimental Study of Biped Dynamic Walking in the Linear Inverted Pendulum Mode** — S. Kajita, K. Tani, *IEEE ICRA*, 1995. [DOI](https://doi.org/10.1109/ROBOT.1995.525693) — LIPM 的硬件实验验证。
- **The Development of Honda Humanoid Robot** — K. Hirai et al., *IEEE ICRA*, 1998. [DOI](https://doi.org/10.1109/ROBOT.1998.677288) — 本田 P2/P3 人形机器人：首个自主行走的全尺寸人形平台。
- **Postural Stability of Biped Robots and the Foot-Rotation Indicator (FRI) Point** — A. Goswami, *The International Journal of Robotics Research*, 1999. [DOI](https://doi.org/10.1177/02783649922066376) — 提出足旋转指示点（FRI），分析 ZMP 之外的姿态稳定边界。

### 2000s

- **The 3D Linear Inverted Pendulum Mode: A Simple Modeling for a Biped Walking Pattern Generation** — S. Kajita et al., *IEEE/RSJ IROS*, 2001. [DOI](https://doi.org/10.1109/IROS.2001.973365) — 将 LIPM 推广到三维，实现人形 3D 实时步态模式生成。
- **Footstep Planning Among Obstacles for Biped Robots** — J. Kuffner et al., *IEEE/RSJ IROS*, 2001. [DOI](https://doi.org/10.1109/IROS.2001.973406) — 避障落脚点规划，连接高层导航与 ZMP 步态生成。
- **Real-Time Humanoid Motion Generation Through ZMP Manipulation Based on Inverted Pendulum Control** — S. Sugihara et al., *IEEE ICRA*, 2002. [DOI](https://doi.org/10.1109/ROBOT.2002.1014740) — 倒立摆控制实时操控 ZMP，反应式平衡经典方案。
- **The Intelligent ASIMO: System Overview and Integration** — Y. Sakagami et al., *IEEE/RSJ IROS*, 2002. [DOI](https://doi.org/10.1109/IRDS.2002.1041641) — 本田智能型 ASIMO 系统总览。
- **Whole-Body Cooperative Balancing of Humanoid Robot Using COG Jacobian** — S. Sugihara, Y. Nakamura, *IEEE/RSJ IROS*, 2002. [DOI](https://doi.org/10.1109/IRDS.2002.1041658) — 质心雅可比（COG Jacobian）全身协同平衡控制，全身平衡早期代表作。
- **Online Generation of Humanoid Walking Motion Based on a Fast Generation Method of Motion Pattern That Follows Desired ZMP** — K. Nishiwaki et al., *IEEE/RSJ IROS*, 2002. [DOI](https://doi.org/10.1109/IRDS.2002.1041675) — 快速生成跟随期望 ZMP 的运动模式，实现在线行走生成。
- **Biped Walking Pattern Generation by Using Preview Control of Zero-Moment Point** — S. Kajita et al., *IEEE ICRA*, 2003. [DOI](https://doi.org/10.1109/ROBOT.2003.1241826) — ZMP 预览控制，利用未来参考输入大幅改善步态跟踪，成为步行生成事实标准。
- **Resolved Momentum Control: Humanoid Motion Planning Based on the Linear and Angular Momentum** — S. Kajita et al., *IEEE/RSJ IROS*, 2003. [DOI](https://doi.org/10.1109/IROS.2003.1248880) — 动量分解控制：以线/角动量为全身运动规划与跟踪量，开启动量类 WBC 路线。
- **Dynamics Filter — Concept and Implementation of Online Motion Generator for Human Figures** — K. Yamane, Y. Nakamura, *IEEE Transactions on Robotics and Automation*, 2003. [DOI](https://doi.org/10.1109/TRA.2003.810579) — 动力学滤波器：将运动学目标实时投影到动力学可行空间。
- **Hybrid Zero Dynamics of Planar Biped Walkers** — E. R. Westervelt, J. W. Grizzle, D. E. Koditschek, *IEEE Transactions on Automatic Control*, 2003. [DOI](https://doi.org/10.1109/TAC.2002.806653) — 混合零动力学（HZD）框架，虚拟约束系统化设计平面双足动态步态。
- **Humanoid Robot HRP-2** — K. Kaneko et al., *IEEE ICRA*, 2004. [DOI](https://doi.org/10.1109/ROBOT.2004.1307969) — HRP-2 平台：全身控制算法研究与实验的标准硬件。
- **Whole-Body Dynamic Behavior and Control of Human-Like Robots** — O. Khatib et al., *International Journal of Humanoid Robotics*, 2004. [DOI](https://doi.org/10.1142/S0219843604000058) — 将操作空间控制扩展到人形机器人的全身动态行为框架。
- **Zero-Moment Point — Thirty Five Years of Its Life** — M. Vukobratović, B. Borovac, *International Journal of Humanoid Robotics*, 2004. [DOI](https://doi.org/10.1142/S0219843604000083) — ZMP 概念权威综述，系统梳理三十五年发展。
- **Efficient Bipedal Robots Based on Passive-Dynamic Walkers** — S. Collins et al., *Science*, 2005. [DOI](https://doi.org/10.1126/science.1107799) — 基于被动动态行走的高效双足机器人，能耗接近人类。
- **Synthesis of Whole-Body Behaviors Through Hierarchical Control of Behavioral Primitives** — L. Sentis, O. Khatib, *International Journal of Humanoid Robotics*, 2005. [DOI](https://doi.org/10.1142/S0219843605000594) — 优先级分层控制综合多个行为基元，全身行为合成早期核心论文。
- **A Whole-Body Control Framework for Humanoids Operating in Human Environments** — L. Sentis, O. Khatib, *IEEE ICRA*, 2006. [DOI](https://doi.org/10.1109/ROBOT.2006.1642100) — 操作空间全身控制框架，为任务与平衡控制提供统一方法。
- **A Universal Stability Criterion of the Foot Contact of Legged Robots — adios ZMP** — H. Hirukawa et al., *IEEE ICRA*, 2006. [DOI](https://doi.org/10.1109/ROBOT.2006.1641995) — 将 ZMP 推广到任意脚接触构型的通用稳定判据。
- **Trajectory Free Linear Model Predictive Control for Stable Walking in the Presence of Strong Perturbations** — P.-B. Wieber, *IEEE-RAS Humanoids*, 2006. [DOI](https://doi.org/10.1109/ICHR.2006.321375) — 线性 MPC 直接在线生成稳定步行，现代 MPC 步态控制源头。
- **Experimentation of Humanoid Walking Allowing Immediate Modification of Foot Place Based on Analytical Solution** — M. Morisawa et al., *IEEE ICRA*, 2007. [DOI](https://doi.org/10.1109/ROBOT.2007.364091) — 解析解即时修改落脚点补偿扰动，落脚点调节早期代表作。
- **Full-Body Compliant Human–Humanoid Interaction: Balancing in the Presence of Unknown External Forces** — S.-H. Hyon, J. G. Hale, G. Cheng, *IEEE Transactions on Robotics*, 2007. [DOI](https://doi.org/10.1109/TRO.2007.904896) — 全身柔顺/阻抗控制下的鲁棒平衡，未知外力人机交互代表作。
- **Honda Humanoid Robots Development** — M. Hirose, K. Ogawa, *Philosophical Transactions of the Royal Society A*, 2007. [DOI](https://doi.org/10.1098/rsta.2006.1917) — 本田人形机器人（P1 至 ASIMO）二十年发展综述。

## 🏗 2010s：Atlas 时代 · QP 全身控制 · MPC 步态 · 质心动量控制

### 2010

- **Online Walking Motion Generation with Automatic Footstep Placement** — A. Herdt et al., *Advanced Robotics* 24(5–6):719–737, 2010. [DOI](https://doi.org/10.1163/016918610X493552) — 把落脚点作为决策变量纳入线性 MPC，在线生成步态并自动调整落脚点。
- **Dynamic Balance Force Control for Compliant Humanoid Robots** — B. J. Stephens, C. G. Atkeson, *IEEE/RSJ IROS*, 2010. [DOI](https://doi.org/10.1109/IROS.2010.5648837) — 基于力控制的动态平衡框架，推力扰动下用踝/髋策略维持稳定。

### 2011

- **Bipedal Walking Control Based on Capture Point Dynamics** — J. Englsberger et al., *IEEE/RSJ IROS*, 2011. [DOI](https://doi.org/10.1109/IROS.2011.6094435) — 提出 Capture Point（捕获点）动力学与反馈控制，DCM 方向起点。
- **Operational Space Control of Constrained and Underactuated Systems** — M. Mistry, L. Righetti, *Robotics: Science and Systems (RSS)*, 2011. [DOI](https://doi.org/10.15607/RSS.2011.VII.031) — 受约束/欠驱动系统操作空间控制的统一理论，全身任务空间动力学基础。

### 2012

- **Capturability-Based Analysis and Control of Legged Locomotion, Part 1: Theory and Application to Three Simple Gait Models** — T. Koolen et al., *The International Journal of Robotics Research*, 2012. [DOI](https://doi.org/10.1177/0278364912452673) — 正式化"可捕获性"（capturability）与 N 步可捕获区域理论。
- **Capturability-Based Analysis and Control of Legged Locomotion, Part 2: Application to M2V2, a Lower-Body Humanoid** — J. Pratt et al., *The International Journal of Robotics Research*, 2012. [DOI](https://doi.org/10.1177/0278364912452762) — 捕获点/可捕获性控制实装到 M2V2 下半身人形。
- **A Momentum-Based Balance Controller for Humanoid Robots on Non-Level and Non-Stationary Ground** — S.-H. Lee, A. Goswami, *Autonomous Robots* 32(4), 2012. [DOI](https://doi.org/10.1007/s10514-012-9294-z) — 基于质心动量的平衡控制器，适用于非水平、非静止支撑面。
- **Balance Control Based on Capture Point Error Compensation for Biped Walking on Uneven Terrain** — M. Morisawa et al., *IEEE-RAS Humanoids*, 2012. [DOI](https://doi.org/10.1109/HUMANOIDS.2012.6651601) — 捕获点误差补偿实现不平整地形双足行走（HRP-2 系列）。

### 2013

- **Centroidal Dynamics of a Humanoid Robot** — D. E. Orin, A. Goswami, S.-H. Lee, *Autonomous Robots* 35(1):1–20, 2013. [DOI](https://doi.org/10.1007/s10514-013-9341-4) — 系统提出质心动力学与质心动量矩阵，全身控制/运动规划的基石模型。
- **Dynamic Whole-Body Motion Generation Under Rigid Contacts and Other Unilateral Constraints** — L. Saab et al., *IEEE Transactions on Robotics* 29(2):346–362, 2013. [DOI](https://doi.org/10.1109/TRO.2012.2234351) — 刚性接触 + 摩擦锥单边约束下的 QP 全身运动生成，HRP-2 验证。
- **Generation of Dynamic Humanoid Behaviors Through Task-Space Control with Conic Optimization** — P. M. Wensing, D. E. Orin, *IEEE ICRA*, 2013. [DOI](https://doi.org/10.1109/ICRA.2013.6631008) — 质心动量任务 + 锥优化的任务空间全身控制。
- **High-Speed Humanoid Running Through Control with a 3D-SLIP Model** — P. M. Wensing, D. E. Orin, *IEEE/RSJ IROS*, 2013. [DOI](https://doi.org/10.1109/IROS.2013.6697099) — 3D-SLIP 模板模型控制实现高速仿人奔跑。
- **Three-Dimensional Bipedal Walking Control Using Divergent Component of Motion** — J. Englsberger et al., *IEEE/RSJ IROS*, 2013. [DOI](https://doi.org/10.1109/IROS.2013.6696723) — 把 DCM 推广到三维（IROS 2013 版）。
- **Implementation and Stability Analysis of Prioritized Whole-Body Compliant Controllers on a Wheeled Humanoid Robot in Uneven Terrains** — L. Sentis et al., *Autonomous Robots* 35(4):301–319, 2013. [DOI](https://doi.org/10.1007/s10514-013-9358-8) — 优先序全身柔顺控制器的实现与稳定性分析。

### 2014

- **An Efficiently Solvable Quadratic Program for Stabilizing Dynamic Locomotion** — S. Kuindersma, F. Permenter, R. Tedrake, *IEEE ICRA*, 2014. [arXiv](https://arxiv.org/abs/1311.1839) — Atlas 平衡核心：LQR + 高效 QP 全身力矩分配。
- **Balancing Experiments on a Torque-Controlled Humanoid with Hierarchical Inverse Dynamics** — A. Herzog et al., *IEEE/RSJ IROS*, 2014. [arXiv](https://arxiv.org/abs/1305.2042) — 力矩控制人形（J2）上的分层逆动力学（HID）平衡实验。
- **Human-Inspired Control of Bipedal Walking Robots** — A. D. Ames et al., *IEEE Transactions on Automatic Control* 59(5):1115–1130, 2014. [DOI](https://doi.org/10.1109/TAC.2014.2299342) — 基于人类步态数据的混合零动力学（HZD）控制。
- **Whole-Body Motion Planning with Centroidal Dynamics and Full Kinematics** — H. Dai, A. Valenzuela, R. Tedrake, *IEEE-RAS Humanoids*, 2014. [DOI](https://doi.org/10.1109/HUMANOIDS.2014.7041375) — 质心动力学 + 全身运动学的直接转置全身运动规划。

### 2015

- **Optimization-Based Full Body Control for the DARPA Robotics Challenge** — S. Feng et al., *Journal of Field Robotics* 32(8):1081–1099, 2015. [DOI](https://doi.org/10.1002/rob.21559) — CMU Atlas 力矩级 QP 全身控制，DRC 实战验证。
- **Team IHMC's Lessons Learned from the DARPA Robotics Challenge Trials** — M. Johnson et al., *Journal of Field Robotics* 32(2):192–208, 2015. [DOI](https://doi.org/10.1002/rob.21571) — IHMC 全身控制与平衡策略经验总结。
- **Prioritized Motion–Force Control of Constrained Fully-Actuated Robots: "Task Space Inverse Dynamics"** — A. Del Prete et al., *Robotics and Autonomous Systems* 63(2):150–157, 2015. [arXiv](https://arxiv.org/abs/1410.3863) — 提出 TSID（任务空间逆动力学），开源 TSID 库的理论来源。
- **iCub Whole-Body Control Through Force Regulation on Rigid Non-Coplanar Contacts** — F. Nori et al., *Frontiers in Robotics and AI*, 2015. [DOI](https://doi.org/10.3389/frobt.2015.00006) — iCub 整身控制：刚性非共面接触上的力调节全身力矩控制。
- **Whole-Body Model-Predictive Control Applied to the HRP-2 Humanoid** — J. Koenemann et al., *IEEE/RSJ IROS*, 2015. [DOI](https://doi.org/10.1109/IROS.2015.7353843) — 全身 MPC 实际部署到 HRP-2 并实验验证。
- **Continuous Humanoid Locomotion over Uneven Terrain Using Stereo Fusion** — M. Fallon et al., *IEEE-RAS Humanoids*, 2015. [DOI](https://doi.org/10.1109/HUMANOIDS.2015.7363465) — Atlas 非结构化地形连续行走：立体视觉 + 落脚点规划 + 全身控制。
- **Three-Dimensional Bipedal Walking Control Based on Divergent Component of Motion** — J. Englsberger et al., *IEEE Transactions on Robotics* 31(2):355–368, 2015. [DOI](https://doi.org/10.1109/TRO.2015.2405592) — 3D DCM 期刊扩展版（含捕获点/落脚点调节与稳定性分析）。

### 2016

- **Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot** — S. Kuindersma et al., *Autonomous Robots* 40(3):429–455, 2016. [DOI](https://doi.org/10.1007/s10514-015-9479-3) — MIT Atlas 系统论文：落脚点规划 + 状态估计 + 全身 QP 控制一体化。
- **Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid** — A. Herzog et al., *Autonomous Robots* 40(3):473–491, 2016. [arXiv](https://arxiv.org/abs/1410.7284) — 质心动量控制 + 分层逆动力学结合的鲁棒平衡。

### 2017

- **The DARPA Robotics Challenge Finals: Results and Perspectives** — E. Krotkov et al., *Journal of Field Robotics* 34(2):229–240, 2017. [DOI](https://doi.org/10.1002/rob.21683) — DRC 决赛官方总结。

### 2018

- **Multicontact Locomotion of Legged Robots** — J. Carpentier, N. Mansard, *IEEE Transactions on Robotics* 34(6):1441–1460, 2018. [DOI](https://doi.org/10.1109/TRO.2018.2862902) — 多接触（双手双脚）运动规划/控制完整框架。

### 2019

- **Stair Climbing Stabilization of the HRP-4 Humanoid Robot Using Whole-Body Admittance Control** — S. Caron, A. Kheddar, O. Tempier, *IEEE ICRA*, 2019. [arXiv](https://arxiv.org/abs/1809.07073) — 全身导纳控制实现 HRP-4 爬楼梯稳定。

## 🧠 2020s：深度强化学习 · 遥操作与示教 · 人形基础模型 / VLA

### 2019

- **Learning Agile and Dynamic Motor Skills for Legged Robots** — J. Hwangbo et al., *Science Robotics* 4(26):eaau5872, 2019. [arXiv](https://arxiv.org/abs/1901.08652) — 首次用大规模并行 RL 在真实四足机器人上训练出敏捷鲁棒的运动技能，足式学习控制里程碑。

### 2020

- **Learning Quadrupedal Locomotion over Challenging Terrain** — J. Lee et al., *Science Robotics* 5(47):eabc5986, 2020. [arXiv](https://arxiv.org/abs/2010.11251) — teacher-student 特权学习 + 高程感知，确立 sim-to-real 经典范式。
- **Learning Agile Robotic Locomotion Skills by Imitating Animals** — X. B. Peng et al., *RSS*, 2020. [arXiv](https://arxiv.org/abs/2004.00784) — 从动物运动捕捉数据模仿学习（AMP 前身）。
- **Learning Memory-Based Control for Human-Scale Bipedal Locomotion** — J. Siekmann et al., *RSS*, 2020. [arXiv](https://arxiv.org/abs/2006.02402) — 基于 RNN 记忆的 Cassie 双足策略，无外部状态估计长时间稳定行走。

### 2021

- **Learning to Jump from Pixels** — G. B. Margolis et al., *CoRL*, 2021. [arXiv](https://arxiv.org/abs/2110.15344) — 仅用真实像素观测在线训练四足跳跃，无需仿真预训练。

### 2022

- **Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning** — N. Rudin et al., *CoRL*, 2022. [arXiv](https://arxiv.org/abs/2109.11978) — GPU 大规模并行仿真把足式运动训练压缩到数分钟，现代 sim-to-real RL 基础设施。
- **Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild** — T. Miki et al., *Science Robotics* 7(62):eabk2822, 2022. [arXiv](https://arxiv.org/abs/2201.08117) — 特权学习 + 高程图感知，野外复杂地形稳健行走。
- **Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion** — Z. Fu et al., *CoRL* (Oral), 2022. [arXiv](https://arxiv.org/abs/2210.10044) — 单一 RL 策略统一带臂足式机器人的移动与操作。

### 2023

- **Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition** — H. Ha et al., *CoRL*, 2023. [arXiv](https://arxiv.org/abs/2307.14535) — 大规模演示蒸馏为语言引导技能，VLA 数据与训练思路代表作（通用机器人）。

### 2024

- **Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning** — T. Haarnoja et al., *Science Robotics* 9(89):eadi8022, 2024. [arXiv](https://arxiv.org/abs/2304.13653) — 深度 RL 让小型双足机器人学会完整足球技能。
- **Real-World Humanoid Locomotion with Reinforcement Learning** — I. Radosavovic et al., *Science Robotics* 9(89):eadi9579, 2024. [arXiv](https://arxiv.org/abs/2303.03381) — 在真实 Digit 人形上直接训练 RL 行走策略，免仿真迁移。
- **Humanoid Locomotion as Next Token Prediction** — I. Radosavovic et al., *NeurIPS*, 2024. [arXiv](https://arxiv.org/abs/2402.19469) — 将运动控制建模为下一 token 预测，单一 transformer 策略实现多种动态运动。
- **Expressive Whole-Body Control for Humanoid Robots** — X. Cheng et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2402.16796) — 从人类运动视频学运动先验，让 Unitree H1 实现流畅自然的全身运动。
- **Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer** — X. Gu et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2404.05695) — 面向 Unitree/DeepRobotics 人形的开源 RL 训练框架，零样本 sim2real。
- **OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning** — T. He et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2406.08858) — 通用人-人形全身遥操作与学习框架（VR/视频驱动）。
- **HumanPlus: Humanoid Shadowing and Imitation from Humans** — Z. Fu et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2406.10454) — 人形影子跟随学习人类动作 + 自主 RL 完成双手机器人任务。
- **Open-TeleVision: Teleoperation with Immersive Active Visual Feedback** — X. Cheng et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2407.01512) — 立体视觉 + 头戴式沉浸反馈的远距离遥操作。
- **HPT: Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers** — L. Wang et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2409.20537) — 跨多种机器人/传感器预训练的 transformer 骨干（HPT 实为 Heterogeneous Pre-trained Transformers）。
- **π0: A Vision-Language-Action Flow Model for General Robot Control** — K. Black et al., arXiv 2024（*RSS* 2025 接收）. [arXiv](https://arxiv.org/abs/2410.24164) — flow matching 的 VLA 基础模型，Physical Intelligence 出品（通用机器人）。
- **ExBody2: Advanced Expressive Humanoid Whole-Body Control** — M. Ji et al., arXiv, 2024. [arXiv](https://arxiv.org/abs/2412.13196) — 全身控制器 + 条件扩散模型，从视频学习自然全身动作。
- **Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion** — T. He et al., *RSS*, 2024. [arXiv](https://arxiv.org/abs/2401.17583) — 学习式安全滤波器实现高速碰撞规避。
- **Cafe-MPC: A Cascaded-Fidelity Model Predictive Control Framework with Tuning-Free Whole-Body Control** — H. Li et al., arXiv（投稿 IEEE T-RO）, 2024. [arXiv](https://arxiv.org/abs/2403.03995) — 级联精度 MPC + 免调参全身控制。
- **Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control** — Z. Li et al., *IJRR*, 2024. [arXiv](https://arxiv.org/abs/2401.16889) — 双历史输入架构的端到端 RL，实现行走、跑步、跳跃、站立等动态技能。

### 2025

- **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** — NVIDIA 等, arXiv, 2025. [arXiv](https://arxiv.org/abs/2503.14734) — 首个开源通用人形基础模型，双系统架构 + 大规模多形态训练。
- **DreamPolicy: A Unified World-model Policy for Scalable Humanoid Locomotion** — Y. Fan et al., arXiv, 2025. [arXiv](https://arxiv.org/abs/2505.18780) — 统一世界模型策略，人形运动学习跨形态、跨任务扩展（清华）。
- **Humanoid World Models: Open World Foundation Models for Humanoid Robotics** — M. Q. Ali et al., arXiv, 2025. [arXiv](https://arxiv.org/abs/2506.01182) — 面向人形机器人的开放世界模型基础模型。
- **LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction** — H. Xue et al., arXiv, 2025. [arXiv](https://arxiv.org/abs/2506.13751) — 潜在视觉-语言指令驱动人形全身控制，衔接 VLA 与全身运动策略。
