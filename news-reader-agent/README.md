# News Reader Agent

Intelligent news aggregation and summarization system that collects, summarizes, and curates news articles into professional daily briefings using CrewAI.

## Overview

This project automates the news reading process by discovering relevant articles, creating multi-tier summaries, and assembling them into publication-ready daily briefings.

## Features

- **News Discovery**: Finds credible news articles from diverse sources
- **Intelligent Filtering**: Removes low-quality content and duplicates
- **Multi-Tier Summaries**: Creates tweet-length, executive, and comprehensive summaries
- **Professional Curation**: Assembles stories into publication-ready format
- **Source Credibility**: Scores articles for credibility and relevance

## Architecture

- **Framework**: CrewAI
- **Agents**: 3 specialized agents (Hunter, Summarizer, Curator)
- **Tools**: Web search and scraping tools
- **Output**: Markdown documents for publication

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
cat > .env << EOF
OPENAI_API_KEY=your_key_here
FIRECRAWL_API_KEY=your_key_here
EOF
```

## Usage

```bash
# Run the news reader
uv run python main.py

# Or customize topic:
result = NewsReaderAgent().crew().kickoff(
    inputs={"topic": "Cambodia Thailand War."}
)
```

## Agent Workflow

### 1. News Hunter Agent
- **Role**: Senior News Intelligence Specialist
- **Task**: Discover and collect credible news articles
- **Tools**: Search tool, scrape tool
- **Process**:
  - Searches for recent articles on topic
  - Filters out topic hubs and tag pages
  - Scrapes full article content
  - Filters by length (>200 words) and freshness (<48 hours)
  - Scores credibility (1-10) and relevance (1-10)
- **Output**: Structured markdown with all collected articles

### 2. Summarizer Agent
- **Role**: Expert News Analyst and Content Synthesizer
- **Task**: Create multi-tier summaries for each article
- **Tools**: Scrape tool (for full content)
- **Output Types**:
  - **Tweet Summary** (≤280 chars): Social media format
  - **Executive Summary** (150-200 words): Professional briefing
  - **Comprehensive Summary** (500-700 words): Full context
- **Output**: Markdown with all three summary types per article

### 3. Curator Agent
- **Role**: Senior News Editor and Editorial Curator
- **Task**: Assemble final publication-ready briefing
- **Process**:
  - Applies editorial judgment
  - Creates compelling headlines
  - Groups related stories
  - Adds editorial transitions
  - Provides analysis and context
- **Output**: Final professional daily briefing

## Project Structure

```
news-reader-agent/
├── main.py                    # Main crew orchestration
├── tools.py                   # Search and scrape tools
├── config/
│   ├── agents.yaml           # Agent configurations
│   └── tasks.yaml            # Task definitions
└── output/
    ├── content_harvest.md    # Collected articles
    ├── summary.md            # Multi-tier summaries
    └── final_report.md       # Publication-ready briefing
```

## Output Format

### Content Harvest (Stage 1)
```markdown
# News Articles Collection: {topic}

## Article 1: [Headline]
- Source, Date, URL
- Category, Credibility Score, Relevance Score
- Full article content
```

### Summary (Stage 2)
```markdown
# News Summaries: {topic}

## Article 1: [Headline]
### 📱 Headline Summary (Tweet-length)
### 📋 Executive Summary
### 📖 Comprehensive Summary
```

### Final Report (Stage 3)
```markdown
# Daily News Briefing: {topic}

## Executive Summary
## 🚨 Today's Lead Story
## 📈 Breaking News & Developments
## 💼 Technology & Innovation
## 🎯 Editor's Analysis
## 📚 Additional Reading
```

## Key Features

### Intelligent Filtering
- Filters out topic hubs (e.g., `/topic/`, `/tag/`)
- Removes articles shorter than 200 words
- Filters articles older than 48 hours
- Removes duplicates
- Scores credibility based on source reputation

### Multi-Tier Summaries
- **Tweet Summary**: For quick scanning and social sharing
- **Executive Summary**: For busy professionals
- **Comprehensive Summary**: For detailed understanding

### Professional Curation
- Editorial judgment on story importance
- Thematic grouping of related stories
- Context and background information
- Future outlook and trends

## Customization

- Adjust filtering criteria
- Modify summary lengths
- Add more output formats
- Customize editorial style
- Add topic categories
- Implement scheduled runs

## Use Cases

- Daily news briefings
- Market intelligence reports
- Industry trend analysis
- Competitive intelligence
- Research automation

## Tips

- Provide specific topics for better results
- Review generated content for accuracy
- Customize editorial voice
- Adjust summary tiers based on audience
- Use for research starting points

## Output Files

All outputs saved in `output/`:
- `content_harvest.md`: Raw collected articles
- `summary.md`: Multi-tier summaries
- `final_report.md`: Final publication-ready briefing

