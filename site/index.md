---
layout: default
title: Reports
---

<ul>
{% for rep in site.reports %}
  <li>
    <a href="{{ rep.url | relative_url }}">{{ rep.title }}</a>
    {%- comment -%}
      1. Grab everything after “## 1. Motivation of the Paper”
      2. Stop at the next “##” (next section)
    {%- endcomment -%}
    {% assign parts      = rep.content | split: '## 1. Motivation of the Paper' %}
    {% if parts.size > 1 %}
      {% assign after_hdr = parts[1]   | split: '##' %}
      {% assign raw_desc  = after_hdr[0] | strip %}
      <p class="report-description">
        {{ raw_desc | markdownify | strip }}
      </p>
    {% endif %}
  </li>
{% endfor %}
</ul>
