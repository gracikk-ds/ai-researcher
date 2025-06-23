---
layout: default        # or whatever layout you already use
title: Reports
---

<ul>
{% for rep in site.reports %}
  <li><a href="{{ rep.url | relative_url }}">{{ rep.title }}</a></li>
{% endfor %}
</ul>
