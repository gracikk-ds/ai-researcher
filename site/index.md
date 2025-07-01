---
layout: default
title: Reports
---

<ul>
  {% for rep in site.reports %}
    <li>
      <a href="{{ rep.url | relative_url }}">{{ rep.title }}</a>
      {% comment %}
        grab the first line in rep.content that starts with “# “
      {% endcomment %}
      <p class="report-description">
        {% assign lines = rep.content | split: "\n" %}
        {% for line in lines %}
          {% if line startswith "# " %}
            {{ line | remove_first: "# " | strip }}
            {% break %}
          {% endif %}
        {% endfor %}
      </p>
    </li>
  {% endfor %}
</ul>
