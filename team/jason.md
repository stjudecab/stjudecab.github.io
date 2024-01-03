---
layout: member
title: Jason Myers
position: Lead Bioinformatics Analyst
handle: jason
email: jason.myers@stjude.org
twitter:
github: stjudecab
googlescholar: 
photo: tm_jason.jpg
stjude: 
orcid: 
linkedin: 
bibfile: tm_jason
years: [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013,2012,2011,2010]
scholar_first_names_underline: Jason
scholar_first_name_bold: Jason
scholar_last_name_bold: Myers
scholar_last_names_underline: Myers
---

### Overview
Jason Myers is a bioinformatician specializing in next-generation sequencing data analysis. He has performed primary differential expression analysis on hundreds of RNA-Seq data sets spanning many different organisms (including non-model), biological systems, and experimental sample paradigms (patient trials, time course studies, and synergistic effect models). Additionally, he has analyzed numerous DNA-Seq, ChIP-Seq, miRNA-Seq, single cell RNA-Seq, and Methyl-Seq data sets following these projects from inception to publication. In order to accomplish this scale of data analysis he designs, tests, and validates software and software pipelines in high-performance computing environments.

### Education
- MS, Bioinformatics, Rochester Institute of Technology, Rochester, NY
- BS, Bioinformatics, Rochester Institute of Technology, Rochester, NY
- AS, Computer Science, Corning Community College, Corning, NY


### Professional Experience

Time           | Position                    | PI/Supervisor      | Institution                                        |
-----------    | :-----------                | -----------        | -----------                                        |
2020 - Current | Lead Bioinformatics Analyst | Evadnie Rampersaud | St. Jude Children's Research Hospital, Memphis, TN |
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

<nobr><em>*</em>denotes equal contribution</nobr>
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
