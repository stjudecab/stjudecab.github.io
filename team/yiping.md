---
layout: member
title:  Yiping Fan
position: Associate Director (Transcriptomics) 
handle: yiping 
email: yiping.fan@stjude.org
github: stjudecab
myncbi: 1ruegfsDfheQ8 
photo: tm_yiping.jpg
stjude: y/yiping-fan
linkedin: yipingfan 
bibfile: tm_yiping 
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]
scholar_first_names_underline: Yiping 
scholar_first_name_bold: Yiping
---

### Overview
Dr. Yiping is a associate director of Center for Applied Bioinformatics at St. Jude Children's Research Hospital. His research interests include Bioinformatics method development and optimization, biomedical application of machine learning, epigenetic regulation of T-cell functions and cancer immunotherapy


### Education
- PhD, Bioengineering, University of California at San Diego
- MS,  Biophyics and physiology, University of Illinois at Urbana Champaign
- BS,  Biomedical Engineering, Zhejiang University

### Professional Experience

Time        | Position                   | PI/Supervisor | Institution                           |
----------- | :-----------               | -----------   | -----------                           |
2020-       | Associate Director         | Gang Wu       | St. Jude Children's Research Hospital |
2014-2019   | Group Lead                 | Jinghui Zhang | St. Jude Children's Research Hospital |
2005-2014   | Scientist/Senior scientist | Jinghui Zhang | St. Jude Children's Research Hospital |
2002-2005   | Research Scientist         | Diversa       | Diversa Co                            |
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
