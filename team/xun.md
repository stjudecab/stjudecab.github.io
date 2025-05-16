---
layout: member
title: Xun Zhu
position: Bioinformatics Resch Scientist
handle: xun
email: xun.zhu@stjude.org
twitter:
github: stjudecab
googlescholar: iMHMSRsAAAAJ
photo: tm_xun.jpg
stjude: z/xun-zhu
orcid: 0000-0001-9097-7824
linkedin: xun-zhu-b6487918
bibfile: tm_xun
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Xun
scholar_first_name_bold: Xun
---

### Overview
Dr. Xun Zhu is a Bioinformatics Research Scientist in the Center for Applied Bioinformatics at St Jude Children's Research Hospital. His work focuses on the design and development of a next-generation bioinformatics workflow platform that would enable streamlined, collaborative, and reproducible biological data analysis.

### Education
- PhD, Molecular Biosciences and Bioengineering, University of Hawaii at Manoa
- MS, Applied Mathematics, University of Southern California
- BS, Mathematics and Applied Mathematics, Tianjin Polytechnic University

### Professional Experience

Time           | Position                          | PI/Supervisor | Institution                                        |
-----------    | :-----------                      | -----------   | -----------                                        |
2019 - Current | Bioinformatics Research Scientist | Gang Wu       | St. Jude Children's Research Hospital, Memphis, TN |
2019           | Postdoctoral Researcher           | John Shepherd | University of Hawaii Cancer Center, Honolulu, HI   |
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
