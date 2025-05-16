---
title: "Publications"
layout: gridlay
excerpt: "- Publications"
sitemap: true
permalink: /Epigenetics_publications/
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
group: Epigenetics
groupcolor: "#8D0034"
scholar_first_names_underline: Beisi;Wojciech;Nadhir;Wenjie;Qiong
scholar_first_name_bold: Beisi
---

{% assign bibfile = page.group | append: ".clean.bib" | prepend: "grp_" %}

## Publications from {{ page.group }}

For a [full list (GEO\|SRA\|Browser\|Code) see below](#full-list)

<div class="row">
### Featured

<div class="publications_highlight">
  {% bibliography -f {{ bibfile }} --template bib_highlight -q @*[highlight] %}
</div>
</div>

<p> &nbsp; </p>

### Full List

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
<h2 class="year">{{y}}:{% bibliography_count -f {{ bibfile }} -q @*[year={{y}}]* %}</h2>
  {% bibliography -f {{ bibfile }} -q @*[year={{y}}]* %}
{% endfor %}
</div>
