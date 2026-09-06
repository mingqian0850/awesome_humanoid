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
## 🆕 2025–2026 最新进展：Humanoid Loco-Manipulation 专题

> 2026-08 通过 arXiv API 全量扫描（9 组关键词 × 40 条）筛选出的最新进展，与本仓库已有条目去重；标题/作者/日期均来自 arXiv 元数据。代码链接为已核实的官方/作者仓库（截至 2026-08 存在），未列出的不代表无代码。

### 🏭 学习式 Loco-Manipulation 系统

> 系统级：移动+操作的统一学习框架

- **FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences** — Omar Rayyan et al., arXiv 2026-08-17. [arXiv](https://arxiv.org/abs/2608.17027) [Code](https://github.com/omarrayyann/FetchMan) — 视觉人形 loco-manipulation 策略（仿真经验学习）
- **Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL** — Martin Schuck et al., arXiv 2026-08-12. [arXiv](https://arxiv.org/abs/2608.12063) — 从 SMPC 演示学习 loco-manipulation（离线到在线 RL）
- **LUCID: Latent-Skill Unified Control via Imagined Dynamics for Long-Horizon Humanoid Loco-Manipulation** — Cheng Guo et al., arXiv 2026-08-07. [arXiv](https://arxiv.org/abs/2608.07746) — LUCID：潜在技能统一控制（长时程人形 loco-manip）
- **$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation** — Zhe Li et al., arXiv 2026-08-06. [arXiv](https://arxiv.org/abs/2608.06375) — ω-0：潜在预测世界动作模型（并发 loco-manipulation）
- **Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition** — Fanxing Meng et al., arXiv 2026-07-31. [arXiv](https://arxiv.org/abs/2608.00208) — 交互表征 + 技能组合的移动操作
- **Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation** — Peng Ren et al., arXiv 2026-07-20. [arXiv](https://arxiv.org/abs/2607.18016) — 人形 VLA 闭环：3D 物体 token 可验证 loco-manipulation
- **VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes** — Yen-Jen Wang et al., arXiv 2026-06-29. [arXiv](https://arxiv.org/abs/2606.30645) — VLK：重建场景中合成交互学习人形 loco-manipulation
- **Humanoid-DART: Humanoid Loco-Manipulation using Diffusion-guided Augmentation through Relabeling and Tracking** — Pranav Debbad et al., arXiv 2026-06-25. [arXiv](https://arxiv.org/abs/2606.26855) [Code](https://github.com/pran-d/Humanoid-DART) — Humanoid-DART：扩散引导增强的 loco-manipulation
- **A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots** — Duncan William Calvert, arXiv 2026-06-24. [arXiv](https://arxiv.org/abs/2606.26425) — 快速、鲁棒、自适应的人形 loco-manipulation 行为系统
- **OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation** — Runyi Yu et al., arXiv 2026-06-24. [arXiv](https://arxiv.org/abs/2606.26201) — OmniContact：接触流链式元技能（通用 loco-manipulation）
- **WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning** — Melya Boukheddimi et al., arXiv 2026-06-24. [arXiv](https://arxiv.org/abs/2606.25591) — WOLF-VLA：全身最优运动 VLA 框架
- **CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation** — Sikai Li et al., arXiv 2026-06-22. [arXiv](https://arxiv.org/abs/2606.23680) [Code](https://github.com/Skevinci/coordex) — CoorDex：身体-手先验协调的灵巧 loco-manipulation
- **OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation** — Yingdong Hu et al., arXiv 2026-06-20. [arXiv](https://arxiv.org/abs/2606.22174) [Code](https://github.com/OpenHLM-project/OpenHLM) — OpenHLM：全身人形 loco-manipulation 开源配方
- **HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations** — Zehui Zhao et al., arXiv 2026-06-17. [arXiv](https://arxiv.org/abs/2606.18772) — HALOMI：主动感知 + 人类演示学习 loco-manipulation
- **MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation** — Jia Zheng et al., arXiv 2026-06-08. [arXiv](https://arxiv.org/abs/2606.09215) — MotionWAM：实时人形 loco-manipulation 世界动作模型
- **OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation** — Zehao Yu et al., arXiv 2026-06-07. [arXiv](https://arxiv.org/abs/2606.08548) [Code](https://github.com/TeleHuman/OASIS) — OASIS：仿真数据采集到真机 loco-manipulation
- **SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation** — Songlin Wei et al., arXiv 2026-06-06. [arXiv](https://arxiv.org/abs/2606.08278) [Code](https://github.com/physical-superintelligence-lab/SIMPLE) — SIMPLE：基于仿真的人形 loco-manipulation 策略学习与评估
- **HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers** — Lizhi Yang et al., arXiv 2026-06-04. [arXiv](https://arxiv.org/abs/2606.06493) — HANDOFF：蒸馏互补教师的智能体全身控制
- **MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation** — Ilyass Taouil et al., arXiv 2026-06-04. [arXiv](https://arxiv.org/abs/2606.06139) — MotionDisco：极端人形 loco-manipulation 动作发现
- **Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation** — Junheng Li et al., arXiv 2026-06-04. [arXiv](https://arxiv.org/abs/2606.05687) [Code](https://github.com/junhengl/mpc-rl) — MPC 引导 RL 的人形运动与操作（加速与规模化）
- **GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors** — Tianyi Xie et al., arXiv 2026-06-03. [arXiv](https://arxiv.org/abs/2606.05160) [Code](https://github.com/NVlabs/GRAIL) — GRAIL：从 3D 资产与视频先验生成 loco-manipulation
- **SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation** — Jeonguk Kang et al., arXiv 2026-06-02. [arXiv](https://arxiv.org/abs/2606.03297) — SplitAdapter：载荷感知的人形 loco-manipulation
- **HOIST: Humanoid Optimization with Imitation and Sample-efficient Tuning for Manipulating Suspended Loads** — Songyang Liu et al., arXiv 2026-05-29. [arXiv](https://arxiv.org/abs/2606.00252) — HOIST：悬挂载荷操作（模仿+样本高效微调）
- **HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning** — Kevin Lin et al., arXiv 2026-05-26. [arXiv](https://arxiv.org/abs/2605.27724) — HumanoidMimicGen：全身规划的 loco-manipulation 数据生成
- **Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum** — Zhizhao Liang et al., arXiv 2026-05-20. [arXiv](https://arxiv.org/abs/2605.21133) [Code](https://github.com/LeungChaos/Humanoid-Whole-Body-Manipulation-via-Active-Spatial-Brain-and-Generalizable-Action-Cerebellum) — 主动空间脑 + 可泛化动作小脑（全身操作）
- **SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework** — Tianshu Wu et al., arXiv 2026-05-19. [arXiv](https://arxiv.org/abs/2605.20373) — SUGAR：人视频驱动的可泛化 loco-manipulation 学习
- **CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation** — Xinyuan Luo et al., arXiv 2026-05-19. [arXiv](https://arxiv.org/abs/2605.19981) — CEER：柔顺末端+根部控制的统一接口
- **VOFA: Visual Object Goal Pushing with Force-Adaptive Control for Humanoids** — Zichao Hu et al., arXiv 2026-05-02. [arXiv](https://arxiv.org/abs/2605.01518) — VOFA：力自适应推动（视觉目标推物）
- **Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation** — John Z. Zhang et al., arXiv 2026-04-09. [arXiv](https://arxiv.org/abs/2604.08508) — Sumo：动态可泛化全身 loco-manipulation
- **HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation** — Shuanghao Bai et al., arXiv 2026-04-09. [arXiv](https://arxiv.org/abs/2604.07993) — HEX：人形对齐专家跨形态全身操作
- **AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning** — Huihua Zhao et al., arXiv 2026-03-20. [arXiv](https://arxiv.org/abs/2603.20147) [Code](https://github.com/nvidia-isaac/WBC-AGILE) — AGILE：人形 loco-manipulation 学习综合工作流（NVIDIA）
- **Cybo-Waiter: A Physical Agentic Framework for Humanoid Whole-Body Locomotion-Manipulation** — Peng Ren et al., arXiv 2026-03-11. [arXiv](https://arxiv.org/abs/2603.10675) — Cybo-Waiter：人形全身运动-操作智能体框架
- **FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid** — Niraj Pudasaini et al., arXiv 2026-03-09. [arXiv](https://arxiv.org/abs/2603.08961) — FAME：力自适应 RL 扩展全尺寸人形操作包络
- **Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids** — Hongjin Chen et al., arXiv 2026-03-03. [arXiv](https://arxiv.org/abs/2603.02856) — Rhythm：双人形交互式全身控制
- **Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations** — Ruiqian Nai et al., arXiv 2026-02-06. [arXiv](https://arxiv.org/abs/2602.06643) [Code](https://github.com/Richard-coder-Nai/HuMI) — 人形操作接口：无机器人演示的全身操作
- **Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning** — Chunxin Zheng et al., arXiv 2025-09-16. [arXiv](https://arxiv.org/abs/2509.13534) [Code](https://github.com/Chunx1nZHENG/Embracing-Bulky-Objects-with-Humanoid-Robots) — 拥抱笨重物体：RL 全身操作
- **TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning** — Jiacheng Liu et al., arXiv 2025-09-15. [arXiv](https://arxiv.org/abs/2509.11839) [Code](https://github.com/OpenHelix-Team/OpenTrajBooster) — TrajBooster：轨迹中心的人形全身操作
- **Scaling Whole-body Multi-contact Manipulation with Contact Optimization** — Victor Levé et al., arXiv 2025-08-18. [arXiv](https://arxiv.org/abs/2508.12980) — 接触优化的多接触全身操作扩展
- **TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality** — Masaki Murooka et al., arXiv 2025-06-18. [arXiv](https://arxiv.org/abs/2506.15146) — TACT：触觉模态的全身接触操作（深度模仿学习）
- **Autonomous Behavior Planning For Humanoid Loco-manipulation Through Grounded Language Model** — Jin Wang et al., arXiv 2024-08-15. [arXiv](https://arxiv.org/abs/2408.08282) — 接地语言模型的 loco-manipulation 自主行为规划
- **Plan-Guided Reinforcement Learning for Whole-Body Manipulation** — Mengchao Zhang et al., arXiv 2023-10-18. [arXiv](https://arxiv.org/abs/2310.12263) — 计划引导 RL 的全身操作（早期代表作）

### 🦾 全身控制与运动技能

> 运动层：WBC/步态/技能

- **GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction** — Ziyang Cheng et al., arXiv 2026-08-18. [arXiv](https://arxiv.org/abs/2608.18234) — GigaBrain-WBC-0.5：行为世界模型的鲁棒全身控制
- **Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control** — Yuan Jiang et al., arXiv 2026-07-06. [arXiv](https://arxiv.org/abs/2607.04837) — Athena-WBC：能力对齐策略专家的长尾全身控制
- **ReactiveBFM: Reactive Closed-Loop Motion Planning Towards Universal Humanoid Whole-Body Control** — Xiao Chen et al., arXiv 2026-06-29. [arXiv](https://arxiv.org/abs/2606.30362) — ReactiveBFM：反应式闭环运动规划（通用全身控制）
- **AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance** — Shuning Li et al., arXiv 2026-06-28. [arXiv](https://arxiv.org/abs/2606.29209) — AnyBody：任意关键点引导的自由形式全身控制
- **Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots** — Yumeng Liu et al., arXiv 2026-06-24. [arXiv](https://arxiv.org/abs/2606.25706) — 异步上半身任务空间轨迹跟踪策略
- **RGB: RL Guided Whole-Body MPPI for Humanoid Control** — Yunsoo Seo et al., arXiv 2026-06-23. [arXiv](https://arxiv.org/abs/2606.25123) — RGB：RL 引导的全身 MPPI 人形控制
- **OMG: Omni-Modal Motion Generation for Generalist Humanoid Control** — Siqiao Huang et al., arXiv 2026-06-09. [arXiv](https://arxiv.org/abs/2606.10340) — OMG：全模态运动生成（通用人形控制）
- **Mind Your Steps: A General Learning Framework for Accurate Humanoid Foothold Tracking** — Alessandro Montenegro et al., arXiv 2026-06-06. [arXiv](https://arxiv.org/abs/2606.08253) — 全身落脚点跟踪学习框架
- **LadderMan: Learning Humanoid Perceptive Ladder Climbing** — Siheng Zhao et al., arXiv 2026-06-04. [arXiv](https://arxiv.org/abs/2606.05873) — LadderMan：人形感知爬梯
- **M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking** — Zuxing Lu et al., arXiv 2026-06-03. [arXiv](https://arxiv.org/abs/2606.04829) — M3imic：多模态运动模仿的通用全身控制器
- **Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions** — Kwanwoo Lee et al., arXiv 2026-05-25. [arXiv](https://arxiv.org/abs/2605.25546) — 输入到状态安全控制屏障函数的全身控制
- **Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking** — Ming Yang et al., arXiv 2026-05-22. [arXiv](https://arxiv.org/abs/2605.23733) — Any2Any：跨形态高效迁移全身跟踪
- **Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control** — Haozhe Jia et al., arXiv 2026-05-14. [arXiv](https://arxiv.org/abs/2605.14417) — 语言条件人形控制的预期关节意图
- **RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting** — Yucheng Xin et al., arXiv 2026-04-23. [arXiv](https://arxiv.org/abs/2604.21355) — RPG：鲁棒策略门控（人形多技能平滑切换）
- **Switch: Learning Agile Skills Switching for Humanoid Robots** — Yuen-Fui Lau et al., arXiv 2026-04-16. [arXiv](https://arxiv.org/abs/2604.14834) — Switch：人形敏捷技能切换
- **Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control** — Shrutheesh R Iyer et al., arXiv 2026-04-14. [arXiv](https://arxiv.org/abs/2604.13323) — 流形约束运动规划向量化投影（实时全身控制）
- **SMASH: Mastering Scalable Whole-Body Skills for Humanoid Ping-Pong with Egocentric Vision** — Junli Ren et al., arXiv 2026-04-01. [arXiv](https://arxiv.org/abs/2604.01158) — SMASH：人形乒乓球全身技能（第一视角）
- **DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors** — Sudarshan Harithas et al., arXiv 2026-03-31. [arXiv](https://arxiv.org/abs/2604.00202) — DreamControl-v2：可训练引导扩散先验的自主人形技能
- **Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation Tasks** — Lequn Fu et al., arXiv 2026-03-15. [arXiv](https://arxiv.org/abs/2603.14308) — 工业搬运任务中的载荷感知运动控制
- **Kinodynamic Motion Retargeting for Humanoid Locomotion via Multi-Contact Whole-Body Trajectory Optimization** — Xiaoyu Zhang et al., arXiv 2026-03-10. [arXiv](https://arxiv.org/abs/2603.09956) — 多接触全身轨迹优化的运动重定向
- **Natural Humanoid Robot Locomotion with Generative Motion Prior** — Haodong Zhang et al., arXiv 2025-03-12. [arXiv](https://arxiv.org/abs/2503.09015) — 生成式运动先验的自然人形运动
- **Learning from Massive Human Videos for Universal Humanoid Pose Control** — Jiageng Mao et al., arXiv 2024-12-18. [arXiv](https://arxiv.org/abs/2412.14172) — 大规模人类视频学习通用人形姿态控制
- **Humanoid Parkour Learning** — Ziwen Zhuang et al., arXiv 2024-06-15. [arXiv](https://arxiv.org/abs/2406.10759) — Humanoid Parkour：人形跑酷学习
- **HumanMimic: Learning Natural Locomotion and Transitions for Humanoid Robot via Wasserstein Adversarial Imitation** — Annan Tang et al., arXiv 2023-09-25. [arXiv](https://arxiv.org/abs/2309.14225) — HumanMimic：Wasserstein 对抗模仿的自然运动与过渡

### 🧠 VLA / 语言-视觉-动作 × Humanoid

> 高层：VLA 与分层接口

- **EATR-Stereo: Embodiment-Aware Token Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control** — Songwei Wu et al., arXiv 2026-08-18. [arXiv](https://arxiv.org/abs/2608.17453) — EATR-Stereo：具身感知 token 路由的人形 VLA
- **HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL** — Langzhe Gu et al., arXiv 2026-08-17. [arXiv](https://arxiv.org/abs/2608.16837) — HAF：分层动作流 + 谱潜在 RL 的人形全身 loco-manip VLA
- **MotionVLA: Vision-Language-Action Model for Humanoid Motion** — Nonghai Zhang et al., arXiv 2026-06-13. [arXiv](https://arxiv.org/abs/2606.15142) — MotionVLA：人形运动的 VLA 模型
- **GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training** — Zhihai Bi et al., arXiv 2026-06-11. [arXiv](https://arxiv.org/abs/2606.12995) — GenHOI：接触感知人形-物体交互（生成视频模仿）
- **LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World** — Hojune Kim et al., arXiv 2026-05-31. [arXiv](https://arxiv.org/abs/2606.01458) — LEGS：免遥操作微调人形 loco-manipulation VLA
- **CLAW: Composable Language-Annotated Whole-body Motion Generation** — Jianuo Cao et al., arXiv 2026-04-13. [arXiv](https://arxiv.org/abs/2604.11251) — CLAW：可组合语言标注全身运动生成
- **DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA** — Yi Chen et al., arXiv 2026-03-31. [arXiv](https://arxiv.org/abs/2603.29844) — DIAL：潜在世界建模解耦意图与动作（端到端 VLA）
- **PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking** — Weikai Qin et al., arXiv 2026-03-05. [arXiv](https://arxiv.org/abs/2603.05410) — PhysiFlow：物理感知人形全身 VLA（多脑潜在流匹配）
- **Habilis-$β$: A Fast-Motion and Long-Lasting On-Device Vision-Language-Action Model** — Tommoro Robotics et al., arXiv 2026-02-21. [arXiv](https://arxiv.org/abs/2602.18813) — Habilis-β：端侧快速长时 VLA 模型（人形）
- **PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence** — Xiaopeng Lin et al., arXiv 2025-12-18. [arXiv](https://arxiv.org/abs/2512.16793) — PhysBrain：人类第一视角数据桥接 VLM 与物理智能
- **EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos** — Ruihan Yang et al., arXiv 2025-07-16. [arXiv](https://arxiv.org/abs/2507.12440) — EgoVLA：第一视角人类视频学习 VLA

### 📡 遥操作 · 数据采集 · 运动重定向

> 数据层：采集/重定向/跟踪

- **Teleopit: A Full-Embodiment Humanoid Teleoperation System** — Bingqian Wu et al., arXiv 2026-08-03. [arXiv](https://arxiv.org/abs/2608.01834) — Teleopit：全具身人形遥操作系统
- **Event-Based Upper-Body Humanoid Teleoperation Under Challenging Illumination** — Haoyu Fu et al., arXiv 2026-07-31. [arXiv](https://arxiv.org/abs/2607.29227) — 事件相机人形上身遥操作（恶劣光照）
- **Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning** — Nicolas Kosanovic et al., arXiv 2026-07-22. [arXiv](https://arxiv.org/abs/2607.20399) — 微型人形 VR+RL 遥 loco-manipulation
- **Handroid: Bridging Dexterous Hand and Humanoid** — Ruogu Li et al., arXiv 2026-07-17. [arXiv](https://arxiv.org/abs/2607.16187) — Handroid：灵巧手与人形桥接
- **Let the Body Follow: Coupled Egocentric Control for Whole-Body Robot Teleoperation** — Tsung-Chi Lin et al., arXiv 2026-07-17. [arXiv](https://arxiv.org/abs/2607.16095) — 身体跟随：耦合同心全身遥操作
- **HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum** — Chenxin Liu et al., arXiv 2026-07-02. [arXiv](https://arxiv.org/abs/2607.02332) — HEFT：重载荷全尺寸人形遥操作（载荷课程）
- **SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction** — Sirui Chen et al., arXiv 2026-06-25. [arXiv](https://arxiv.org/abs/2606.27581) — SceneBot：接触提示的全身跟踪（场景交互）
- **HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation** — Hongwu Wang et al., arXiv 2026-06-25. [arXiv](https://arxiv.org/abs/2606.27239) [Code](https://github.com/BAAI-AETHER/HumanoidUMI) — HumanoidUMI：免机器人演示的全身操作
- **X-OP: Cross-Morphology Whole-Body Teleoperation via MPC Retargeting** — Jen-Wei Wang et al., arXiv 2026-06-06. [arXiv](https://arxiv.org/abs/2606.07934) — X-OP：MPC 重定向的跨形态全身遥操作
- **Human2Humanoid: Physics-Aware Cross-Morphology Motion Retargeting for Humanoid Robots** — Tianchen Huang et al., arXiv 2026-06-02. [arXiv](https://arxiv.org/abs/2606.03476) — Human2Humanoid：物理感知跨形态运动重定向
- **Real-Time Whole-Body Teleoperation of a Humanoid Robot Using IMU-Based Motion Capture with Sim2Sim and Sim2Real Validation** — Hamza Ahmed Durrani et al., arXiv 2026-05-12. [arXiv](https://arxiv.org/abs/2605.12347) — IMU 动捕实时全身遥操作（sim2real 验证）
- **BifrostUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation** — Hongwu Wang et al., arXiv 2026-05-05. [arXiv](https://arxiv.org/abs/2605.03452) [Code](https://github.com/BAAI-AETHER/BifrostUMI) — BifrostUMI：桥接免机器人演示与全身操作
- **Safe Human-to-Humanoid Motion Imitation Using Control Barrier Functions** — Wenqi Cai et al., arXiv 2026-04-13. [arXiv](https://arxiv.org/abs/2604.11447) — 控制屏障函数的自然人-人形模仿
- **Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control** — Qingrui Zhao et al., arXiv 2026-03-23. [arXiv](https://arxiv.org/abs/2603.22201) — Make Tracking Easy：人形全身控制神经重定向
- **OmniClone: Engineering a Robust, All-Rounder Whole-Body Humanoid Teleoperation System** — Yixuan Li et al., arXiv 2026-03-15. [arXiv](https://arxiv.org/abs/2603.14327) — OmniClone：全能全身人形遥操作系统
- **ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control** — Ziyan Xiong et al., arXiv 2026-02-11. [arXiv](https://arxiv.org/abs/2602.11321) — ExtremControl：低延迟末端直接控制遥操作
- **EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration** — Modi Shi et al., arXiv 2026-02-10. [arXiv](https://arxiv.org/abs/2602.10106) [Code](https://github.com/OpenDriveLab/EgoHumanoid) — EgoHumanoid：野外免机器人第一视角演示
- **A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation** — Chuizheng Kong et al., arXiv 2026-02-02. [arXiv](https://arxiv.org/abs/2602.01632) — 上肢遥操作闭式几何重定向求解器
- **AdaMorph: Unified Motion Retargeting via Embodiment-Aware Adaptive Transformers** — Haoyu Zhang et al., arXiv 2026-01-12. [arXiv](https://arxiv.org/abs/2601.07284) — AdaMorph：具身感知自适应变换器统一重定向
- **World-Coordinate Human Motion Retargeting via SAM 3D Body** — Zhangzheng Tu et al., arXiv 2025-12-25. [arXiv](https://arxiv.org/abs/2512.21573) — SAM 3D 人体世界坐标运动重定向
- **CaFe-TeleVision: A Coarse-to-Fine Teleoperation System with Immersive Situated Visualization for Enhanced Ergonomics** — Zixin Tang et al., arXiv 2025-12-16. [arXiv](https://arxiv.org/abs/2512.14270) [Code](https://github.com/Zixin-Tang/CaFe-TeleVision) — CaFe-TeleVision：粗到细遥操作可视化
- **X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale** — Pei Yang et al., arXiv 2025-12-04. [arXiv](https://arxiv.org/abs/2512.04537) [Code](https://github.com/Open-X-Humanoid/TienKung-Lab) — X-Humanoid：人类视频人形化生成
- **TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System** — Yanjie Ze et al., arXiv 2025-11-04. [arXiv](https://arxiv.org/abs/2511.02832) — TWIST2：可扩展便携人形数据采集系统
- **EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations** — Justin Yu et al., arXiv 2025-10-31. [arXiv](https://arxiv.org/abs/2511.00153) — EgoMI：第一视角主动视觉+全身操作学习
- **From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance** — Zhe Li et al., arXiv 2025-10-16. [arXiv](https://arxiv.org/abs/2510.14952) — 从语言到运动：免重定向人形控制（运动潜在引导）
- **HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton** — Rui Zhong et al., arXiv 2025-10-03. [arXiv](https://arxiv.org/abs/2510.03022) — HumanoidExo：可穿戴外骨骼全身操作
- **Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking** — Joao Pedro Araujo et al., arXiv 2025-10-02. [arXiv](https://arxiv.org/abs/2510.02252) — Retargeting Matters：通用运动重定向
- **MoReFlow: Motion Retargeting Learning through Unsupervised Flow Matching** — Wontaek Kim et al., arXiv 2025-09-29. [arXiv](https://arxiv.org/abs/2509.25600) — MoReFlow：无监督流匹配运动重定向
- **A Scalable Whole-body Motion Transfer via Implicit Kinodynamic Motion Retargeting** — Xingyu Chen et al., arXiv 2025-09-18. [arXiv](https://arxiv.org/abs/2509.15443) — 隐式运动动力学重定向的全身运动迁移
- **A Whole-Body Motion Imitation Framework from Human Data for Full-Size Humanoid Robot** — Zhenghan Chen et al., arXiv 2025-08-01. [arXiv](https://arxiv.org/abs/2508.00362) — 全尺寸人形全身运动模仿框架
- **TWIST: Teleoperated Whole-Body Imitation System** — Yanjie Ze et al., arXiv 2025-05-05. [arXiv](https://arxiv.org/abs/2505.02833) [Code](https://github.com/YanjieZe/TWIST) — TWIST：遥操作全身模仿系统
- **Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids** — Toru Lin et al., arXiv 2025-02-27. [arXiv](https://arxiv.org/abs/2502.20396) — 人形视觉灵巧操作 sim-to-real RL
- **Embrace Collisions: Humanoid Shadowing for Deployable Contact-Agnostics Motions** — Ziwen Zhuang et al., arXiv 2025-02-03. [arXiv](https://arxiv.org/abs/2502.01465) — Embrace Collisions：碰撞无关动作的人形影子跟随
- **Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking** — Yun Liu et al., arXiv 2024-12-23. [arXiv](https://arxiv.org/abs/2412.17730) [Code](https://github.com/mimicking-bench/mimicking-bench.github.io) — Mimicking-Bench：人形-场景交互模仿基准
- **Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration** — Junjia Liu et al., arXiv 2024-12-19. [arXiv](https://arxiv.org/abs/2412.15166) — 分解对抗模仿的跨形态行为技能迁移
- **Redefining Data Pairing for Motion Retargeting Leveraging a Human Body Prior** — Xiyana Figuera et al., arXiv 2024-09-20. [arXiv](https://arxiv.org/abs/2409.13208) [Code](https://github.com/rllab-postech/MR-HuBo) — 人体先验重新定义重定向数据配对
- **High-Speed and Impact Resilient Teleoperation of Humanoid Robots** — Sylvain Bertrand et al., arXiv 2024-09-06. [arXiv](https://arxiv.org/abs/2409.04639) — 高速抗冲击人形遥操作
- **Unsupervised Neural Motion Retargeting for Humanoid Teleoperation** — Satoshi Yagi et al., arXiv 2024-06-02. [arXiv](https://arxiv.org/abs/2406.00727) — 无监督神经运动重定向（遥操作）

### 🤝 双机交互与基准

> 双人形/双臂/基准

- **Policy-Induced Hand Priors in Humanoid Dual-Arm Manipulation: Diagnosing and Mitigating Initial-Pose Dependence** — Chaeyeon Jung et al., arXiv 2026-08-12. [arXiv](https://arxiv.org/abs/2608.11769) — 人形双臂操作的手部先验（初始位姿依赖诊断）
- **RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation** — Shuliang He et al., arXiv 2026-08-04. [arXiv](https://arxiv.org/abs/2608.03387) — RoboReact：生成视频智能体技能蒸馏（全身操作）
- **Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control** — Hyunjong Song et al., arXiv 2026-07-31. [arXiv](https://arxiv.org/abs/2607.29625) — 人形搬运物体质量平衡（举升控制）
- **ThorArena: Benchmarking Humanoid Physical Interaction with Human Motion-Force Demonstrations** — Chenhao Yu et al., arXiv 2026-07-07. [arXiv](https://arxiv.org/abs/2607.06052) [Code](https://github.com/BAAI-AETHER/ThorArena) — ThorArena：人形物理交互基准（人-力演示）
- **ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning** — Wei Xiao et al., arXiv 2026-06-15. [arXiv](https://arxiv.org/abs/2606.17011) — ROVE：RL 人形操作中的人类干预
- **WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning** — Jaehwi Jang et al., arXiv 2026-06-11. [arXiv](https://arxiv.org/abs/2606.13232) [Code](https://github.com/wt-umi/WTUMI) — WT-UMI：力监督接触感知规划的触觉全身操作
- **Cognition to Control - Multi-Agent Learning for Human-Humanoid Collaborative Transport** — Hao Zhang et al., arXiv 2026-03-04. [arXiv](https://arxiv.org/abs/2603.03768) — 人-人形协作搬运（多智能体学习）
- **It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots** — Zuhong Liu et al., arXiv 2025-10-11. [arXiv](https://arxiv.org/abs/2510.10206) — It Takes Two：双人形交互式全身控制
- **DexMan: Learning Bimanual Dexterous Manipulation from Human and Generated Videos** — Jhen Hsieh et al., arXiv 2025-10-09. [arXiv](https://arxiv.org/abs/2510.08475) — DexMan：人类+生成视频学习双臂灵巧操作
- **HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** — Zhi Jing et al., arXiv 2025-07-01. [arXiv](https://arxiv.org/abs/2507.00833) [Code](https://github.com/TeleHuman/HumanoidGen) — HumanoidGen：LLM 推理的双臂灵巧操作数据生成
- **Large Language Models for Orchestrating Bimanual Robots** — Kun Chu et al., arXiv 2024-04-02. [arXiv](https://arxiv.org/abs/2404.02018) — 大语言模型编排双臂机器人
- **HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation** — Carmelo Sferrazza et al., arXiv 2024-03-15. [arXiv](https://arxiv.org/abs/2403.10506) — HumanoidBench：全身运动与操作仿真基准
