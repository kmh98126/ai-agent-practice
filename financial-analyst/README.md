# Financial Analyst

Comprehensive stock analysis system that gathers data, performs financial analysis, researches news, and generates investment advice reports using Google ADK.

## Overview

This project implements a financial advisor agent that coordinates multiple specialized sub-agents to provide comprehensive stock analysis and investment recommendations.

## Features

- **Multi-Agent Analysis**: Coordinates 3 specialized sub-agents
- **Data Collection**: Gathers company info, stock prices, financial metrics
- **Financial Analysis**: Deep dive into income statements, balance sheets, cash flow
- **News Analysis**: Latest company news and market sentiment
- **Investment Reports**: Generates comprehensive investment advice documents

## Architecture

- **Framework**: Google ADK
- **Pattern**: Main agent with sub-agents as tools
- **Data Source**: yfinance for stock market data
- **Tools**: Custom functions for financial data retrieval

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the financial advisor
uv run python -m financial_advisor.agent

# The agent will analyze stocks and generate reports
```

## Agent Structure

### Main Agent: Financial Advisor
- Coordinates all sub-agents
- Synthesizes analysis from multiple sources
- Generates final investment advice
- Saves comprehensive reports as artifacts

### Sub-Agents

#### 1. Data Analyst
- **Tools**: 
  - `get_company_info()`: Company name, industry, sector
  - `get_stock_price()`: Current price and historical data
  - `get_financial_metrics()`: P/E ratio, market cap, dividend yield, beta
- **Output**: Basic stock data and metrics

#### 2. Financial Analyst
- **Tools**:
  - `get_income_statement()`: Revenue, profit, margins
  - `get_balance_sheet()`: Assets, liabilities, equity
  - `get_cash_flow()`: Operating, investing, financing cash flows
- **Output**: Detailed financial statement analysis

#### 3. News Analyst
- **Tools**:
  - `web_search_tool()`: Latest company news and market updates
- **Output**: News analysis and market sentiment

## Project Structure

```
financial-analyst/
├── financial_advisor/
│   ├── agent.py              # Main advisor agent
│   ├── prompt.py             # Agent prompts
│   └── sub_agents/
│       ├── data_analyst.py   # Stock data collection
│       ├── financial_analyst.py  # Financial statement analysis
│       └── news_analyst.py   # News and sentiment analysis
├── tools.py                  # Web search tool
└── pyproject.toml            # Dependencies
```

## Data Sources

### yfinance Integration
- Real-time and historical stock data
- Financial statements (income, balance sheet, cash flow)
- Company information and metrics
- Market data and indicators

### Web Search
- Latest company news
- Market analysis articles
- Industry trends
- Regulatory updates

## Output Format

### Investment Advice Report
```markdown
# Executive Summary and Advice:
{Investment recommendation and summary}

## Data Analyst Report:
{Stock data and basic metrics}

## Financial Analyst Report:
{Financial statement analysis}

## News Analyst Report:
{News analysis and sentiment}
```

## Key Features

### Parallel Sub-Agent Execution
- All three sub-agents can work simultaneously
- Results stored in shared state
- Efficient data gathering

### Structured Financial Analysis
- Income statement analysis (revenue, margins, profitability)
- Balance sheet analysis (assets, debt, equity ratios)
- Cash flow analysis (operating, free cash flow, capital allocation)

### Comprehensive Reporting
- Combines all analyses into single report
- Saves as markdown artifact
- Easy to share and review

## Use Cases

- Stock research and analysis
- Investment decision support
- Portfolio management
- Financial education
- Market research automation

## Customization

- Add more financial metrics
- Integrate additional data sources
- Customize analysis depth
- Add technical analysis
- Implement portfolio tracking
- Add risk assessment

## Tips

- Provide accurate stock tickers
- Review generated reports for accuracy
- Combine with human judgment
- Use for research starting points
- Keep data sources updated

## Example Usage

```python
# Ask the agent about a stock
"I'm considering investing in AAPL. Should I buy?"

# Agent will:
# 1. Gather company data
# 2. Analyze financial statements
# 3. Research latest news
# 4. Generate investment advice report
```

## Dependencies

- google-cloud-aiplatform[adk]
- yfinance (stock data)
- firecrawl (web search)
- litellm (LLM integration)

