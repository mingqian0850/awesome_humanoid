# Recent humanoid-control developments

[Home](../README.md) · [中文](topic-progress-2026-10-21.zh-CN.md)

Checked **2026-10-21**. This is a recent topic increment, with paper, code-snapshot and announcement dates distinguished; historical entries were not all reverified. Method results are author-reported; selection and exercises are engineering guidance.

## Choose by your problem

| Your problem | Recent work | Change | Current access |
| --- | --- | --- | --- |
| Abundant human data, scarce robot demonstrations | VioLA, Oct 8 | Body/hand motion latents connect human data with robot control | Method and robot experiments; code/checkpoints pending |
| Arm and torso contact matters when carrying a box | Whole-Body Dexterity, Oct 15 | Body surfaces participate in grasping and repositioning | Robot research, not an autonomous factory product |
| Independent IK breaks contact between cooperating humanoids | OmniInteract, Oct 19; v2 Oct 20 | Joint surface-aware retargeting plus partner-conditioned residuals | Paper/demos; executable release not verified here |

## VioLA: change the policy action space

[VioLA](https://arxiv.org/abs/2610.12435) encodes human/robot motion into shared spaces. A generalist policy predicts body and hand latents executed by pretrained controllers, rather than treating human joint angles as robot commands.

**Implication for your workflow:** design capture around both motion information and the target controller representation. Ego RGB alone does not supply these latent labels. Draw video/motion → encoder → latent → controller, identifying training and embodiment adaptation requirements.

**Evidence boundary:** the paper reports robot experiments; the [project page](https://viola.is.tue.mpg.de) still labels code and checkpoints as forthcoming. It is not yet a verified downloadable fine-tuning baseline. Its particular tests do not establish performance across industrial tasks.

## Whole-Body Dexterity: use body contact

The [paper](https://arxiv.org/abs/2610.22184) generates feasible whole-body grasps, trains repositioning experts and distills them. Arms and torso support objects rather than relying only on fingertips. G1 demonstrations reposition a ball and box; coarse motion references come from a human operator.

**Choose it for:** bulky-object transfer, bracing or under-arm carrying. It does not replace precision end-effector contact for a stationary insertion task. Record object geometry, permitted robot contact surfaces and contact transitions. Research success rates are not unattended production availability.

## OmniInteract: contact relations are objectives

[OmniInteract](https://arxiv.org/abs/2610.26043v2) jointly retargets two humanoids while preserving surface contacts and nearby geometry. Partner-conditioned corrections build on a frozen whole-body prior; flow matching consolidates interaction skills. The [project](https://calvinyhli.github.io/omniinteract.github.io/) provides demonstrations.

**Reading exercise:** separate individual pose errors from inter-robot contact errors. Inspect contact location/timing, interpenetration and perturbation recovery. Dual-robot research does not establish human–robot collaboration safety.

## Learning output without training

Compare three hypothetical processes: stationary bimanual placement, carrying a box, and a two-robot handover. Record policy representation, controller interface, contact objects, capture signals, unknown components and acceptance metrics. An 8GB laptop can support document/record inspection; this page makes no claim that full training or simulation fits its memory.
