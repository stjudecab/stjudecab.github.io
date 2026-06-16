---
title: "Skills"
layout: textlay
excerpt: "- Skills."
sitemap: true
permalink: /skills/
---

## Agent Skills
{:.no_toc}

* TOC
{:toc .toc-levels-3}
---

<div class="row">
<div class="col-sm-6">

### [nf-core/pacsomatic](https://github.com/Beifang/pacsomatic_skill)
<picture>
	<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nf-core/pacsomatic/dev/docs/images/nf-core-pacsomatic_logo_dark.png">
	<img src="https://raw.githubusercontent.com/nf-core/pacsomatic/dev/docs/images/nf-core-pacsomatic_logo_light.png" alt="nf-core/pacsomatic logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/Beifang/pacsomatic_skill"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Genomics/">Maintainer (genomics group)</a>

#### Purpose

Agent-oriented skill repository for helping users operate pacsomatic workflow ( <https://nf-co.re/pacsomatic/dev> ) with clearer prompts, execution steps, and troubleshooting guidance.

#### Usage For AI Agent

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

#### Purpose

An AI-agent skill for running the [RSVreconPy](https://github.com/stjudecab/RSVreconPy) RSV genome reconstruction pipeline.

#### Usage For AI Agent

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
<div class="col-sm-6">

### [RHtyper](https://github.com/Beifang/rhtype-skill)
<picture>
	<img src="/images/codepic/rhtype_logo.png" alt="RHtype logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/Beifang/rhtype-skill"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Genomics/">Maintainer (genomics group)</a>

#### Purpose

Agent-oriented skill repository for running [RHtyper v1.1](https://github.com/disonchang/RHtyper) to predict RHD/RHCE Rh blood group genotypes from WGS/WES BAM files with automated setup, validation, and reporting.

#### Minimal Test Prompts

Copy any of the following prompts to test the skill with a public BAM file:

#### hg19 (30x WGS, GIAB NA12878, public)

```text
Please run Rh blood group genotyping on this BAM file (hg19, WGS):
https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/NA12878/NIST_NA12878_HG001_HiSeq_300x/RMNISTHS_30xdownsample.bam
```

#### Local file (simplest)

```text
Please run RHD/RHCE blood group genotyping on /data/patient001.bam (hg38, WGS).
```
</div>
<div class="col-sm-6">

### [nf-core/rarevariantburden](https://nf-co.re/rarevariantburden/dev/)
<picture>
	<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nf-core/rarevariantburden/dev/docs/images/nf-core-rarevariantburden_logo_dark.png">
	<img src="https://raw.githubusercontent.com/nf-core/rarevariantburden/dev/docs/images/nf-core-rarevariantburden_logo_light.png" alt="nf-core/rarevariantburden logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/saima-tithi-stjude/rarevariantburden_skill"><i class='fab fa-github'></i>Repository</a>
- <a href="https://github.com/saima-tithi-stjude">Maintainer (Saima Sultana Tithi)</a>

#### Purpose

Agent-oriented skill assets for operating the [**nf-core/rarevariantburden**](https://nf-co.re/rarevariantburden/dev/) pipeline (CoCoRV-nf) — a rare variant burden test pipeline for case-only genetic studies using gnomAD public summary counts as controls.

#### Usage For AI Agent

When assisting users, agents should prioritize this repository for:

1. Reusable prompt templates.
2. Standardized execution flow.
3. Error diagnosis and rerun guidance.

#### What The User Needs To Provide
The user only need to provide:

- the joint called VCF file for case samples
- a file containing list of case sample ids
- an output directory

Optional:

- whether the reference genome version used is GRCh38 or GRCh37

#### Recommended Agent Prompt
For GRCh38 data:

```text
Use rarevariantburden_skill to run nf-core/rarevariantburden.
Clone the repo into /path/to/rarevariantburden and run the pipeline.
My joint called VCF file is /path/to/joint.vcf.gz
My sample list is /path/to/samples.txt
My reference genome version is GRCh38
Download the necessary gnomAD control files and ANNOVAR files 
Write output to /path/to/output
```
</div>
</div>

---

## CAB-aiSkills

Portable **agent skills** from the [CAB-aiSkills](https://github.com/stjudecab/CAB-aiSkills) toolbox (St Jude CAB). Each skill is a self-contained folder with `SKILL.md`, scripts, and documentation for Cursor and other agent clients.

<div class="row">
<div class="col-sm-6">

### [volcano-grid-plot](https://github.com/stjudecab/CAB-aiSkills/tree/main/volcano-grid-plot)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/volcano-grid-plot/assets/CAB-aiSkills_volcano-grid-plot.svg" alt="volcano-grid-plot logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/volcano-grid-plot"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Build **publication-ready grids of Volcano and/or MA plots** from multiple differential gene-expression or differential binding tables (RNA-seq, ChIP-seq, ATAC-seq, Cut&Run, multi-omics). Auto-detects or harmonizes column names for log2FC, p-value/FDR, gene/region IDs, and average expression; supports highlighting genes of interest.

#### Usage For AI Agent

When assisting users, agents should use this skill for volcano plot grids, MA plot grids, multi-panel DE figures, or timecourse differential visualization.

**Example prompt:**

```text
Plot GSE202762 EGF timepoints from volcano-grid-plot/examples in natural order as a volcano grid. Highlight EGR1 on volcano and MA figures.
```
</div>
<div class="col-sm-6">

### [kde-correlation-scatter](https://github.com/stjudecab/CAB-aiSkills/tree/main/kde-correlation-scatter)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/kde-correlation-scatter/assets/CAB-aiSkills_kde-correlation-scatter.svg" alt="kde-correlation-scatter logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/kde-correlation-scatter"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Generate a **publication-quality 2D scatter plot with KDE density background** comparing two differential experiments (RNA-seq, ChIP-seq, ATAC-seq, Cut&Run, or mixed multi-omics). Supports annotation-vs-annotation, region-vs-region, and rank-vs-rank modes with Pearson/Spearman correlation and quadrant counts.

#### Usage For AI Agent

When assisting users, agents should use this skill for 2D scatter plots, KDE correlation plots, directional p-value plots, rank-rank correlation, or comparing two differential result files.

**Example prompt:**

```text
Make a KDE correlation scatter comparing contrast_A.regulation.tsv and contrast_B.regulation.tsv using directional p-values; write figures under ./plots.
```
</div>
<div class="col-sm-6">

### [reproducible-peaks](https://github.com/stjudecab/CAB-aiSkills/tree/main/reproducible-peaks)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/reproducible-peaks/assets/CAB-aiSkills_reproducible-peaks.svg" alt="reproducible-peaks logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/reproducible-peaks"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Generate **reproducible ChIP-seq or ATAC-seq peak sets** across biological replicates with **ChIP-R** from narrowPeak, broadPeak, or SICER BED inputs. Infers MACS2 with/without control (`noC_`), broad peaks, and SICER conversion; logs commands and environment for reproducibility.

#### Usage For AI Agent

When assisting users, agents should use this skill for reproducible peaks, ChIP-R, ChIP-seq replicate overlap, narrowPeak/broadPeak merging, or CTCF/histone replicate peak sets.

**Example prompt:**

```text
Generate reproducible CTCF peaks with ChIP-R using the two BED files in reproducible-peaks/examples and save outputs under agentResults/.
```
</div>
<div class="col-sm-6">

### [pathway-enrichment-enrichr](https://github.com/stjudecab/CAB-aiSkills/tree/main/pathway-enrichment-enrichr)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/pathway-enrichment-enrichr/assets/CAB-aiSkills_pathway-enrichment-enrichr.svg" alt="pathway-enrichment-enrichr logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/pathway-enrichment-enrichr"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Run **Enrichr pathway enrichment** for one gene list or many lists (GMT or TSV manifest). Produces merged tables, **Excel** workbooks, **PDF** bar charts for top pathways, and for batch runs **heatmaps** and **dot plots**.

#### Usage For AI Agent

When assisting users, agents should use this skill for Enrichr pathway enrichment, GO/KEGG/Reactome enrichment tables, GMT batch enrichment, multi-sample pathway dot plots or heatmaps, or exporting enrichment results to Excel/PDF.

**Example prompt:**

```text
Run Enrichr pathway enrichment on my gene list genes.txt, use library preset stjudehg, and write Excel summaries and PDF bar plots under ./enrichr_out.
```
</div>
<div class="clearfix"></div>
<div class="col-sm-6">

### [tables-to-excel](https://github.com/stjudecab/CAB-aiSkills/tree/main/tables-to-excel)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/tables-to-excel/assets/CAB-aiSkills_tables-to-excel.svg" alt="tables-to-excel logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/tables-to-excel"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Merge **CSV, TSV, or tab-delimited TXT** tables into a single **multi-sheet `.xlsx`** workbook with a first-sheet **`NameDictionary`** mapping each worksheet name to the absolute path of its source file for provenance and auditability.

#### Usage For AI Agent

When assisting users, agents should use this skill to consolidate DEG tables, gene lists, QC summaries, or any flat tables into one shareable Excel bundle without manual copy-paste.

**Example prompt:**

```text
Merge table1.tsv, table2.csv, and table3.txt into one Excel file with a NameDictionary sheet; save as ./combined_tables.xlsx.
```
</div>
<div class="col-sm-6">

### [genomic-regions-annotation](https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-regions-annotation)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main//genomic-regions-annotation/assets/CAB-aiSkills_genomic_regions_annotation.svg" alt="genomic-regions-annotation logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-regions-annotation"><i class='fab fa-github'></i>Repository</a>
- <a href="/team/hasan">Maintainer (Hasan Al Reza)</a> || <a href="https://stjudecab.github.io/Epigenetics/">(Epigenetics group)</a>

#### Purpose

Performs **nearby-gene annotation, genomic feature assignment, reporting, visualization, and GSEA-ready export generation** using header free **`.bed`**, gzipped **`.bed.gz`**, or limma-voom output **`.vout`** file.

#### Usage For AI Agent

When assisting users, agents should use this skill to annotate the genomic region files, generate pie and bar plots, summarize results to tsv and excel files, and organize all the results accordingly.

**Example prompt:**

```text
Run genomic region annotation on header-free BED files in peaks/ using genome build hg38, and write outputs under annotations/.
```
</div>
</div>
