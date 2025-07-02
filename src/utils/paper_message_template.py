"""Message template for the paper."""

from src.utils.schemas import Paper

message_template = """\
(づ｡◕‿‿◕｡)づ  ✨  *New Scroll of Knowledge Detected!*  ✨

🏮 **{title}** 🏮
✍️  *Authored by*: {authors}

🎤 **Quick Synopsis, senpai!**
{summary}

🔍 **Link to Full Report**: [(~˘▾˘)~]({report_url})

📚 **ArXiv Portal**: {arxiv_url}

📈 **Citations Collected**: {citation_count} 📜
"""


def prepare_message(paper: Paper, report_url: str) -> str:
    """Prepare the message for the paper.

    Args:
        paper (Paper): The paper to prepare the message for.
        report_url (str): The URL of the report.

    Returns:
        str: The prepared message.
    """
    authors_merits = []
    for author in paper.authors:
        name = f"- {author.name}, "
        h_index = f"h-index: {author.h_index}, " if author.h_index else ""
        paper_count = f"papers: {author.paper_count}, " if author.paper_count else ""
        citation_count = f"citations: {author.citation_count}" if author.citation_count else ""
        authors_merits.append(f"{name}{h_index}{paper_count}{citation_count}")
    return message_template.format(
        title=paper.title,
        authors="\n ".join(authors_merits),
        summary=paper.summary,
        report_url=report_url,
        arxiv_url=paper.arxiv_url,
        citation_count=paper.citation_count,
    )
