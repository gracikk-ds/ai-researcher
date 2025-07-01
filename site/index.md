---
layout: default
title: Reports
---

<ul class="report-list">
{% for rep in site.reports %}
  <li class="report-item">
    <h3 class="report-title">
      <a href="{{ rep.url | relative_url }}">
        {{ rep.title | replace: "_", " " }}
      </a>
    </h3>
    {% assign html         = rep.content | replace: '\r\n', '\n' %}
    {% assign parts        = html | split: '<h2 id="1-motivation-of-the-paper">' %}
    {% if parts.size > 1 %}
      {%- assign after_hdr = parts[1] | split: '</h2>' -%}
      {%- assign remainder = after_hdr[1] -%}
      {%- assign desc_html = remainder | split: '<h2' | first -%}
      <p class="report-description">
        {{ desc_html | strip_html | markdownify | truncatewords: 100 }}
      </p>
    {% endif %}
  </li>
{% endfor %}
</ul>
