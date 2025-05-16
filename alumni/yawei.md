---
layout: member
title: Yawei Hui
position: Manager (DevOps)
handle: yawei
email: yawei.hui@stjude.org
twitter:
github: bh007
googlescholar: uwON2rEAAAAJ&hl
photo: tm_yawei.jpg
stjude: h/yawei-hui
orcid: 0000-0001-6397-3086
linkedin: yaweihui
bibfile: tm_yawei
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Yawei
scholar_first_name_bold: Yawei
---

### Overview
Being an astrophysicist by training, Dr. Yawei Hui spent much of his early career in exploring the universe for special celestial objects that emit strong X-rays. With experiences accumulated in computing and analytical modeling, he took a significant turn to focus on designing and implementing HPC/Supercomputing workflow and data management system and algorithms development. Now he is taking on new challenges to apply all his data science expertise to understand biomedical data and develop efficient and powerful systems to accelerate scientific discoveries in childhood diseases.


### Education
- PhD, Astrophisics, The Johns Hopkins University, Baltimore, MD (2008)
- MS, Computer Science, University of Tennessee, Knoxville, TN (2015)
- BS, Theoretical Physics, Nanjing University, Nanjing, China (1997)

### Professional Experience

Time        | Position                   | PI/Supervisor   | Institution                           |
----------- | :-----------               | -----------     | -----------                           |
2020-2021   | Manager - DevOps           | Gang Wu         | St. Jude Children's Research Hospital |
2019-2020   | Bioinformatics Analyst III | Gang Wu         | St. Jude Children's Research Hospital |
2016-2019   | Postmaster Res. Associate  | Eric Lingerfelt | The Oak Ridge National Laboratory     |
2012-2012   | Res. Asst. Prof.           |                 | University of Tennessee, Knoxville    |
2008-2012   | Postdoc. Res. Associate    | David Schultz   | The Oak Ridge National Laboratory     |
2000-2008   | Grad. Res. Assistant       | Julian Krolik   | The Johns Hopkins University          |
1997-2000   | Grad. Res. Assistant       | Jinming Dong    | Nanjing University                    |
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
