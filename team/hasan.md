---
layout: member
title: Hasan Al Reza
position: Bioinformatics Research Scientist(Epigenetics)
handle: hasan
email: hasanal.reza@stjude.org
twitter:
github: hasanwraeth
googlescholar: YOemoSAAAAAJ
myncbi: hasan.reza.2
photo: tm_hasan.jpg
stjude: x/hreza
orcid: 0000-0002-9346-2217
linkedin: hasan-al-reza
bibfile: tm_hasan
years: [2010]
scholar_first_names_underline: Hasan
scholar_first_name_bold: Hasan
---

### Overview
**Hasan** (pronounce /hʌˈsɑːn/ as huh-SAHN) is an innovative Computational / Molecular Biologist with 5+ years of experience generating and handling Biological Big Data. I have designed pipelines for streamlined analysis of NGS data assisted by bioinformatics and machine learning algorithms that have analyzed Terabytes of data.

NGS Data Hasan knows how to analyze:

- CHIP-Seq
- ATAC-Seq
- RNA-Seq
- scRNA-Seq
- scATAC-Seq
- spatialRNA-Seq
- Microbiome-Seq
- GWAS
- WGS
- Perturb-Seq

### Education
- **PhD in Molecular and Developmental Biology** | University of Cincinnati Oct 2023
- **MS in Genetic Engineering and Biotechnology** | University of Dhaka Sep 2017
- **BS in Genetic Engineering and Biotechnology** | University of Dhaka Feb 2016

### Professional Experience

Time        | Position                   | PI/Supervisor        | Institution                                    |
----------- | :-----------               | -----------          | -----------                                    |
2025-       | Bioinformatics Research    | Beisi Xu /           | St. Jude Children's Research Hospital,         |
            | Scientist                  | Wojciech Rosikiewicz | Memphis, TN                                    |
2024-2025   | Bioinformatics Data        | Yan Xu               | Cincinnati Children's Hospital Medical Center, |
            | Scientist                  |                      | Cincinnati, OH                                 |
2023-2024   | Research Fellow            | Takanori Takebe      | CCHMC, Cincinnati, OH                          |
2018-2023   | Graduate Research Assistant| Takanori Takebe      | CCHMC, Cincinnati, OH                          |
2016-2023   | Graduate Research Assistant| M. Aftab Uddin       | University of Dhaka, Dhaka, Bangladesh         |
2014-2016   | Undergraduate Research     | Miraj Kobad          | University of Dhaka, Dhaka, Bangladesh         |
            | Assistant                  | Chowdhury            |                                                |
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
