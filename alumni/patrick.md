---
layout: member
title: Patrick Schreiner
position: Bioinoformatics Research Scientist
handle: patrick
email: patrick.schreiner@stjude.org
twitter: pschreins
github: stjudecab
googlescholar:
myncbi: 1ZmoCXANKssI1v
photo: tm_patrick.jpg
stjude: x/patrick-schreiner
orcid: 0000-0001-5391-2642
linkedin: patrick-schreiner-phd
bibfile: tm_patrick
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017]
scholar_first_names_underline: Patrick
scholar_first_name_bold: Patrick
---

### Overview
Patrick's graduate research was focused on the origin and function of sRNA mainly in the yellow fever mosquito.  In addition to mosquito samples, Patrick also has experience in analyzing data from bacteria, yeast, ferret, mice, and human samples. He received his Ph.D. in Genetics, Genomics, and Bioinformatics from the University of California, Riverside in 2017 before coming to St. Jude as a Bioinformatics Research Scientist.  Patrick has led the execution of projects that mine and analyze big data from internal and external datasets. His particular research areas of interest include Transcriptomics, Immunology, and Single-Cell Omics.

NGS Data that Patrick knows how to analyze:

- RNA-Seq
- scRNA-Seq
- scATAC-Seq
- Microarray (Expression)
- WGBS/TEBS

### Education
- PhD, University of California, Riverside (2017)
- BS, Loyola University of Chicago (2012)

### Professional Experience

Time        | Position                   | PI/Supervisor    | Institution                                   |
----------- | :-----------               | -----------      | -----------                                   |
2017-       | Bioinformatics	         | Gang Wu /        | St. Jude Children's Research Hospital         |
            | Research Scientist         | Yiping Fan       |                                               |
{:.custom-table}


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
