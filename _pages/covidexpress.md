---
title: "CovidExpress"
layout: textlay
excerpt: "CovidExpress, COVID-19, COVID, sars-cov-2, database, gene, expression, RNA-seq, OASL, FURIN, IL6, TNF, RIG-I, Immune, ACE2, Virus, TMPRSS2, CRP, IL1A, PPARGC1A, CXCL10, STAT1, DDX58, CSF3, SERPINE1, SPRR2A, CCL3, CD79A, TLR3, CSF2"
sitemap: true
permalink: /covidexpress/
---

## [CovidExpress Server](http://146.190.197.5/){:target="_blank"} 
{:.no_toc}
<!-- [CovidExpress Server](https://stjudecab_epi.gitlab.io/covidexpressdata/){:target="_blank"} -->
{:.no_toc}
(Server would sleep if no access within 30mins, please wait and refresh)

---
<div class="row">
<div class="col-sm-8">
* TOC
{:toc}
</div>

<div class="col-sm-3">
<script type="text/javascript" src="https://rf.revolvermaps.com/0/0/1.js?i=54woy7d9mxl&amp;s=200&amp;m=7&amp;v=true&amp;r=false&amp;b=ffffff&amp;n=true&amp;c=ff0000" async="async"></script>
</div>
</div>

**What's New**
 - 2021-10-08 Put up [Video Tutorials](https://www.youtube.com/playlist?list=PL6mTMza0yJjaqDJSoemg6qWhgUTjh9jua){:target="_blank"}
 - 2021-10-06 Setup [Gitter Channel](https://gitter.im/covidexpress/community){:target="_blank"} for bug report, new study suggestion, et.al
 - 2021-08-04 Added protocol information to meta data. Add "Split by", "Group by" function to heatmap
 - 2021-07-07 Poster presented at CSHL conference "COVID/SARS CoV2 Rapid Research Reports #6"
 - 2021-06-12 > 300 Vistors
 - 2021-05-26 Update biorxiv version for figures
 - 2021-05-18 Added DEG volcano plot, improved memory usage
 - 2021-05-16 biorxiv submission accepted
 - 2021-05-12 Start running at digitalocean
 - 2021-05-08 Deposit app to heroku and digitalocean
 - 2021-05-02 Improved GSEA run time by numba, add GSEA volcano plot
 - 2021-04-29 Finalized GSEA results, improved GSEA results storage usage
 - 2021-04-25 GSEA module ready
 - 2021-03-17 Visualization module Ready
 - 2021-03-12 Extracted gene clouds
 - 2021-03-10 Landing page framework finalized at github.io
 - 2021-02-24 Test idea PCA/tSNE/UMAP using ssGSEA score
 - 2021-02-12 Finalized QC criterion
 - 2021-01-20 Expand data to ~1500 samples
 - 2020-11-17 Started data download and processing ~700 samples

---- 
#### **Overview**
#### CovidExpress: an interactive portal for intuitive investigation on SARS-CoV-2 related transcriptomes
{:.no_toc}

#### Abstract
{:.no_toc}
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_wordcloud_DEG.jpg){: style="width: 250px; float: right;margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_wordcloud_DEG.svg)
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_wordcloud_pubtator.jpg){: style="width: 250px; float: right;margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_wordcloud_pubtator.svg)
<div style="text-align: justify">
Infection with severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) in humans could cause coronavirus disease 2019 (COVID-19). Since its first discovery in Dec 2019, SARS-CoV-2 has become a global pandemic and caused 2.8 million direct/indirect deaths (2021 Apr). Amongst the scientific community’s response to COVID-19, data sharing has emerged as an essential aspect of the combat against SARS-CoV-2. Despite the ever-growing studies about SARS-CoV-2 and COVID-19, to date, only a few databases were curated to enable access to gene expression data. Furthermore, these databases curated only a small set of data and do not provide easy access for investigators without computational skills to perform analyses. To fill this gap and advance open-access to the growing gene expression data on this deadly virus, we collected about 1,500 bulk RNA-seq datasets from publicly available resources, developed a database and visualization tool, named CovidExpress (https://stjudecab.github.io/covidexpress).  This open access database will allow research investigators to examine the gene expression in various tissues, cell lines, and their response to SARS-CoV-2 under different experimental conditions, accelerating the understanding of the etiology of this disease in order to inform the drug and vaccine development. Our integrative analysis of this big dataset highlights a set of commonly regulated genes in SARS-CoV-2 infected lung and nasal tissues, including OASL that were under-studied in COVID-19 related reports. Our results also suggested a potential FURIN positive feedback loop that might explain the evolutional advantage of SARS-CoV-2.
</div>
---- 
#### **Portal Usage**
- [Learn about cellxgene basical functions](https://chanzuckerberg.github.io/cellxgene/posts/gallery){:target="_blank"}
- [Video Tutorial: CovidExpress Differential Expressed Gene(DEG) analysis feature](https://www.youtube.com/watch?v=NYHAFQs8PDM&list=PL6mTMza0yJjaqDJSoemg6qWhgUTjh9jua&index=3){:target="_blank"}
- [Video Tutorial: CovidExpress Gene Set Enrichment Analysis(GSEA) feature](https://www.youtube.com/watch?v=--7KuPGOxgA&list=PL6mTMza0yJjaqDJSoemg6qWhgUTjh9jua&index=1){:target="_blank"}

- Below illustrated the functional plugins we developed to help visualzation and analysis.
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/cellxgene_gsea.jpg){: style="width: 100%; margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/cellxgene_gsea.jpg)

---- 
#### **Suggested Analysis Steps**
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_analysis_route.png){: style="width: 100%; margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_analysis_route.png)

----
#### **CovidExpress Metadata Explorer**
We used [jquery dataTable](https://datatables.net){:target="_blank"} so you could explore the meta data easily. [Open explorer page](https://stjudecab_epi.gitlab.io/covidexpressdata/CovidExpress_metadataExplorer.html){:target="_blank"}

----
#### **CovidExpress Expression Data Download**
h5ad file is a [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format#HDF5){:target="_blank"} format with annotation commonly used for single cell data. [Learn more about h5ad file.](https://anndata.readthedocs.io/en/latest/fileformat-prose.html){:target="_blank"}

[Download h5ad file for expression (~350Mb)](https://stjudecab_epi.gitlab.io/covidexpressdata/hm.integrated_withMeta_all.h5ad){:target="_blank"}

[Download GMT file for genesets from our and others' analysis(~30Mb)](https://stjudecab_epi.gitlab.io/covidexpressdata/202103highQ1093.cumulative_DEG_signatures.plusPublicCOVID.gmt.gz){:target="_blank"} so you could perform [GSEA analysis](http://www.gsea-msigdb.org/gsea/index.jsp){:target="_blank"} using your own data.

----
#### **Clustering Results for reviewing and Download**
(see below tables for details)
<table style="border-spacing: 10px;" border="1" class="dataframe table-bordered">
    <thead>
        <tr style="text-align: center;">
            <th>Score</th>
            <th>ssGSEA</th>
            <th>ssGSEA</th>
            <th>ssGSEA</th>
            <th>TPM</th>
            <th>TPM</th>
            <th>TPM</th>
        </tr>
        <tr style="text-align: right;">
            <th>Data</th>
            <th>COV.Significant</th>
            <th>COV.All.Signature</th>
            <th>MSigDB</th>
            <th>CombinedDiff</th>
            <th>BatchCorrected</th>
            <th>Original</th>
        </tr>
  </thead>
  <tbody>
    <tr>
      <th>PCA.3D</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.PCA.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.PCA.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.PCA.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.PCA.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.PCA.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.PCA.3D.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>PCA.2PCs</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.PCA.2PCs.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.PCA.2PCs.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.PCA.2PCs.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.PCA.2PCs.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.PCA.2PCs.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.PCA.2PCs.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>PCA.grid</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.PCA.grid.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.PCA.grid.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.PCA.grid.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.PCA.grid.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.PCA.grid.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.PCA.grid.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>PCA.components_matrix</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.PCA.components_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.PCA.components_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.PCA.components_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.PCA.components_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.PCA.components_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.PCA.components_matrix.tsv" target="_blank">Download tsv</a></td>
    </tr>
    <tr>
      <th>PCA.loadings</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.PCA.loadings.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.PCA.loadings.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.PCA.loadings.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.PCA.loadings.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.PCA.loadings.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.PCA.loadings.tsv" target="_blank">Download tsv</a></td>
    </tr>
    <tr>
      <th>PCA.loadings_matrix</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.PCA.loadings_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.PCA.loadings_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.PCA.loadings_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.PCA.loadings_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.PCA.loadings_matrix.tsv" target="_blank">Download tsv</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.PCA.loadings_matrix.tsv" target="_blank">Download tsv</a></td>
    </tr>
    <tr>
      <th>tSNE.3D</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.tSNE.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.tSNE.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.tSNE.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.tSNE.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.tSNE.3D.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.tSNE.3D.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>tSNE.2nc</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.tSNE.2nc.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.tSNE.2nc.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.tSNE.2nc.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.tSNE.2nc.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.tSNE.2nc.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.tSNE.2nc.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>UMAP.3D.n_neighbors_20</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.UMAP.3D.n_neighbors_20.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.UMAP.3D.n_neighbors_20.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.UMAP.3D.n_neighbors_20.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.UMAP.3D.n_neighbors_20.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.UMAP.3D.n_neighbors_20.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.UMAP.3D.n_neighbors_20.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>UMAP.3D.n_neighbors_10</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.UMAP.3D.n_neighbors_10.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.UMAP.3D.n_neighbors_10.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.UMAP.3D.n_neighbors_10.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.UMAP.3D.n_neighbors_10.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.UMAP.3D.n_neighbors_10.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.UMAP.3D.n_neighbors_10.html" target="_blank">Open</a></td>
    </tr>
    <tr>
      <th>UMAP.3D.n_neighbors_5</th>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.Significant.Signature.UMAP.3D.n_neighbors_5.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.COV.All.Signature.UMAP.3D.n_neighbors_5.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.ssGSEA.MSigDB.UMAP.3D.n_neighbors_5.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.CombinedDiff.UMAP.3D.n_neighbors_5.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Combat.UMAP.3D.n_neighbors_5.html" target="_blank">Open</a></td>
      <td><a href="https://stjudecab_epi.gitlab.io/covidexpressdata/Cluster/GSEA.TPM.Original.UMAP.3D.n_neighbors_5.html" target="_blank">Open</a></td>
    </tr>
  </tbody>
</table>
<br>

<table style="border-spacing: 10px;" border="1" class="dataframe table-bordered">
<thead>
<tr style="text-align: center;">
<th>Column/Row</th>
<th>Meaning</th>
</tr>
</thead>

<tbody>
<tr>
<th>Score:ssGSEA</th>
<td>Clustering using single-sample Gene Set Enrichment Analysis Score (<a target="_blank" href="https://www.genepattern.org/modules/docs/ssGSEAProjection">ssGSEA</a>)</td>
</tr>
<tr>
<th>Score:TPM</th>
<td>Clustering using expression value Transcripts Per Million(<a target="_blank" href="https://www.rna-seqblog.com/rpkm-fpkm-and-tpm-clearly-explained/">TPM</a>)</td>
</tr>

<tr>
<th>Data:COV.Significant</th>
<td>ssGSEA score were using genesets from pre-computed differential analysis(<a target="_blank" href="https://doi.org/10.1186/gb-2014-15-2-r29">Using Voom</a>), only genes significant(fold change &gt; 2, False Discovery Rate corrected p-value &lt; 0.05) were considered for each differential analysis.</td>
</tr>


<tr>
<th>Data:COV.All.Signature</th>
<td>ssGSEA score were using genesets from pre-computed differential analysis(<a target="_blank" href="https://doi.org/10.1186/gb-2014-15-2-r29">Using Voom</a>), genes passed different levels of cutoff or top regulated genes were all considered for each differential analysis.</td>
</tr>

<tr>
<th>Data:MSigDB</th>
<td>ssGSEA score were using genesets from Molecular Signatures Database(<a target="_blank" href="http://www.gsea-msigdb.org/gsea/index.jsp">MSigDB</a>)</td>
</tr>

<tr>
<th>Data:Original</th>
<td>TPM values from RSEM method(<a target="_blank" href="https://doi.org/10.1186/1471-2105-12-323">Li and Dewey,2011,BMC Bioinformatics</a>) using STAR(<a target="_blank" href="https://doi.org/10.1093/bioinformatics/bts635">Dobin et al,2013,Bioinformatics</a>)</td>
</tr>

<tr>
<th>Data:CombinedDiff</th>
<td>Only used TPM values for top1000 differential expressed genes from COV Signature(Union)</td>
</tr>

<tr>
<th>Data:BatchCorrected</th>
<td>TPM values were corrected for batch effect using Combat(<a target="_blank" href="https://bioconductor.org/packages/release/bioc/html/sva.html">From SVA R package</a>, <a target="_blank" href="https://doi.org/10.1093/biostatistics/kxj037">Johnson et al,2007,Biostatistics</a>)</td>
</tr>

<tr>
<td>–</td>
</tr>

<tr>
<th>PCA.3D</th>
<td>Three dimensions plot(PC1 vs PC2 vs PC3) from <a target="_blank" href="https://en.wikipedia.org/wiki/Principal_component_analysis">Principal component analysis</a>
</td>
</tr>
<tr>
<th>PCA.2PCs</th>
<td>Two dimensions plot(PC1 vs PC2) from <a target="_blank" href="https://en.wikipedia.org/wiki/Principal_component_analysis">Principal component analysis</a>
</td>
</tr>
<tr>
<th>PCA.grid</th>
<td>Two dimensions plots(Many vs Many) from <a target="_blank" href="https://en.wikipedia.org/wiki/Principal_component_analysis">Principal component analysis</a>
</td>
</tr>
<tr>
<th>PCA.components_matrix</th>
<td>Each sample’s projection to top principal components</td>
</tr>
<tr>
<th>PCA.loadings</th>
<td>PCA <a target="_blank" href="https://scentellegher.github.io/machine-learning/2020/01/27/pca-loadings-sklearn.html">loading</a> as each geneset or gene’s loading to top principal components</td>
</tr>
<tr>
<th>PCA.loadings_matrix</th>
<td>PCA <a target="_blank" href="https://scentellegher.github.io/machine-learning/2020/01/27/pca-loadings-sklearn.html">loading matrix</a> as each geneset or gene’s correlations to top principal components</td>
</tr>
<tr>
<th>tSNE.3D</th>
<td>Three dimensions plot from <a target="_blank" href="https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding">tSNE analysis</a>
</td>
</tr>
<tr>
<th>tSNE.2D</th>
<td>Two dimensions plot from <a target="_blank" href="https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding">tSNE analysis</a>
</td>
</tr>
<tr>
<th>UMAP.3D.n_neighbors_20</th>
<td>Three dimensions plot from <a target="_blank" href="https://umap-learn.readthedocs.io/en/latest">UMAP analysis</a> using parameter n_neighbors = 20</td>
</tr>
<tr>
<th>UMAP.3D.n_neighbors_10</th>
<td>Three dimensions plot from <a target="_blank" href="https://umap-learn.readthedocs.io/en/latest">UMAP analysis</a> using parameter n_neighbors = 10</td>
</tr>
<tr>
<th>UMAP.3D.n_neighbors_5</th>
<td>Three dimensions plot from <a target="_blank" href="https://umap-learn.readthedocs.io/en/latest">UMAP analysis</a> using parameter n_neighbors = 5</td>
</tr>


</tbody>
</table>
<br>

----
#### **FAQs**

##### **Where can I find more details**
More details could be found in our pre-print [BIORXIV/2021/444026](https://www.biorxiv.org/content/10.1101/2021.05.14.444026v1){:target="_blank"}

##### **Will the database been updated?**
Yes, we plan to update the database either Quarterly or if we found 10 new studies from public resources. Suggestion of new studies is welcome and appreciated, simple <a href="mailto:beisi.xu#stjude.org?subject=[Covidexpress]">Email Us</a> or let us know in [Our Gitter Channel](https://gitter.im/covidexpress/community){:target="_blank"}

##### **Can I compare samples from different studies?**
We strongly recommend only compare samples from the same study. Our ssGSEA approach mainly aimed at help visual so investigator could find the samples easier, but not able to overcome the batch effect. We tried batch effect correction methods such as Combat, sva, Combat-seq, quantiles normalization, they indeed reduced the batch effect. However, for many published studies, we failed reproduce the top reported genes using the corrected expression values. Thus we decided provide original TPM values as log2(TPM+1). We are investigating more on this topic and might update later if we found better solution allow meta studies.

##### **How can I plot heatmap compare within group**
You could select the samples by checkbox on the left, then choose which meta data to split by and which meta data to group by. see below for example:
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_heatmap.jpg){: style="width: 100%; margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_heatmap.jpg)

##### **How can I custimize my own groups for plots?**
Simple click "creat new category" on the left, select the samples and add to new groups. see below. 
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_add_group.jpg){: style="width: 100%; margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_add_group.jpg)

##### **How can I get differential expressed genes(DEG) results and Volcano plot?**
You could select the samples by checkbox on the left or lasso and put them into either group 1 or group2, and then compare, see below for steps.
[![]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_DEG_volcano.jpg){: style="width: 100%; margin-left: 30px; margin-right: 30px; border: 10px"}]({{ site.url }}{{ site.baseurl }}/images/codepic/covidexpress_DEG_volcano.jpg)


##### More...

##### **What does "Diff. groups" mean in "Split by" or "Group by" meta data**
{:.no_toc}
Those were the samples you selected either checkbox or lasso function after you click "1:" or "2:" for differential expression analysis. For details, check "Compare expression of multiple genes" part of [Learn about cellxgene basical functions](https://chanzuckerberg.github.io/cellxgene/posts/gallery){:target="_blank"}

##### **Why the GSEA results different when I re-run**
{:.no_toc}
To reduce the time use, our GSEA run permutation 100 times, this increased variation of enrichment score calculation. In our tests, the exactly value might be different but the stable signal remains the same. We suggest use the GSEA plot as evidence. We will also implement the feature to allow user select permutation times later.

##### **Why I encountered "Unexpected HTTP response 400, BAD REQUEST"**
{:.no_toc}
This usually happens because the group you tried to plot doesn't contain samples. We went through many tests and tried to avoid this. You could also try [open a browser using in private/incognito mode](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DAndroid&hl=en){:target="_blank"} and let us know in [Our Gitter Channel](https://gitter.im/covidexpress/community){:target="_blank"}

##### **Why I encountered "Unexpected HTTP error" or "Failure loading source"?**
{:.no_toc}
This usually happens when an user tried to plot his customized sample group annotation but didn't add samples to that group. As tempory solution, please [open a browser using in private/incognito mode](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DAndroid&hl=en){:target="_blank"} and let us know in [Our Gitter Channel](https://gitter.im/covidexpress/community){:target="_blank"}

##### **Why the download button for figures didn't work**
{:.no_toc}
There are some technical difficulties to allow that feature due to the javascript plugin used. You could still download the high resolution svg figure using right-click -> "save image as".

##### **How do report bugs**
{:.no_toc}
Please let us know in [Our Gitter Channel](https://gitter.im/covidexpress/community){:target="_blank"}
