---
layout: member
title: Beisi Xu
position: Principal Bioinformatics Research Scientist(Epigenetics)
handle: beisi
email: beisi.xu@stjude.org
twitter:
github: stjudecab
googlescholar: PIPGxWoAAAAJ
myncbi: 1zofdYmKS0FQg
photo: tm_beisi.jpg
stjude: x/beisi-xu
orcid: 0000-0003-0099-858X
linkedin: beisixu
bibfile: tm_beisi
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Beisi
scholar_first_name_bold: Beisi
---

### Overview
Beisi (pronounce /bās/ as bass) is a highly motivated, skilled, communicative, independent and team-oriented PhD biologist with over 10 years of bioinformatics experience (who did not know how to play bass). He has extensive expertise in Epigenomics, Cancer Biology, Developmental Biology, and High Performance Computation.

NGS Data Beisi knows how to analyze:

- CHIP-Seq
- ATAC-Seq
- RNA-Seq
- Hi-C([Juicer](https://github.com/aidenlab/juicer){:target="_blank"})
- HiCHIP/PLAC-seq/Capture-C([HiC-Pro](https://github.com/nservant/HiC-Pro){:target="_blank"})
- scRNA-Seq([Seurat](https://satijalab.org/seurat/v3.0/immune_alignment.html){:target="_blank"}/[Pagoda](http://hms-dbmi.github.io/scde/pagoda.html){:target="_blank"})
- scATAC-Seq
- SLAM-Seq([SlamDunk](https://t-neumann.github.io/slamdunk/docs.html#docstart){:target="_blank"})
- DNase-Seq, FAIRE-Seq, MNase-Seq
- WGBS/TEBS

### Education
- PhD, University of Science and Technology of China, P.R.CHINA (2009)
- Research Fellowship, Indiana University-Purdue University at Indianapolis, USA (2007)
- BS, University of Science and Technology of China, P.R.CHINA (2003)

### Professional Experience

Time        | Position                   | PI/Supervisor    | Institution                                                |
----------- | :-----------               | -----------      | -----------                                                |
2021-       | Principal Bioinformatics   | Gang Wu /        | St. Jude Children's Research Hospital, Memphis, TN         |
            | Research Scientist         | Yiping Fan       |                                                            |
2019-2021   | Group Lead in Epigenetics  | Gang Wu /        | St. Jude                                                   |
            |                            | Yiping Fan       |                                                            |
2017-2019   | Sr. Bioinformatics         | Jinghui Zhang /  | St. Jude                                                   |
            | Research Scientist         | Yiping Fan       |                                                            |
2014-2017   | Bioinformatics             | Jinghui Zhang /  | St. Jude                                                   |
            | Research Scientist         | Yiping Fan       |                                                            |
2011-2014   | Postdoctoral Fellow        | Dustin E.Schones | City of Hope, Duarte, CA                                   |
2009-2011   | Postdoctoral Fellow        | Guohui Li        | Dalian Institute of Chemical Physics, Dalian               |
2009-2009   | Postdoctoral Fellow(Joint) | Yan Cui          | University of Tennessee Health Science Center, Memphis, TN |
2009-2009   | Internship                 | BGI              | Beijing Genomics Institute, Shenzhen                       |
2007-2008   | Research Fellow            | Yaoqi Zhou       | IUPUI, Indianapolis, IN                                    |
2003-2007   | Research Assistant         | Haojun Liang     | University of Science and Technology of China, Hefei       |
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
