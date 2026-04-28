---
layout: member
title: Beifang Niu
position: Senior Bioinformatics Research Scientist(Genomics)
handle: Beifang
email: beifang.niu@stjude.org
twitter:
github: stjudecab
googlescholar: GS6CPtgAAAAJ
photo: tm_beifang.jpg
stjude: x/beifang-niu
linkedin: beifang-niu-7bb19563
bibfile: tm_beifang
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
scholar_first_names_underline: Beifang
scholar_first_name_bold: Beifang
---

### Overview

Dr. Beifang Niu is a Senior Bioinformatics Research Scientist at the Genomics Group, the Center for Applied Bioinformatics (CAB) in the St Jude Children’s Research Hospital (SJCRH). He is a bioinformatics researcher with over 20 years of experience in genome informatics and high-performance computing, focusing on pan-cancer genomics. His work integrates omics data, machine learning, and algorithm development to identify tumor-specific drivers, such as **microsatellite instability (MSI)** and pan-cancer spacial somatic **mutation hotspots**. As the principal developer of widely used software such as MSIsensor, HotSpot3D, and the CD-HIT suite, his research has contributed to over 80 publications with more than 40,000 citations, advancing the fields of cancer genomics and precision medicine.


### Education
- PhD, Computer Science (Bioinformatics), University of Chinese Academy of Sciences, Beijing, China (2009)
- Research Fellowship, Genome Informatics, Beijing Genomics Institute (BGI), Beijing, China (2007)
- BS, Coumputer Science, Shandong Agricultural University, Shandong, China (2002)

### Professional Experience

Time        | Position                   | PI/Supervisor    | Institution                                                                                      |
----------- | :-----------               | -----------      | -----------                                                                                      |
2025-       | Senior Bioinformatics Research Scientist      | Gang Wu /Ti-Cheng Chang | St. Jude Children's Research Hospital, Memphis, TN, USA                |
2015-2025   | Professor                  | -                | Computer Network Information Center, Chinese Acedemy of Sciences, Beijing, China                 |
2012-2015   | Staff Research Scientist   | Li Ding          | McDonnell Genome Institute, Washington University in St. Louis, MO, USA                          |
2009-2012   | Postdoctoral Fellow        | Weizhong Li      | Center for Research in Biological Systems, University of California San Diego, CA, USA           |

{:.custom-table}

<!--more-->


### 📌 Bioinformatics Tools

---

- **MSIsensor**  
  A fast and accurate microsatellite instability (MSI) detection tool for paired tumor-normal sequencing data.  
  👉 [Paper (PMID: 24371154)](https://www.ncbi.nlm.nih.gov/pubmed/24371154) \| [GitHub](https://github.com/ding-lab/msisensor)

- **MSIsensor2**  
  An improved MSI detection machine learning model supporting both paired and unpaired tumor samples.  
  👉 [Paper (PMID: 33461213)](https://www.ncbi.nlm.nih.gov/pubmed/33461213) \| [GitHub](https://github.com/niu-lab/msisensor2)

- **HotSpot3D** 
  A tool for identifying spatial variant hotspots (clusters), functionally important cancer mutations using protein 3D structure.  
  👉 [Paper (PMID: 25837912)](https://www.ncbi.nlm.nih.gov/pubmed/25837912) \| [GitHub](https://github.com/ding-lab/hotspot3d)

- **HotSpot3D Web Server**  
  An interactive web platform for visualizing and analyzing spatial clusters of somatic mutations in protein 3D structures.  
  👉 [Paper (PMID: 32315389)](https://www.ncbi.nlm.nih.gov/pubmed/32315389) \| [Web Server](http://niulab.scgrid.cn/HotSpot3D/)

- **Docker-FLT3-ITD**  
  A Docker image for accurate FLT3-internal tandem duplication (FLT3-ITD) identification in acute myeloid leukaemia (AML).  
  👉 [Paper (PMID: 33851200)](https://www.ncbi.nlm.nih.gov/pubmed/33851200) \| [github](https://github.com/niu-lab/docker-flt3-itd)

- **CD-HIT**  
  A widely used tool for clustering and comparing large sets of protein or nucleotide sequences at high speed.  
  👉 [Paper (PMID: 23060610)](https://www.ncbi.nlm.nih.gov/pubmed/23060610) \| [Website](https://sites.google.com/view/cd-hit/home)

---


### Selected Publications

For a full list - 
{% if page.googlescholar %} [Google Scholar](https://scholar.google.com/citations?user={{page.googlescholar}}){:target="_blank"}
{% endif %} {% if page.myncbi %}, or [Pubmed](https://www.ncbi.nlm.nih.gov/myncbi/{{page.myncbi}}/bibliography/public/){:target="_blank"}{% endif %}



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
