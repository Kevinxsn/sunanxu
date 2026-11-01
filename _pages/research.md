---
layout: page
permalink: /research/
title: research
description: Algorithms and machine learning for biological discovery.
nav: true
nav_order: 1
---

I build computational methods for reconstructing biological sequences, understanding gene regulation, and evaluating machine learning models. My work brings together algorithm design, biological measurements, and learned representations.

{% assign research = site.data.cv.cv.sections.Experience | where: "type", "research" %}
{% for experience in research %}

## {{ experience.position }}

**{{ experience.company }}**<br>
{{ experience.department }}{% if experience.period %} · {{ experience.period }}{% endif %}

{% if experience.summary %}
{{ experience.summary }}
{% endif %}

{% for highlight in experience.highlights %}

- {{ highlight }}
  {% endfor %}

{% if experience.reserved %}

<!-- Tiffany's experience is intentionally blank. Add it in _data/cv.yml. -->
<div aria-label="Space reserved for my experience with Tiffany" style="min-height: 5rem;"></div>
{% endif %}

{% unless forloop.last %}

<hr>

{% endunless %}
{% endfor %}

[Read my publications]({{ '/publications/' | relative_url }})
