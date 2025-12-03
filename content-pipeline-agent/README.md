# Content Pipeline Agent

Automated content generation pipeline that creates blog posts, tweets, and LinkedIn posts with SEO and virality optimization using CrewAI Flow.

## Overview

This project demonstrates a sophisticated content creation workflow that conducts research, generates content, evaluates quality through scoring, and iteratively improves content until it meets quality thresholds.

## Features

- **Multi-Format Content**: Generates blog posts, tweets, and LinkedIn posts
- **Research Phase**: Web search to gather relevant information
- **Quality Scoring**: SEO score for blogs, virality score for social media
- **Iterative Improvement**: Automatically rewrites content if score < 7
- **Structured Output**: Uses Pydantic models for consistent formatting

## Architecture

- **Framework**: CrewAI Flow
- **Pattern**: Flow-based workflow with routing and looping
- **Evaluation**: Specialized crews (SeoCrew, ViralityCrew) for scoring
- **LLM**: OpenAI o4-mini with structured output

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
# Run the content pipeline
uv run python main.py

# Or customize in code:
flow.kickoff(
    inputs={
        "content_type": "blog",  # or "tweet", "linkedin"
        "topic": "Your Topic Here",
    }
)
```

## Workflow Stages

### 1. Initialization
- Validates content type (blog/tweet/linkedin)
- Sets maximum length based on content type
- Validates topic input

### 2. Research
- Uses Head Researcher agent to gather information
- Web search for relevant facts and insights
- Collects comprehensive research data

### 3. Content Generation
- Routes to appropriate content generator based on type
- Blog: SEO-optimized blog post with title, subtitle, sections
- Tweet: Viral-worthy tweet with hashtags
- LinkedIn: Professional post with hook, content, CTA

### 4. Quality Evaluation
- **For Blogs**: SeoCrew evaluates SEO effectiveness (0-10)
- **For Social**: ViralityCrew evaluates viral potential (0-10)
- Detailed feedback provided on strengths/weaknesses

### 5. Iterative Improvement
- If score ≥ 7: Content finalized
- If score < 7: Content regenerated with improvement guidance
- Process repeats until quality threshold met

## Project Structure

```
content-pipeline-agent/
├── main.py              # Main flow implementation
├── seo_crew.py          # SEO evaluation crew
├── virality_crew.py     # Virality evaluation crew
├── tools.py             # Web search tool
└── crewai_flow.html     # Flow visualization (generated)
```

## Key Concepts

### CrewAI Flow Decorators
- `@start()`: Entry point
- `@listen()`: Reacts to state changes
- `@router()`: Conditional routing
- `@or_()`: Multiple trigger conditions

### Quality Scoring
- **SEO Score**: Keyword optimization, structure, readability
- **Virality Score**: Hook strength, emotional resonance, shareability

### State Management
- ContentPipelineState tracks entire workflow
- Includes inputs, research, scores, and generated content
- Pydantic models ensure type safety

## Example Output

### Blog Post Structure
```json
{
  "title": "SEO-optimized title",
  "subtitle": "Engaging subtitle",
  "sections": ["Section 1", "Section 2", ...]
}
```

### Tweet Structure
```json
{
  "content": "Tweet text",
  "hashtags": "#hashtag1 #hashtag2"
}
```

### LinkedIn Post Structure
```json
{
  "hook": "Attention-grabbing opening",
  "content": "Main content",
  "call_to_action": "Engagement CTA"
}
```

## Customization

- Adjust quality thresholds (currently 7/10)
- Modify scoring criteria
- Add more content types
- Customize research depth
- Add brand voice guidelines
- Implement A/B testing

## Flow Visualization

Generate flow diagram:
```python
flow.plot()  # Creates crewai_flow.html
```

## Use Cases

- Social media content creation
- Blog post generation
- Content marketing automation
- SEO content optimization
- Viral content strategy

## Tips

- Provide specific topics for better results
- Review generated content for brand alignment
- Use high-quality research sources
- Iterate on content based on performance data
- A/B test different content versions

