"""Utility functions for the web application."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdown as md  # type: ignore[import]
import yaml  # type: ignore[import]

from webapp.models import Article

APP_DIR = Path(__file__).resolve().parent
REPO_DIR = APP_DIR.parent
REPORTS_DIR = REPO_DIR / "site" / "_reports"
META_FILE = APP_DIR / "data" / "articles_meta.json"


def load_meta() -> Dict[str, Any]:
    """Load the metadata for the articles.

    Returns:
        A dictionary with the article IDs as keys and the metadata as values.
    """
    if META_FILE.exists():
        with META_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_meta(meta: Dict[str, Any]) -> None:
    """Save the metadata for the articles to a JSON file.

    Args:
        meta (Dict[str, Any]): A dictionary with the article IDs as keys and the metadata as values.
    """
    META_FILE.parent.mkdir(parents=True, exist_ok=True)
    with META_FILE.open("w", encoding="utf-8") as file:
        json.dump(meta, file, indent=2)


def parse_markdown(path: Path) -> Optional[Article]:
    """Parse a markdown file and extract article metadata and content.

    Args:
        path (Path): Path to the markdown file.

    Returns:
        Optional[Article]: An Article object if parsing is successful, otherwise None.
    """
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
    """Load all articles from the reports directory and enrich them with metadata.

    Returns:
        List[Article]: A list of Article objects sorted by date in descending order.
    """
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
    articles.sort(key=lambda article: article.date, reverse=True)
    return articles


ALL_ARTICLES: List[Article] = load_articles()


def save_article_meta(article: Article) -> None:
    """Save or update the metadata for a single article.

    Args:
        article (Article): The Article object whose metadata should be saved.
    """
    meta = load_meta()
    meta[article.id] = {
        "tags": article.tags,
        "likes": article.likes,
        "dislikes": article.dislikes,
        "topic": article.topic,
    }
    save_meta(meta)


def filter_articles(category: str, tag: Optional[str], search: str, topic: Optional[str]) -> List[Article]:
    """Filter articles by category, tag, search query, and topic.

    Args:
        category (str): The category to filter articles by.
        tag (Optional[str]): The tag to filter articles by.
        search (str): The search query to filter articles by title or summary.
        topic (Optional[str]): The topic to filter articles by.

    Returns:
        List[Article]: A list of filtered Article objects.
    """
    result = [article for article in ALL_ARTICLES if article.category == category]
    if tag:
        result = [article for article in result if tag in article.tags]
    if topic:
        result = [article for article in result if article.topic == topic]
    if search:
        q = search.lower()
        result = [article for article in result if q in article.title.lower() or q in article.summary.lower()]
    return result


def paginate(items: List[Article], page: int, per_page: int = 20) -> Tuple[List[Article], bool]:  # noqa: WPS221
    """Paginate a list of articles.

    Args:
        items (List[Article]): The list of articles to paginate.
        page (int): The current page number (1-based).
        per_page (int): Number of articles per page. Defaults to 20.

    Returns:
        Tuple[List[Article], bool]: A tuple containing the list of articles for the current page and a boolean
            indicating if there are more pages.
    """
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end], end < len(items)
