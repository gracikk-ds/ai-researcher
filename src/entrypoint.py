"""Entrypoint for the application."""

import subprocess  # noqa: S404
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

import click
from loguru import logger

from src.ai_researcher.gemini_researcher import GeminiApiClient
from src.fetcher.arxiv_fetcher import ArxivFetcher
from src.notifier.notifier import Notifier
from src.settings import Settings
from src.utils.add_images_to_md import add_images_to_md
from src.utils.fetch_images import extract_images
from src.utils.load_pdfs import download_pdf
from src.utils.paper_message_template import prepare_message
from src.utils.schemas import Paper


class Entrypoint:
    """Entrypoint for the application."""

    def __init__(self, gemini_model_name: str = "gemini-2.5-pro", site_reports_dir: str = "site/_reports") -> None:
        """Initialize the entrypoint.

        Args:
            gemini_model_name (str): The name of the Gemini model to use.
            site_reports_dir (str): The directory to save the reports to.
        """
        self.site_reports_dir = site_reports_dir
        self.gemini_researcher = GeminiApiClient(model_name=gemini_model_name, site_reports_dir=site_reports_dir)
        with open("prompts/summarizer.txt", "r", encoding="utf-8") as summary_file:
            self.summary_prompt = summary_file.read()
        self.arxiv_fetcher = ArxivFetcher()

    def _get_keywords(
        self,
        keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
    ) -> Tuple[List[str], List[str], List[str]]:
        """Get the keywords for the arxiv search.

        Args:
            keywords (Optional[List[str]]): The keywords for arxiv search.
            exclude_keywords (Optional[List[str]]): The keywords to exclude from the search.
            categories (Optional[List[str]]): The categories for arxiv search.

        Returns:
            Tuple[List[str], List[str], List[str]]: The keywords, exclude keywords, and categories.
        """
        if keywords is None:
            logger.warning("No keywords provided, use predefined keywords.")
            keywords = self.arxiv_fetcher.predefined_keywords
        if exclude_keywords is None:
            logger.warning("No exclude keywords provided, use predefined exclude keywords.")
            exclude_keywords = self.arxiv_fetcher.exclude_keywords
        if categories is None:
            logger.warning("No categories provided, use predefined categories.")
            categories = self.arxiv_fetcher.predefined_categories
        return keywords, exclude_keywords, categories

    def download_pdfs(self, papers: List[Paper]) -> Tuple[List[str], List[str], List[str]]:  # noqa: WPS221
        """Download the PDFs for the papers.

        Args:
            papers (List[Paper]): The papers to download.

        Returns:
            Tuple[List[str], List[str], List[str]]: The path to the PDF, the path to the images, and the published date.
        """
        pdf_paths: List[str] = []
        images_paths: List[str] = []
        published_dates: List[str] = []
        for paper in papers:
            title = paper.title.replace(" ", "_")
            month_year = datetime.strptime(paper.published, "%Y-%m-%d").strftime("%m-%Y")
            path_to_pdf = Path("data/pdfs") / f"{month_year}" / f"{title}.pdf"
            path_to_images = Path("site/images") / f"{month_year}" / f"{title}"
            if not path_to_pdf.exists():
                try:
                    download_pdf(paper.pdf_url, path_to_pdf)
                    extract_images(str(path_to_pdf), str(path_to_images))
                except Exception as exp:
                    logger.error(f"Error downloading {paper.pdf_url}: {exp}")
                    continue
            pdf_paths.append(str(path_to_pdf))
            images_paths.append(str(path_to_images))
            published_dates.append(paper.published)
        return pdf_paths, images_paths, published_dates

    def generate_reports(self, pdfs: List[str], images: List[str], published_dates: List[str]) -> None:
        """Generate the reports for the papers.

        Args:
            pdfs (List[str]): The paths to the PDFs.
            images (List[str]): The paths to the images.
            published_dates (List[str]): The published dates of the papers.
        """
        for pdf_path, images_path, published_date in zip(pdfs, images, published_dates):
            _, md_path = self.gemini_researcher(self.summary_prompt, pdf_local_path=pdf_path)
            if md_path is not None:
                add_images_to_md(md_path, images_path, published_date)

    def start_research(
        self,
        start_date: str,
        end_date: str,
        keywords: Optional[List[str]] = None,
        exclude_keywords: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
    ) -> List[Paper]:
        """Start the research.

        Args:
            start_date (str): Start date (YYYY-MM-DD) for filtering papers.
            end_date (str): End date (YYYY-MM-DD) for filtering papers.
            keywords (Optional[List[str]]): The keywords for arxiv search.
            exclude_keywords (Optional[List[str]]): The keywords to exclude from the search.
            categories (Optional[List[str]]): The categories for arxiv search.

        Returns:
            List[Paper]: List of relevant papers.
        """
        # Get the keywords, exclude keywords, and categories
        keywords, exclude_keywords, categories = self._get_keywords(keywords, exclude_keywords, categories)

        # Fetch the papers
        papers = self.arxiv_fetcher.fetch_papers(start_date, end_date, keywords, exclude_keywords, categories)

        # Download the PDFs
        pdf_paths, images_paths, published_dates = self.download_pdfs(papers)

        # Generate the reports
        self.generate_reports(pdf_paths, images_paths, published_dates)

        return papers


def add_and_commit_reports_to_git(reports_dir: str, start_date: str, end_date: str) -> None:
    """Add, commit, and push the reports to the git repository.

    Args:
        reports_dir (str): The directory to save the reports to.
        start_date (str): The start date of the research.
        end_date (str): The end date of the research.
    """
    try:  # noqa: WPS229
        subprocess.run(["git", "add", reports_dir], check=True)  # noqa: S607,S603
        subprocess.run(  # noqa: S607,S603
            ["git", "commit", "-m", f"Add reports {start_date} to {end_date}"],
            check=True,
        )
        subprocess.run(["git", "push", "origin", "main"], check=True)  # noqa: S607,S603
        logger.info("Reports added, committed, and pushed successfully.")
    except subprocess.CalledProcessError as exc:
        logger.error(f"Git command failed: {exc}")


@click.command()
@click.option("--start-date", required=True, help="Start date (YYYY-MM-DD) for filtering papers.")
@click.option("--end-date", required=True, help="End date (YYYY-MM-DD) for filtering papers.")
@click.option(
    "--gemini-model-name",
    default="gemini-2.5-pro",
    help="The name of the Gemini model to use.",
)
@click.option(
    "--site-reports-dir",
    default="site/_reports",
    help="The directory to save the reports to.",
)
@click.option("--keywords", multiple=True, help="Keywords for arxiv search. Can be specified multiple times.")
@click.option(
    "--exclude-keywords",
    multiple=True,
    help="Keywords to exclude from the search. Can be specified multiple times.",
)
@click.option(
    "--categories",
    multiple=True,
    help="Categories for arxiv search. Can be specified multiple times.",
)
def main(  # noqa: WPS216
    start_date: str,
    end_date: str,
    gemini_model_name: str = "gemini-2.5-pro",
    site_reports_dir: str = "site/_reports",
    keywords: Optional[list[str]] = None,
    exclude_keywords: Optional[list[str]] = None,
    categories: Optional[list[str]] = None,
):
    """
    CLI to run the Entrypoint research pipeline.

    Args:
        start_date (str): Start date (YYYY-MM-DD) for filtering papers.
        end_date (str): End date (YYYY-MM-DD) for filtering papers.
        gemini_model_name (str): The name of the Gemini model to use.
        site_reports_dir (str): The directory to save the reports to.
        keywords (Optional[list[str]]): The keywords for arxiv search.
        exclude_keywords (Optional[list[str]]): The keywords to exclude from the search.
        categories (Optional[list[str]]): The categories for arxiv search.
    """
    settings = Settings()  # type: ignore
    entrypoint = Entrypoint(gemini_model_name=settings.gemini_model_name, site_reports_dir=settings.site_reports_dir)
    notifier = Notifier(settings=settings)
    papers = entrypoint.start_research(
        start_date=start_date,
        end_date=end_date,
        keywords=list(keywords) if keywords else None,
        exclude_keywords=list(exclude_keywords) if exclude_keywords else None,
        categories=list(categories) if categories else None,
    )
    click.echo(f"Fetched {len(papers)} papers.")
    site_dir = str(Path(settings.site_reports_dir).parent)
    add_and_commit_reports_to_git(site_dir, start_date, end_date)
    for paper in papers:
        published = datetime.strptime(paper.published, "%Y-%m-%d").strftime("%m-%Y")
        title = paper.title.replace(" ", "_")
        report_url = settings.github_url_template.format(month_year=published, title=title)
        message = prepare_message(paper, report_url)
        notifier.send(message)


if __name__ == "__main__":
    main()
