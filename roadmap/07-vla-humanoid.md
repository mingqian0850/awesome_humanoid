# 07 · VLA / VLM × Humanoid（Stage 6）

> 定位：路线图的**终点**。理解 2025–2026 人形 VLA 的三条主流架构路线，并最终搭出 `VLM/VLA → task/EE/latent command → whole-body controller → humanoid` 的系统。
> 时间预算：1 周（12 周计划 Week 12 收尾；此前 Week 11 只读架构图）。
> ⚠️ 本文所有链接均为 2026-08 实测核实；标注"未核实"的项不要引用为事实。

## 7.1 核心问题：VLA 到底输出什么？

```
路线 A：VLA ──直接输出 20–40 DoF joint actions──▶ robot
路线 B：VLA ──EE / body command──▶ WBC ──joint command──▶ robot
路线 C：VLA ──latent action──▶ low-level whole-body policy──▶ robot
```

**2026 年 8 月的结论**：路线 A 只出现在数据极充分的单一本体（GR00T N1、Figure Helix 是 A/B 混合体）；**工程主流是 B（NVIDIA GR00T 全栈）**；**研究热点是 C（π0/WholeBodyVLA/LeVERB）**。趋势是 B+C 融合：统一 latent VLA + 解耦/可学习的 WBC 低层。

## 7.2 各工作核实表（2026-08）

| 工作 | 年份 | 架构 | 开源 | 真机 | 关键点 |
|---|---|---|---|---|---|
| **GR00T N1**（[arXiv](https://arxiv.org/abs/2503.14734)） | 2025 | A：双系统（System2 VLM + System1 扩散 Transformer）直接出关节位置目标 | ✅ HF `nvidia/GR00T-N1-2B` + [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | ✅ Fourier GR-1 | 开源人形基础模型开山之作 |
| **GR00T N1.5**（[官方页](https://research.nvidia.com/labs/gear/gr00t-n1_5/)） | 2025-06 | B：VLA 出关节速度（50Hz）→ **Decoupled WBC** 解算 | ✅ HF `nvidia/GR00T-N1.5-3B` | ✅ GR-1/H1/G1 | 人视频预训练 + RL 微调；"VLA+WBC"业界标准形态（无 arXiv 论文） |
| **GR00T Whole-Body Control**（[GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl) · [文档](https://nvlabs.github.io/GR00T-WholeBodyControl/)） | 2025–26 | B 的实现：Decoupled WBC（RL 下半身 + IK 上半身），现含 GEAR-SONIC 全身控制器 | ✅ Apache-2.0 | ✅ N1.5/N1.6/N1.7 | **不是论文，是可训练/可部署的 WBC 模块栈** —— 想学"VLA→WBC 怎么落地"，这是第一站 |
| **π0 / π0.5**（[arXiv](https://arxiv.org/abs/2410.24164) · [π0.5 博客](https://www.pi.website/blog/pi05)） | 2024–25 | C：flow matching 出 EEF 动作（latent/连续动作） | 🟡 权重状态未核实 | ✅ 双臂平台 | 首个通用 flow-matching VLA；π0.5 权重传闻在 HF `lerobot/pi05_base` |
| **Gemini Robotics / ER**（[arXiv 2503.20020](https://arxiv.org/abs/2503.20020) · [1.5: arXiv 2510.03342](https://arxiv.org/abs/2510.03342)） | 2025 | A/C 混合（Gemini 2.0 底座；ER 具身推理） | ❌ 未开源 | ✅（非人形主打） | 通用 VLA+推理双线；motion transfer 与 ER 思路被后人形工作复用 |
| **WholeBodyVLA**（[arXiv 2512.11047](https://arxiv.org/abs/2512.11047)） | 2025（ICLR 2026） | C：locomotion 与 manipulation 共享**统一 latent 动作空间** | ✅ [OpenDriveLab/WholebodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) | 未核实 | 操纵感知的移动（大空间 loco-manipulation） |
| **LeVERB**（[arXiv](https://arxiv.org/abs/2506.13751) · [项目页](https://ember-lab-berkeley.github.io/LeVERB-Website/)） | 2025 | C：latent VLM 指令 + 低层全身控制 | 未核实 | ✅ 人形 | 解耦语义与高频运动的 sim-to-real 方案 |
| **HPT**（[arXiv](https://arxiv.org/abs/2409.20537) · [项目页](https://liruiw.github.io/hpt/)） | 2024 | 跨本体预训练 Transformer 骨干（常作低层 policy 底座） | ✅ [liruiw/HPT](https://github.com/liruiw/HPT) | ❌ 仿真 benchmark | 学 latent 表征，非 VLA 本身 |
| **Figure Helix**（[博客](https://www.figure.ai/news/helix) · [Helix 02](https://www.figure.ai/news/helix-02)） | 2025-02 | A/B 混合：S2 VLM 出语义/潜变量 + S1 连续上身控制（200Hz） | ❌ 未开源（社区有复现） | ✅ Figure 02/03 | 首个全上身高频连续控制 VLA + 双机协作 |
| **1X World Model**（[页面](https://www.1x.tech/discover/1x-world-model) · [技术报告 PDF](https://www.1x.tech/1x-world-model.pdf)） | 2024-09 | 视频世界模型（NEO 的虚拟仿真器，"bits not atoms"） | ❌ 未开源 | NEO 视频数据 | 注意：官方无 NeurIPS 说法，是技术博客+报告 |
| **Tesla Optimus** | — | 无公开技术论文/技术博客 | — | — | **不列入**（无足够技术细节） |
| **Humanoid Locomotion as Next Token Prediction**（[arXiv](https://arxiv.org/abs/2402.19469) · [NeurIPS 2024](https://proceedings.neurips.cc//paper_files/paper/2024/hash/90afd20dc776bc8849c31d61a0763a0b-Abstract-Conference.html)） | 2024 | "运动即语言"：自回归下一 token 预测 | 未核实 | ✅ Digit | 触发后续"运动即语言"路线 |

> ⚠️ **FLEX 澄清**：流传的 "FLEX: Full-Body Grasping"（arXiv 2409.14800）经核实是无关论文；同名 "FLEX"（arXiv 2211.11903, CVPR 2023）是**虚拟人全身抓取合成**（avatar 动画），不是机器人工作。本文不收录该名称，避免误导。

## 7.3 三条路线的工程判断（写给要动手的人）

| 维度 | A 直接出 joint | B VLA→命令→WBC | C VLA→latent→policy |
|---|---|---|---|
| 实现难度 | 中（但调数据地狱） | 低-中（模块解耦，可分别调试） | 高（端到端联合训练） |
| 可复用性 | 差（绑定本体/数据） | 好（WBC 层独立可复用） | 中（latent 空间不通用） |
| 数据效率 | 低 | 中 | 高 |
| 可解释/可调试 | 好 | 好 | 差 |
| 2026 热度 | 低（仅大厂单本体） | **工程主流（NVIDIA 全栈）** | **研究热点** |

**你的 roadmap 落点**：学路线 B 的实现（GR00T-WholeBodyControl 代码），理解路线 C 的论文（π0/WholeBodyVLA），自己搭一个小型"路线 B"系统即可毕业 —— 即 **VLM 出 task/EE 命令 → 你的 learned WBC（Stage 4 训练的）→ G1**。

## 7.4 Stage 6 · 学习路径与 milestone

```
Week 12:
  D1–2  读 GR00T N1 论文（只读架构图+训练配方）+ π0 论文（flow matching 概念即可）
  D3    读 GR00T-WholeBodyControl 代码：搞清楚 body 命令空间、WBC 接口
  D4–5  集成实验：把 Week 11 的 locomotion policy 接到一个简单的 VLM 命令源
        （先用规则/脚本模拟 VLM 输出目标速度+EE 目标，验证接口设计）
  D6–7  综合项目收尾 + 写系统架构文档（你的 policy 栈长什么样）
```

**Milestone 验证**：
- [ ] 能画出你的完整系统框图：感知（RGB/RGB-D）→ VLM/VLA → 命令空间 → 低层 WBC → G1
- [ ] 能解释为什么路线 B 的"命令空间设计"是瓶颈（接口 gap）
- [ ] 用模拟 VLM 命令（脚本代替）驱动你的 G1 完成"走到桌子前 → 手伸向物体"的 sim 演示

**可以跳过**：flow matching 数学细节、Gemini/Figure 的工程细节、世界模型训练、VLA 数据管线搭建（用公开数据集）。
