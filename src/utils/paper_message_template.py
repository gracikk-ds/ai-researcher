"""Message template for the paper."""

from typing import List

from src.utils.schemas import Author, Paper

message_template = """\
(づ｡◕‿‿◕｡)づ  ✨  *New Scroll of Knowledge Detected!*  ✨

*{title}*

✍️  *Authored by*: {authors}

🎤 *Quick Synopsis, senpai!*
{summary}

🔍 *Link to Summary Report*: [(~˘▾˘)~]({report_url})

📚 *ArXiv Portal*: {arxiv_url}

📈 *Citations Collected*: {citation_count} 📜

"""

message_for_skipped_papers = """✨  Koi wa, senpai!  ✨

I've found some interesting papers. Probably, they are not about generative image editing directly.
But maybe you will find them useful for your research.

Here are the titles of the papers:
{skipped_titles}
"""


def add_authors_merits(authors: list[Author]) -> str:
    """Get the merits of the authors.

    Args:
        authors (list[Author]): The authors of the paper.

    Returns:
        str: The merits of the authors.
    """
    authors_merits = []
    for author in authors:
        name = f"\n- {author.name}"
        h_index = f", h-index: {author.h_index}, " if author.h_index else ""
        paper_count = f"papers: {author.paper_count}, " if author.paper_count else ""
        citation_count = f"citations: {author.citation_count}" if author.citation_count else ""
        authors_merits.append(f"{name}{h_index}{paper_count}{citation_count}")
    return "".join(authors_merits)


def prepare_message(paper: Paper, report_url: str) -> str:
    """Prepare the message for the paper.

    Args:
        paper (Paper): The paper to prepare the message for.
        report_url (str): The URL of the report.

    Returns:
        str: The prepared message.
    """
    return message_template.format(
        title=paper.title,
        authors=add_authors_merits(paper.authors),
        summary=paper.summary,
        report_url=report_url,
        arxiv_url=paper.arxiv_url,
        citation_count=paper.citation_count,
    )


def prepare_message_for_skipped_papers(skipped_titles: List[str]) -> str:  # noqa: WPS118
    """Prepare the message for the skipped papers.

    Args:
        skipped_titles (List[str]): The titles of the skipped papers.

    Returns:
        str: The prepared message.
    """
    return message_for_skipped_papers.format(skipped_titles="\n".join(skipped_titles))
