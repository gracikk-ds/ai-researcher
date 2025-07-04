from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from flask import Flask, render_template, request, redirect, url_for
import markdown as md
import yaml

APP_DIR = Path(__file__).resolve().parent
REPO_DIR = APP_DIR.parent
REPORTS_DIR = REPO_DIR / "site" / "_reports"
META_FILE = APP_DIR / "data" / "articles_meta.json"

app = Flask(__name__)


def load_meta() -> Dict[str, Any]:
    if META_FILE.exists():
        with open(META_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_meta(meta: Dict[str, Any]) -> None:
    META_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)


class Article:
    def __init__(
        self, identifier: str, title: str, date: str, summary: str, content: str, path: str, meta: Dict[str, Any]
    ):
        self.id = identifier
        self.title = title
        self.date = date
        self.summary = summary
        self.content = content
        self.path = path
        self.tags: List[str] = meta.get("tags", [])
        self.likes: int = meta.get("likes", 0)
        self.dislikes: int = meta.get("dislikes", 0)
        self.topic: str = meta.get("topic", "general")

    @property
    def category(self) -> str:
        if self.dislikes > 0 and self.dislikes >= self.likes:
            return "useless"
        if self.likes > 0:
            return "helpful"
        return "inbox"


def parse_markdown(path: Path) -> Optional[Article]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    header = yaml.safe_load(parts[1])
    body = parts[2].strip()
    title = header.get("title", path.stem)
    date = header.get("date", "")
    html = md.markdown(body)
    summary = body.split("\n", 1)[0]
    return Article(str(path), title, date, summary, html, str(path), {})


def load_articles() -> List[Article]:
    meta = load_meta()
    articles: List[Article] = []
    for md_file in REPORTS_DIR.rglob("*.md"):
        art = parse_markdown(md_file)
        if art is None:
            continue
        extra = meta.get(art.id, {})
        art.tags = extra.get("tags", [])
        art.likes = extra.get("likes", 0)
        art.dislikes = extra.get("dislikes", 0)
        art.topic = extra.get("topic", "general")
        articles.append(art)
    articles.sort(key=lambda a: a.date, reverse=True)
    return articles


def save_article_meta(article: Article) -> None:
    meta = load_meta()
    meta[article.id] = {
        "tags": article.tags,
        "likes": article.likes,
        "dislikes": article.dislikes,
        "topic": article.topic,
    }
    save_meta(meta)


ALL_ARTICLES: List[Article] = load_articles()


def filter_articles(category: str, tag: Optional[str], search: str, topic: Optional[str]) -> List[Article]:
    result = [a for a in ALL_ARTICLES if a.category == category]
    if tag:
        result = [a for a in result if tag in a.tags]
    if topic:
        result = [a for a in result if a.topic == topic]
    if search:
        q = search.lower()
        result = [a for a in result if q in a.title.lower() or q in a.summary.lower()]
    return result


def paginate(items: List[Article], page: int, per_page: int = 20) -> tuple[List[Article], bool]:
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end], end < len(items)


@app.route("/")
def index() -> str:
    page = int(request.args.get("page", 1))
    tag = request.args.get("tag")
    search = request.args.get("search", "")
    filtered = filter_articles("inbox", tag, search, None)
    articles, has_next = paginate(filtered, page)
    tags = sorted({t for a in ALL_ARTICLES for t in a.tags})
    return render_template(
        "index.html",
        articles=articles,
        tags=tags,
        page=page,
        has_next=has_next,
        title="Inbox",
    )


@app.route("/helpful")
def helpful() -> str:
    page = int(request.args.get("page", 1))
    tag = request.args.get("tag")
    search = request.args.get("search", "")
    filtered = filter_articles("helpful", tag, search, None)
    articles, has_next = paginate(filtered, page)
    tags = sorted({t for a in ALL_ARTICLES for t in a.tags})
    return render_template(
        "index.html",
        articles=articles,
        tags=tags,
        page=page,
        has_next=has_next,
        title="Helpful",
    )


@app.route("/useless")
def useless() -> str:
    page = int(request.args.get("page", 1))
    tag = request.args.get("tag")
    search = request.args.get("search", "")
    filtered = filter_articles("useless", tag, search, None)
    articles, has_next = paginate(filtered, page)
    tags = sorted({t for a in ALL_ARTICLES for t in a.tags})
    return render_template(
        "index.html",
        articles=articles,
        tags=tags,
        page=page,
        has_next=has_next,
        title="Useless",
    )


@app.route("/topic/<topic>")
def topic_view(topic: str) -> str:
    page = int(request.args.get("page", 1))
    tag = request.args.get("tag")
    search = request.args.get("search", "")
    filtered = [a for a in ALL_ARTICLES if a.topic == topic]
    if tag:
        filtered = [a for a in filtered if tag in a.tags]
    if search:
        q = search.lower()
        filtered = [a for a in filtered if q in a.title.lower() or q in a.summary.lower()]
    articles, has_next = paginate(filtered, page)
    tags = sorted({t for a in filtered for t in a.tags})
    return render_template(
        "topic.html",
        articles=articles,
        tags=tags,
        page=page,
        has_next=has_next,
        title=f"Topic: {topic}",
        topic=topic,
    )


@app.route("/article/<path:article_id>")
def view_article(article_id: str) -> str:
    article = next((a for a in ALL_ARTICLES if a.id == article_id), None)
    if article is None:
        return "Not found", 404
    return render_template("article.html", article=article, title=article.title)


@app.route("/add", methods=["GET", "POST"])
def add_article() -> str:
    if request.method == "POST":
        title = request.form.get("title", "New Article")
        url = request.form.get("url", "")
        tags = [t.strip() for t in request.form.get("tags", "").split(",") if t.strip()]
        topic = request.form.get("topic", "general")
        identifier = f"manual:{title}"
        summary = "Summary will be generated by backend."
        content = f"<p>Placeholder for {title}. Link: {url}</p>"
        article = Article(identifier, title, "", summary, content, identifier, {})
        article.tags = tags
        article.topic = topic
        ALL_ARTICLES.insert(0, article)
        save_article_meta(article)
        return redirect(url_for("index"))
    return render_template("add_article.html", title="Add Article")


@app.post("/like/<path:article_id>")
def like_article(article_id: str):
    article = next((a for a in ALL_ARTICLES if a.id == article_id), None)
    if article:
        article.likes += 1
        save_article_meta(article)
    return redirect(request.referrer or url_for("index"))


@app.post("/dislike/<path:article_id>")
def dislike_article(article_id: str):
    article = next((a for a in ALL_ARTICLES if a.id == article_id), None)
    if article:
        article.dislikes += 1
        save_article_meta(article)
    return redirect(request.referrer or url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
