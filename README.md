# Arxiv Research Agent

A service to automatically load research papers from arXiv by topic and date, analyze them using AI agents (CrewAI), select the most relevant ones, and generate concise summaries.

## Features
- **Search arXiv**: Retrieve papers by topic and date.
- **AI Analysis**: Use CrewAI agents to analyze paper content.
- **Relevance Selection**: Automatically select the most useful papers.
- **Summarization**: Generate summaries of selected papers.

## Installation

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd ResearchAgent
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the service to fetch and analyze papers by specifying a topic and date range.

```bash
python src/main.py --topic "machine learning" --start-date 2024-01-01 --end-date 2024-01-31
```

- `--topic`: Topic or keywords to search for.
- `--start-date`, `--end-date`: Date range for papers (YYYY-MM-DD).

## Configuration

- Environment variables (if any) can be set in a `.env` file.
- API keys or additional settings for CrewAI can be configured as needed.

## Example Workflow
1. The service queries arXiv for papers matching your topic and date.
2. CrewAI agents analyze the papers' abstracts and content.
3. The most relevant papers are selected by the agents.
4. Summaries are generated and presented to the user.
