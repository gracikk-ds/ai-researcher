# Web Interface API

This document describes the HTTP API exposed by the Flask based site.  The
application lives in the `webapp` package with request handlers defined in
`webapp/routes.py`.

## Endpoints

### `GET /`
List articles in the *Inbox* category. Supports query parameters:
- `page` – page number (default `1`).
- `tag` – filter articles by a tag.
- `search` – free text search in title and summary.

### `GET /helpful`
List articles that received likes.

### `GET /useless`
List articles that were disliked.

### `GET /topic/<topic>`
List articles associated with the given topic.

### `GET /article/<id>`
Show the full article content.

### `GET /add`
Display a form for manually adding an article.

### `POST /add`
Add a new article. Expected form fields:
- `title` – article title.
- `url` – link to arXiv page or PDF.
- `tags` – comma separated list of tags.
- `topic` – topic name.

A placeholder summary is created until a backend service generates the real one.

### `POST /like/<id>`
Increase the like counter of an article. The article is moved to the *Helpful* category.

### `POST /dislike/<id>`
Increase the dislike counter of an article. The article is moved to the *Useless* category.

All endpoints return standard HTML pages. They can be used as the basis for a future JSON API once the backend is implemented.
