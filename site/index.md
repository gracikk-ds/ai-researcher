---
layout: default
title: Reports
---

<ul>
{% for rep in site.reports %}
  <li>
    <a href="{{ rep.url | relative_url }}">{{ rep.title }}</a>
    <p class="report-description">
      {{ rep.content | strip_html | truncatewords: 20 }}
    </p>
  </li>
{% endfor %}
</ul>
