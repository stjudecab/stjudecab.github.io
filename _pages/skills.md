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

### [imprintomeR](https://github.com/hongjianjin/imprintomeR)
<img
  src="https://raw.githubusercontent.com/hongjianjin/imprintomeR/master/images/logo_small.png"
  alt="imprintomeR logo"
  width="140"
/>

- <a href="https://github.com/hongjianjin/imprintomeR"><i class='fab fa-github'></i>Repository</a>
- <a href="https://github.com/hongjianjin/imprintomeR/tree/master/skills/imprintomer">Skill</a>
- <a href="https://github.com/hongjianjin">Maintainer (Hongjian Jin)</a>

#### Purpose

Agent-oriented skill repository for helping users run the [imprintomeR](https://github.com/hongjianjin/imprintomeR) R workflow for methylation-array quality control, genomic-imprinting analysis, and publication-quality visualization.

#### Usage For AI Agent

When assisting users, agents should prioritize this repository for:

1. Validating IDAT or beta-matrix inputs, metadata, array platforms, probesets, and genome builds.
2. Guiding the two-stage QC-to-imprintome workflow or direct beta-matrix analysis with the repository’s Rscript entry points.
3. Verifying QC RDS files, result tables, plots, warnings, and output locations.

</div>
<div class="col-sm-6">
</div>
</div>


<div class="row">
<div class="col-sm-6">

### [ChIPseqSpikeInFree](https://github.com/stjude/ChIPseqSpikeInFree)
<img
 src="https://raw.githubusercontent.com/stjude/ChIPseqSpikeInFree/master/docs/logo_small.png"
 alt="ChIPseqSpikeInFree logo"
 width="150"
/>
- <a href="https://github.com/stjude/ChIPseqSpikeInFree"><i class='fab fa-github'></i>Repository</a>
- <a href="https://github.com/stjude/ChIPseqSpikeInFree/tree/master/skills/chipseqspikeinfree">Skill</a>
- <a href="https://github.com/hongjianjin">Maintainer (Hongjian Jin)</a>

#### Purpose

Agent-oriented skill repository for helping users run the [ChIPseqSpikeInFree](https://github.com/stjude/ChIPseqSpikeInFree) spike-in-free ChIP-seq normalization workflow with clear prompts, validated inputs, standardized execution steps, and reproducible result reporting.

#### Usage For AI Agent

When assisting users, agents should prioritize this repository for:

1. Validating BAM lists, metadata files, genome aliases, and chromosome-size inputs.
2. Selecting and running standard normalization or replotting workflows.
3. Inspecting scaling-factor tables, QC status, plots, warnings, and output locations.

</div>
<div class="col-sm-6">
</div>
</div>

<div class="row">
<div class="col-sm-6">

### [nf-core/pacsomatic](https://github.com/Beifang/pacsomatic_skill)
<picture>
	<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nf-core/pacsomatic/dev/docs/images/nf-core-pacsomatic_logo_dark.png">
	<img src="https://raw.githubusercontent.com/nf-core/pacsomatic/dev/docs/images/nf-core-pacsomatic_logo_light.png" alt="nf-core/pacsomatic logo" style="max-width: 200px; width: 100%; height: auto; margin: 8px 0 14px 0;">
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
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/genomic-regions-annotation/assets/CAB-aiSkills_genomic_regions_annotation.svg" alt="genomic-regions-annotation logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-regions-annotation"><i class='fab fa-github'></i>Repository</a>
- <a href="/team/hasan">Maintainer (Hasan Al Reza)</a> | <a href="https://stjudecab.github.io/Epigenetics/">(Epigenetics group)</a>

#### Purpose

Performs **nearby-gene annotation, genomic feature assignment, reporting, visualization, and GSEA-ready export generation** using header free **`.bed`**, gzipped **`.bed.gz`**, or limma-voom output **`.vout`** file.

#### Usage For AI Agent

When assisting users, agents should use this skill to annotate the genomic region files, generate pie and bar plots, summarize results to tsv and excel files, and organize all the results accordingly.

**Example prompt:**

```text
Run genomic region annotation on header-free BED files in peaks/ using genome build hg38, and write outputs under annotations/.
```
</div>
<div class="clearfix"></div>
<div class="col-sm-6">

### [custom-ES-plot-GSEApy](https://github.com/stjudecab/CAB-aiSkills/tree/main/custom-ES-plot-GSEApy)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/custom-ES-plot-GSEApy/assets/CAB-aiSkills_custom-ES-plot-GSEApy.svg" alt="custom-ES-plot-GSEApy logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/custom-ES-plot-GSEApy"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Generate **GSEA enrichment score (ES) plots** and **statistics text files** from saved **GSEApy `pre_res` pickle** files or **Broad Institute GSEA desktop output directories**, with support for exact gene sets, regex patterns, and `allGeneSets` — including non-significant gene sets omitted from default exports.

#### Usage For AI Agent

When assisting users, agents should use this skill for custom GSEA enrichment score visualization, replotting Broad GSEA results, GSEApy pickle inspection, or exporting GSEA statistics and figures.

**Example prompt:**

```text
From GSEApy_prerank.pre_res.RNA.KO_48h_vs_WT_48h.pkl, plot enrichment for all CTCF_peaks.* gene sets and save PNG/PDF/TXT under agentResults/.
```
</div>
<div class="col-sm-6">

### [genomic-set-analysis](https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-set-analysis)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/genomic-set-analysis/assets/CAB-aiSkills_genomic-set-analysis.svg" alt="genomic-set-analysis logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-set-analysis"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

**Order-independent overlap analysis** of genomic region sets (ChIP-seq, ATAC-seq, CUT&Tag, CUT&RUN, narrowPeak/broadPeak/BED) or gene sets (GMT) using **Intervene** (Venn / UpSet / pairwise), producing membership matrices and mutually exclusive per-sector files. Optionally chains **`genomic-regions-annotation`** and **`pathway-enrichment-enrichr`** skills for comprehensive downstream analysis.

#### Usage For AI Agent

When assisting users, agents should use this skill for overlapping genomic region sets, generating Venn/UpSet diagrams, performing set intersection analysis, or running multi-omics overlap with integrated annotation and pathway enrichment.

**Example prompt:**

```text
Overlap the three BED files in peaks/ using Intervene, annotate results against hg38, and run pathway enrichment for each intersection and original file; write outputs under agentResults/.
```
</div>
<div class="clearfix"></div>
<div class="col-sm-6">

### [bioinformatics-reporting](https://github.com/stjudecab/CAB-aiSkills/tree/main/bioinformatics-reporting)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/bioinformatics-reporting/assets/CAB-aiSkills_bioinformatics-reporting.svg" alt="bioinformatics-reporting logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/bioinformatics-reporting"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Transform **existing** bioinformatics result directories into polished, evidence-grounded **Quarto HTML/PDF reports** with complete reproducibility bundles. Discovers/validates artifacts, builds normalized report models with provenance-backed metrics, renders self-contained deliverables, and verifies outputs.

#### Usage For AI Agent

When assisting users, agents should use this skill to generate scientific reports from RNA-seq, ATAC-seq, ChIP-seq, CUT&RUN/CUT&Tag, enrichment, overlap analysis, or multi-omics result collections with automated metrics and audit trails.

**Example prompt:**

```text
Create a scientific bioinformatics report from the results in agentResults/my-analysis-20260709T141453Z, including overlap plots, enrichment tables, and an evidence-grounded executive summary; write HTML and PDF under agentResults/.
```
</div>
<div class="col-sm-6">

### [colorblind-sim](https://github.com/stjudecab/CAB-aiSkills/tree/main/colorblind-sim)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/colorblind-sim/assets/CAB-aiSkills_colorblind-sim.svg" alt="colorblind-sim logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/colorblind-sim"><i class='fab fa-github'></i>Repository</a>
- <a href="https://stjudecab.github.io/Epigenetics/">Maintainer (Epigenetics group)</a>

#### Purpose

Simulate how **figures appear under color vision deficiency (CVD)** using **CBviz** (protanopia, deuteranopia, tritanopia, monochrome). Accepts PNG/JPEG/TIFF directly; auto-converts PDF (and SVG/EPS when tools available) to PNG before simulation. Outputs multi-panel preview figures plus full run audit trail.

#### Usage For AI Agent

When assisting users, agents should use this skill for colorblind-accessibility preview of figures, testing plot visibility under color vision deficiency, or generating CVD-aware figure panels.

**Example prompt:**

```text
Simulate colorblindness on my volcano plot figures/volcano.png (or figure.pdf) and save the CBviz comparison panels under agentResults/.
```
</div>
<div class="clearfix"></div>
<div class="col-sm-6">

### [genomic-regions-correlation](https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-regions-correlation)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/genomic-regions-correlation/assets/CAB-aiSkills_genomic_regions_correlation.svg" alt="genomic-regions-correlation logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/genomic-regions-correlation"><i class='fab fa-github'></i>Repository</a>
- <a href="/team/hasan">Maintainer (Hasan Al Reza)</a> | <a href="https://stjudecab.github.io/Epigenetics/">(Epigenetics group)</a>

#### Purpose

Runs `bidirectional` **GenometriCorr analyses** on two **`.bed`** files and generates **PDF correlation reports and visualizations** for the selected `genome build`.

#### Usage For AI Agent

When assisting users, agents should use this skill to find bidirectional correlation between two genomic region files, PDF correlation reports, and visualizations for each chromosome and the genome overall.

**Example prompt:**

```text
Compare gained.bed and reference.bed with GenometriCorr using hg38, and write the reports under agentResults/.
```
</div>
<div class="col-sm-6">

### [tornado-plots](https://github.com/stjudecab/CAB-aiSkills/tree/main/tornado-plots)
<picture>
	<img src="https://raw.githubusercontent.com/stjudecab/CAB-aiSkills/main/tornado-plots/assets/CAB-aiSkills_tornado_plots.svg" alt="tornado-plots logo" style="max-width: 300px; width: 100%; height: auto; margin: 8px 0 14px 0;">
</picture>

- <a href="https://github.com/stjudecab/CAB-aiSkills/tree/main/tornado-plots"><i class='fab fa-github'></i>Repository</a>
- <a href="/team/hasan">Maintainer (Hasan Al Reza)</a> | <a href="https://stjudecab.github.io/Epigenetics/">(Epigenetics group)</a>

#### Purpose

Generates **deepTools tornado plots and heatmaps** from **`.bed`** region files and **`.bigwig`** signal tracks using `computeMatrix reference-point` and `plotHeatmap`. Supports local execution and optional LSF bsub submission.

#### Usage For AI Agent

When assisting users, agents should use this skill to create symlinks to input files and generate a matrix containing scores per genomic regions, and a tornado plot.

**Example prompt:**

```text
Create a tornado plot from Sample.Up2FC.Region.bed and Sample.Down2FC.Region.bed using the supplied ChIP-seq BigWig tracks, and save outputs under agentResults/.
```
</div>
</div>
