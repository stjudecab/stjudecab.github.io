---
title: "Team"
layout: gridlay
excerpt: "- Team members"
sitemap: true
permalink: /Transcriptomics_team/
group: Transcriptomics
groupcolor: "#FDB71A"
groupspec: [ "team/" ] 
---

{% assign teamurlbase = site.url | append: site.baseurl | append: "/team/" %}

## Team Members of {{ page.group }}

{% assign grpmember = site.data.team_members | where: "group", page.group %}
---

### Group Lead
{% assign number_printed = 0 %}
{% for member in grpmember %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.posgroup == 0 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <a href="{{ teamurlbase }}{{ member.url }}" class="off">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  </a>
  <h4><a href="{{ teamurlbase }}{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

### Scientist
{% assign number_printed = 0 %}
{% for member in grpmember %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.posgroup == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <a href="{{ teamurlbase }}{{ member.url }}" class="off">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  </a>
  <h4><a href="{{ teamurlbase }}{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
---

### Contact
Please contact our group lead, <a href="mailto:yiping.fan#stjude.org">Yiping Fan</a>.

