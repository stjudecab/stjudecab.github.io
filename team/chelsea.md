---
layout: member
title: Chelsea Trotter
position: Bioinformatics Software Engineer
handle: chelsea
email: chelsea.trotter@stjude.org
twitter:
github: ChelseaTrotter
googlescholar: 
photo: tm_chelsea.jpg
stjude: x/chelsea-trotter
orcid: 0000-0002-8788-8043
linkedin:
bibfile: tm_chelsea.bib
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Chelsea
scholar_first_name_bold: Xiaoqi
---

### Overview
Chelsea Trotter discovered her love for software engineering in her 20s. She started with basic Java programming, and later on took a research interest in high performance computing, specially in GPUs. She now is a user of Julia, R, Python to implement workflows and acclerate algorithms for genomic research. 

### Education
- MS, Computer Science, University of Mississippi, Oxford, MS (2017)

### Professional Experience

Time        | Position                   | PI/Supervisor   | Institution                           |
----------- | -----------                | -----------     | -----------                           |
2021-       | Bioinformatics Software    | Gang Wu/        | St. Jude Children's Research Hospital |
            | Engineer                   | Yawei Hui       |                                       |
2018-2021   | Scientific Programmer      | Saunak Sen      | University of Tenneessee              |
2017-2018   | Associate Systems Engineer | Power Seawright | Autozone                              |
2015-2017   | Research Assistant         | Byunghyun Jang  | University of Mississippi             |
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
