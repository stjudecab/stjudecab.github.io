---
layout: member
title: Lei Li
position: Sr. Bioinoformatics Research Scientist
handle: lei
email: lei.li@stjude.org
twitter:
github: stjudecab
googlescholar: 3qt2VoAAAAAJ
myncbi: 
photo: tm_lei.jpg
stjude: 
orcid: 0000-0002-8828-5199
linkedin: lei-li-46713b78
bibfile: tm_lei
years: [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Lei
scholar_first_name_bold: Lei
---

### Overview
Dr. Lei Li is a senior bioinformatics research scientist at St. Jude Children's Research Hospital, He is particularly interested in the development and application of bioinformatics methods in single-cell sequencing.

His expertise includes analyisis, integration and intepretation of transcriptomics and genomics data:

- RNA-Seq, scRNA-Seq
- ATAC-Seq, scATAC-Seq
- NGS, virus genome assembly
- Phylogenetoic analysis


### Education
- PhD,  Xiamen University, Xiamen, China (2015)
- MS, Xian Jiaotong University, Xian, China (2011)

### Professional Experience

Time        | Position                   | PI/Supervisor    | Institution                                   |
----------- | :-----------               | -----------      | -----------                                   |
2022-       | Sr. Bioinformatics         | Yiping Fan       | St. Jude Children's Research Hospital         |
            | Research Scientist         |                  |                                               |
2022-2022   | Research Assistant         | Patrick Wilson   | Weill Cornell Medicine                        |
            | Professor                  |                  |                                               |
2021-2022   | Senior Bioinformatics      | Patrick Wilson   | Weill Cornell Medicine                        |
            | Analyst                    |                  |                                               |
2019-2021   | Postdoctoral Scholar       | Patrick Wilson   | The University of Chicago                     |
            |                            |                  |                                               |
2015-2018   | Postdoctoral Scholar       | Xiufeng Wan      | Mississippi State University                  |
            |                            |                  |                                               |

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
