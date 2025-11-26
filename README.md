# AI Agents Practice Projects

A collection of practice projects for learning AI Agent development. Explore various frameworks and architecture patterns to master building AI agents.

## 📚 Overview

This repository contains 18 independent AI Agent projects, each demonstrating different frameworks and use cases.

## 🎯 Learning Objectives

- Master various AI Agent frameworks (LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, etc.)
- Design multi-agent architectures
- Implement workflow and state management patterns
- Integrate and utilize tools effectively
- Implement human-in-the-loop patterns
- Apply guardrail and security patterns

## 📁 Projects

### LangGraph-Based Projects

#### 1. hello-langgraph
**Basic Tutorial** - Introduction to LangGraph
- Simple conversational agent
- Poetry generation with human feedback (human-in-the-loop)
- SQLite memory for conversation state persistence

#### 2. tutor-agent
**Educational Tutor Agent** - Personalized learning support
- 4 specialized agents: classification, teacher, feynman, quiz
- Automatic routing based on learner's level
- Web search for up-to-date information
- Quiz generation and assessment

#### 3. multi-agent-architectures
**Supervisor Pattern** - Multi-language customer support
- Central supervisor routes to language-specific agents
- Korean/Spanish/Greek dedicated agents
- AgentTool pattern for using agents as tools

#### 4. youtube-thumbnail-maker
**YouTube Thumbnail Generator** - Video-based workflow
- Video → audio extraction → transcription → summarization
- Parallel thumbnail candidate generation (Send pattern)
- User feedback-based final selection
- Integration with ffmpeg, Whisper, DALL-E

#### 5. workflow-architectures
**Parallel Processing Pattern** - Document summarization optimization
- Split documents into chunks for parallel summarization
- LangGraph Send pattern implementation
- Aggregation step to combine all summaries

#### 6. email-refiner-agent
**Email Processing Workflow** - Automatic classification and response
- Sequential workflow: classification → priority → response drafting
- Structured output (Pydantic models)
- Travel advisor agent included (weather, exchange rates, attractions)

#### 7. workflow-testing
**Workflow Testing** - LangGraph testing examples
- End-to-end graph testing
- Individual node unit testing
- LLM-based response evaluation
- Partial execution testing

### CrewAI-Based Projects

#### 8. content-pipeline-agent
**Content Generation Pipeline** - SEO/virality optimization
- CrewAI Flow for workflow management
- Automatic blog/tweet/LinkedIn post generation
- Research → generation → score evaluation → rewriting loop
- Score-based quality assurance (rewrite if score < 7)

#### 9. job-hunter-agent
**Job Hunter Agent** - Job search support system
- 5-agent chain: search → matching → selection → resume optimization → company research → interview prep
- Resume-based matching and optimization
- YAML config files for agent/task management
- Knowledge Source for resume information

#### 10. news-reader-agent
**News Reader** - News collection and summarization
- 3-stage process: collection → summarization → curation
- Web search/scraping for news collection
- Multi-tier summaries (tweet/executive/detailed)
- Credibility and relevance score filtering

### Google ADK-Based Projects

#### 11. a2a
**Agent-to-Agent Communication** - Inter-agent interaction
- LangGraph agent and A2A server implementation
- Remote agents as sub-agents
- FastAPI for Agent Card JSON exposure
- JSON-RPC protocol implementation

#### 12. financial-analyst
**Financial Analyst** - Stock analysis system
- Main agent utilizes 3 sub-agents
- Parallel execution of data/financial/news analysis
- Stock data retrieval via yfinance
- Automatic investment advice report generation

#### 13. youtube-shorts-maker
**YouTube Shorts Maker** - Fully automated video generation
- Content planning → asset generation (image/voice) → video assembly
- ParallelAgent for parallel image/voice generation
- Structured output (Scene list)
- Callback for input filtering

### OpenAI Agents SDK-Based Projects

#### 14. chatgpt-clone
**ChatGPT Clone** - Conversational AI assistant
- Streamlit web interface
- Multiple tools: web search, file search, image generation, code execution
- MCP server integration (Yahoo Finance, Time, etc.)
- Vector store for file search
- Streaming response support

#### 15. customer-support-agent
**Customer Support Agent** - Voice-based support system
- Triage agent for inquiry classification and routing
- 4 specialized agents: account/billing/order/technical support
- VoicePipeline for voice input/output
- Input/Output Guardrails for safety
- Handoff mechanism implementation

#### 16. deployment
**API Deployment Example** - Deploy agent via FastAPI
- RESTful API endpoints
- Conversation creation and message handling
- Streaming responses (Server-Sent Events)
- OpenAI Conversations API integration

### AutoGen-Based Projects

#### 17. deep-research-clone
**Deep Research Team** - Multi-agent research system
- SelectorGroupChat for team composition
- Research planner → research agent → termination conditions
- Web search for information gathering
- Automatic report generation

### Other Projects

#### 18. my-first-agent
**My First Agent** - Basic tutorial
- Direct OpenAI API usage
- Function calling pattern learning
- Weather lookup tool example

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (package manager)
- Required API keys:
  - `OPENAI_API_KEY`: OpenAI API key (required for most projects)
  - `FIRECRAWL_API_KEY`: Firecrawl API key (for some projects)
  - `GOOGLE_CLOUD_PROJECT_ID`: Google Cloud project ID (for ADK projects)
  - `VECTOR_STORE_ID`: OpenAI Vector Store ID (for chatgpt-clone)

### Installation & Execution

Each project runs independently:

```bash
# Navigate to a specific project
cd chatgpt-clone

# Install dependencies
uv sync

# Set up environment variables (create .env file in project directory)
# Add required API keys to .env file

# Run the project
uv run streamlit run main.py  # For Streamlit apps
# or
uv run python main.py
```

## 📝 Environment Variables

Each project manages environment variables through a `.env` file.

**Note**: Add your actual API keys to the `.env` file, but this file will not be committed to Git (included in `.gitignore`).

Required environment variables:
- `OPENAI_API_KEY`: Required for most projects
- `FIRECRAWL_API_KEY`: For projects requiring web search
- `GOOGLE_CLOUD_PROJECT_ID`, `GOOGLE_CLOUD_LOCATION`, `GOOGLE_CLOUD_BUCKET`: For Google ADK projects
- `VECTOR_STORE_ID`: For chatgpt-clone project

## 🏗️ Framework Features

### LangGraph
- State-based workflow management
- Conditional routing and parallel processing
- Human-in-the-loop patterns
- Checkpoints for state persistence/restoration

### CrewAI
- Role-based agent design
- Task chains and dependency management
- Knowledge Source utilization
- YAML configuration file support

### Google ADK
- Sub-agents as tools
- Structured output (Pydantic)
- Parallel execution (ParallelAgent)
- Artifact storage functionality

### OpenAI Agents SDK
- Handoff mechanism
- Guardrails (input/output filtering)
- VoicePipeline (voice processing)
- Session management (SQLite)

## 📂 Project Structure

```
ai-agents-practice/
├── a2a/                          # Agent-to-Agent communication
├── chatgpt-clone/                # ChatGPT clone
├── content-pipeline-agent/       # Content generation pipeline
├── customer-support-agent/       # Customer support agent
├── deep-research-clone/          # Deep research team
├── deployment/                   # API deployment example
├── email-refiner-agent/          # Email processing agent
├── financial-analyst/            # Financial analyst
├── hello-langgraph/              # LangGraph basics
├── job-hunter-agent/             # Job hunter agent
├── multi-agent-architectures/    # Multi-agent architectures
├── my-first-agent/               # My first agent
├── news-reader-agent/            # News reader
├── tutor-agent/                  # Tutor agent
├── workflow-architectures/       # Workflow architectures
├── workflow-testing/             # Workflow testing
├── youtube-shorts-maker/         # YouTube Shorts maker
└── youtube-thumbnail-maker/      # YouTube thumbnail maker
```

## ⚠️ Important Notes

- This repository is for **educational purposes only**
- Never commit actual API keys to Git (`.env` is included in `.gitignore`)
- Each project runs independently and has no dependencies on others
- Some projects require paid API keys

## 📚 References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Google ADK Documentation](https://cloud.google.com/vertex-ai/docs/agent-development-kit)
- [OpenAI Agents SDK](https://github.com/openai/agents)
