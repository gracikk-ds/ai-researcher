# Arxiv Research Agent

A service to automatically load research papers from arXiv by topic and date, analyze them using AI agents (Gemini), select the most relevant ones, generate concise summaries and published them in Notion DB.

## Features

- **Search arXiv**: Retrieve papers by date range, categories, and keywords.
- **Relevance Selection**: Use Gemini model to select the most relevant papers.
- **Download PDFs**: Download PDFs and extract images from them.
- **Summarization**: Use Gemini model to generate summaries of selected papers.
- **Report Generation**: Generate markdown reports with images for each paper.
- **Publish Reports**:  Publish reports to Notion DB.

## Installation

1. Clone the repository:

```bash
git clone git@github.com:gracikk-ds/ai-researcher.git
cd ResearchAgent
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

You can run the service to fetch and analyze papers by specifying a topic and date range.

```bash
python src/entrypoint.py --start-date 2025-06-01 (included) --end-date 2025-06-30 (excluded)
```
