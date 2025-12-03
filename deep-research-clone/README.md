# Deep Research Clone

Advanced multi-agent research system using AutoGen that breaks down complex questions, conducts focused research, and generates comprehensive reports.

## Overview

This project demonstrates a sophisticated research workflow where multiple specialized agents collaborate to answer complex questions through web research, analysis, and synthesis.

## Features

- **Research Planning**: Breaks complex questions into focused research subtasks
- **Web Research**: Searches and extracts information from web sources
- **Team Collaboration**: Multiple agents working together
- **Termination Conditions**: Smart stopping criteria
- **Report Generation**: Comprehensive markdown reports

## Architecture

- **Framework**: AutoGen (Microsoft)
- **Pattern**: SelectorGroupChat for team composition
- **Agents**: Research Planner, Research Agent
- **Tools**: Web search and scraping

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
# Run in Jupyter notebook
uv run jupyter notebook deep-research-team.ipynb
```

## Agent Team

### Research Planner Agent
- **Role**: Strategic research coordinator
- **Function**: Breaks down complex questions
- **Output**: Focused research plan with:
  - 2-3 core topics to investigate
  - 3-5 specific search queries
  - Coverage areas: latest news, statistics, expert analysis, future outlook

### Research Agent
- **Role**: Web research specialist
- **Tools**: Web search tool (Firecrawl)
- **Function**: 
  - Executes search queries from plan
  - Extracts key information
  - Synthesizes findings
- **Process**:
  1. Executes 3-5 searches
  2. Extracts main facts and statistics
  3. Identifies recent developments
  4. Compiles research results

## Project Structure

```
deep-research-clone/
├── deep-research-team.ipynb   # Main research workflow
├── email-optimizer-team.ipynb # Email optimization example
├── tools.py                    # Web search tool
├── report.md                   # Generated reports
└── pyproject.toml              # Dependencies
```

## Key Concepts

### SelectorGroupChat
- AutoGen's team chat pattern
- Agents collaborate in structured conversations
- Automatic role assignment and coordination

### Termination Conditions
- **MaxMessageTermination**: Stops after max messages
- **TextMentionTermination**: Stops when specific text appears
- Prevents infinite loops
- Ensures completion

### Research Strategy
1. **Plan First**: Create focused research plan
2. **Execute Searches**: Run multiple targeted searches
3. **Extract Information**: Pull key facts and insights
4. **Synthesize**: Combine findings into coherent report

## Workflow

1. **Question Input**: Complex research question
2. **Planning**: Research Planner creates focused plan
3. **Research**: Research Agent executes searches
4. **Synthesis**: Agents collaborate to synthesize findings
5. **Report**: Generate comprehensive markdown report

## Example Research Plans

### Core Topics
- Latest developments
- Key statistics
- Expert opinions
- Future implications

### Search Queries
- Recent news articles
- Data and statistics
- Expert analysis
- Academic studies
- Industry reports

## Use Cases

- Market research
- Academic research
- Competitive analysis
- Industry intelligence
- Due diligence
- Technical research

## Customization

- Adjust research depth
- Add more agent types
- Customize termination conditions
- Modify search strategies
- Add citation tracking
- Implement source verification

## Tips

- Ask specific, focused questions
- Review generated research plans
- Verify source credibility
- Combine with human review
- Use for research starting points

## Output

- Structured research plan
- Web search results
- Extracted information
- Comprehensive report (report.md)

## Dependencies

- autogen-agentchat
- autogen-ext
- firecrawl (for web search)

