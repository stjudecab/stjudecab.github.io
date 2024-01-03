---
layout: member
title: Wenchao Zhang
position: Bioinformatics Software Engineer(DevOps)
handle: wenchao
email: wenchao.zhang@stjude.org
twitter:
github: 
googlescholar: HVfLT8AAAAAJ
photo: tm_wenchao.png
stjude: z/wenchao-zhang
orcid: 0000-0003-4478-8410
linkedin: wenchao-zhang-5095044a
bibfile: tm_wenchao.bib
years: [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2016, 2015, 2014, 2012, 2011, 2008]
scholar_first_names_underline: Wenchao
scholar_first_name_bold: Wenchao
---

### Overview
Dr. Wenchao Zhang is a bioinformatics software engineer in the Center for Applied Bioinformatics (CAB) in the St Jude Children’s Research Hospital (SJCRH). He worked as an electronics engineer in his early career time and later on switched to Bioinformatics. He has since been accumulated knowledge and skills in bioinformatics software/pipeline development, including computational mass-spectrometry for proteomics and metabolomics, statistical genomics with a focus on polygenic variant analysis, epistatic GWAS mapping, NGS and HiC data analysis. He is particularly interested in utilizing HPC skills (task driven CPU parallel computing such as MPI, and data driven parallel computing such as CUDA GPU) to accelerate the bioinformatics analysis.          

### Education
- PhD, Communication & Information System, Institute of Electronics, Chinese Academy of Science, Beijing, China (2008)
- MS, Communication & Information System, Jilin University, Changchun, China (2004)
- BS, Electronics Engineering, Jilin University, Changchun, China (2001)

### Professional Experience

Time        | Position                         | PI/Supervisor   | Institution                           |
----------- | :-----------                     | -----------     | -----------                           |
2021-       | Bioinformatics Software Engineer |Yawei Hui        | St. Jude Children's Research Hospital |                                     |
2020-2021   | Computational Biologist II       |Chao Xing        | UT Southwestern Medical Center        |
2017-2020   | Computational Biologist          |Patrick Zhao     | Noble Research Institute              |
2012-2017   | Bioinformatics Research Analyst  |Patrick Zhao     | The Samuel Roberts Noble Foundation   |
2010-2012   | Postdoc. Res. Associate          |Xiuxia Du        | UNC-Charlotte & NC Research Campus    |
2007-2010   | Algorithm Engineer               |Xiaoxu Guo       | Analogix SemiConductor Inc.           |
{:.custom-table}

<!--more-->

# Publications

For a [full list (GEO\|SRA\|Browser\|Code) see below](#full-list)
{% if page.googlescholar %}, or [Google Scholar](https://scholar.google.com/citations?user={{page.googlescholar}}){:target="_blank"}
{% endif %} {% if page.myncbi %}, or [Pubmed](https://www.ncbi.nlm.nih.gov/myncbi/{{page.myncbi}}/bibliography/public/){:target="_blank"}{% endif %}


<div class="row">
  {% capture npaper %}
    {% bibliography_count -f {{ page.bibfile }} -q @*[highlight] %}
  {% endcapture %}
  {% assign npaper = npaper | plus: 0 %}
  {% if npaper > 0 %}
## Featured

<div class="publications_highlight">
  {% bibliography -f {{ page.bibfile }} --template bib_highlight -q @*[highlight] %}
</div>
{% endif %}

</div>

## Full List

<nobr><em>*</em>denotes equal contribution, <em>#</em>denotes corresponding</nobr>
<div class="publications">
{% for y in page.years %}
  {% capture npaper %}
    {% bibliography_count -f {{ page.bibfile }} -q @*[year={{y}}]* %}
  {% endcapture %}
  {% assign npaper = npaper | plus: 0 %}
  {% if npaper > 0 %}
  <h2 class="year">{{y}}:{{npaper}}</h2>
  {% bibliography -f {{ page.bibfile }} -q @*[year={{y}}]* %}
  {% endif %}
{% endfor %}
</div>
