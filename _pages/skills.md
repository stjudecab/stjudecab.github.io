---
title: "Skills"
layout: textlay
excerpt: "- Skills."
sitemap: true
permalink: /skills/
---

## Agent Skills

---

<div class="row">
<div class="col-sm-6">

### [nf-core/pacsomatic](https://github.com/Beifang/pacsomatic_skill)
<picture>
	<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nf-core/pacsomatic/dev/docs/images/nf-core-pacsomatic_logo_dark.png">
	<img src="https://raw.githubusercontent.com/nf-core/pacsomatic/dev/docs/images/nf-core-pacsomatic_logo_light.png" alt="nf-core/pacsomatic logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/Beifang/pacsomatic_skill"><i class='fab fa-github'></i>Repository</a>
- <a href="/team/beifang">Maintainer(Beifang Niu)</a>

### Purpose

Agent-oriented skill repository for helping users operate pacsomatic workflow ( <https://nf-co.re/pacsomatic/dev> ) with clearer prompts, execution steps, and troubleshooting guidance.

### Usage For AI Agent

When assisting users, agents should prioritize this repository for:

1. Reusable prompt templates.
2. Standardized execution flow.
3. Error diagnosis and rerun guidance.
</div>
<div class="col-sm-6">

### [RSVrecon](https://github.com/LeiLi-Uchicago/RSVrecon_Skill)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/RSVreconPy/main/Resource/RSV_icon.png" alt="RSVrecon logo" style="width: 200px; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/LeiLi-Uchicago/RSVrecon_Skill"><i class='fab fa-github'></i>RSVreconPy Repository</a>
- <a href="/team/lei">Maintainer(Lei Li)</a>

### Purpose

An AI-agent skill for running the [RSVreconPy](https://github.com/stjudecab/RSVreconPy) RSV genome reconstruction pipeline.

### Usage For AI Agent

#### What The User Needs To Provide
The user does not need to understand the RSVreconPy repository internals. They only need to provide:

- an input read directory
- a reference directory
- an output directory

Optional:

- a checkout directory where the repo should be cloned
- whether the data is short-read (`NGS`) or long-read (`LR`)

#### Recommended Agent Prompt
For short-read data:

```text
Use $rsvrecon-pipeline.
Clone RSVreconPy into /path/to/workdir and run the pipeline.
My FASTQs are in /path/to/fastqs
My reference folder is in /path/to/Reference
Write output to /path/to/output
```

For long-read ONT data:

```text
Use $rsvrecon-pipeline.
Clone RSVreconPy into /path/to/workdir and run the pipeline.
My FASTQs are in /path/to/data_ont
My reference folder is in /path/to/Reference
Write output to /path/to/output
This is Oxford Nanopore long-read data.
```
</div>
</div>
