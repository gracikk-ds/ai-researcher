from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdown as md
import yaml

from .models import Article

APP_DIR = Path(__file__).resolve().parent
REPO_DIR = APP_DIR.parent
REPORTS_DIR = REPO_DIR / "site" / "_reports"
META_FILE = APP_DIR / "data" / "articles_meta.json"


def load_meta() -> Dict[str, Any]:
    if META_FILE.exists():
        with META_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_meta(meta: Dict[str, Any]) -> None:
    META_FILE.parent.mkdir(parents=True, exist_ok=True)
    with META_FILE.open("w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)


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
    return Article(str(path), title, date, summary, html, str(path))


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


ALL_ARTICLES: List[Article] = load_articles()


def save_article_meta(article: Article) -> None:
    meta = load_meta()
    meta[article.id] = {
        "tags": article.tags,
        "likes": article.likes,
        "dislikes": article.dislikes,
        "topic": article.topic,
    }
    save_meta(meta)


def filter_articles(
    category: str, tag: Optional[str], search: str, topic: Optional[str]
) -> List[Article]:
    result = [a for a in ALL_ARTICLES if a.category == category]
    if tag:
        result = [a for a in result if tag in a.tags]
    if topic:
        result = [a for a in result if a.topic == topic]
    if search:
        q = search.lower()
        result = [a for a in result if q in a.title.lower() or q in a.summary.lower()]
    return result


def paginate(items: List[Article], page: int, per_page: int = 20) -> Tuple[List[Article], bool]:
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end], end < len(items)
