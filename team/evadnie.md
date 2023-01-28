---
layout: member
title: Dr. Evadnie Rampersaud
position: Principal Bioinformatics Research Scientist(Genetics)
handle: evadnie
email: evadnie.rampersauds@stjude.org
twitter:
github: stjudecab
googlescholar:
photo: tm_evadnie.jpg
stjude:
orcid:
linkedin:
bibfile: tm_evadnie
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998]
scholar_first_names_underline: Evadnie
scholar_first_name_bold: Evadnie
---

### Overview
Dr. Evadnie Rampersaud is a genetic epidemiologist with expertise in applied statistical analyses to correlate genotype and phenotype data.  Her expertise includes family-based and population-level studies of pediatric cancer, rare nonmalignant blood diseases, and neurodegenerative disorders. Dr. Rampersaud brings over 10 years of experience in analysis of complex human traits.


### Educational Experience
- Postdoctoral Fellow, Human Genetics, University of Maryland School of Medicine, Baltimore, MD
- PhD, Genetics and Genomics, Duke University, Durham, NC
- MS, Epidemiology, University of South Florida, Tampa FL
- BS, Psychology, University of Florida, Gainesville FL

### Professional Experience

Time           | Position                                    | PI/Supervisor                        | Institution                                        |
-----------    | :-----------                                | -----------                          | -----------                                        |
2021 - current | Principal Bioinformatics Research Scientist | Gang Wu                              | St. Jude Children’s Research Hospital, Memphis, TN |
2019 - 2021    | Group Lead in Genetics                      | Gang Wu                              | St. Jude Children’s Research Hospital, Memphis, TN |
2015 - 2019    | Bioinformatics Research Scientist           | Gang Wu                              | St. Jude Children’s Research Hospital, Memphis, TN |
2007 - 2015    | Research Assistant Professor                | Leonard M. Miller School of Medicine | University of Miami, Miami, FL                     |
2005 - 2007    | Postdoctoral Fellow                         | Braxton Mitchell                     | University of Maryland, Baltimore, MD              |
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
