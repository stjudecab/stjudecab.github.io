---
layout: member
title: Hongjian Jin
position: Sr. Bioinoformatics Research Scientist
handle: hongjian
email: hongjian.jin@stjude.org
twitter:
github: stjudecab
googlescholar: V_vuP6wAAAAJ
myncbi: 1HSwfzta96x54
photo: tm_hongjian.jpg
stjude: j/hongjian-jin
orcid: 0000-0003-3833-7170
linkedin: hongjianjin
bibfile: tm_hongjian
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]
scholar_first_names_underline: Hongjian
scholar_first_name_bold: Hongjian
---

### Overview
Dr. Hongjian Jin is a senior bioinformatics research scientist at St. Jude Children's Research Hospital, He is particularly interested in understanding transcriptional regulation and its roles in childhood and adult cancer.

His expertise includes analyisis, integration and intepretation of epigenetics and transcriptomics data:

- RNA-Seq, scRNA-Seq
- ATAC-Seq, scATAC-Seq
- ChIP-Seq, CUT&RUN CUT&TAG
- FAIRE-Seq, DNase-Seq 
- Microarry, Methylation Array


### Education
- PhD,  Zhejiang University, Hangzhou, China (2007)
- MS, - Zhejiang University, Hangzhou, China (2002)

### Professional Experience

Time        | Position                   | PI/Supervisor    | Institution                                   |
----------- | :-----------               | -----------      | -----------                                   |
2019-       | Sr. Bioinformatics         | Yiping Fan       | St. Jude Children's Research Hospital         |
            | Research Scientist         |                  |                                               |
2016-2019   | Bioinformatics             | Jinghui Zhang /  | St. Jude Children's Research Hospital         |
            | Research Scientist         | Yiping Fan       |                                               |
2014-2016   | Research Assistant         | Ramana V Davuluri| Northwestern University                       |
            | Professor                  |                  |                                               |

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
{% assign start_year = page.years | last %}
{% assign current_year = site.time | date: "%Y" | plus: 0 %}
{%- assign years_string = "" -%}
{% for year in (start_year..current_year) %}
    {%- assign year_string = year_string | append: year | append: "," -%}
{%- endfor -%}
{%- assign year_array = year_string | split: "," | reverse -%}
{% for y in year_array %}
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
