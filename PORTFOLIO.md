# AI Agents Practice Projects — Portfolio

---

## Project Overview

**Project Name:** AI Agents Practice Projects  
**Period:** 2025  
**Team Size:** Solo (Personal Project)  
**Repository:** GitHub  

> A comprehensive hands-on repository featuring 18 independent AI Agent projects that explore diverse frameworks and architecture patterns. Built with LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, and AutoGen, covering multi-agent systems, workflow automation, voice-powered AI, content generation pipelines, and production-ready API deployment.

---

## Tech Stack

### Language & Runtime

| Category | Technology |
|----------|-----------|
| **Primary Language** | Python 3.13+ |
| **Package Manager** | uv (Modern Python Package Manager) |
| **Dependency Management** | pyproject.toml |

### AI Agent Frameworks

| Framework | Purpose | Projects |
|-----------|---------|:--------:|
| **LangGraph** | State-based workflows, graph orchestration | 7 |
| **CrewAI** | Role-based multi-agent systems | 3 |
| **Google ADK** | Sub-agents, parallel execution | 3 |
| **OpenAI Agents SDK** | Handoffs, guardrails, voice processing | 3 |
| **AutoGen** | Multi-agent research systems | 1 |

### Web Frameworks & UI

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Interactive web interface (ChatGPT Clone, Customer Support) |
| **FastAPI** | RESTful API server, SSE streaming |

### Database & Storage

| Technology | Purpose |
|-----------|---------|
| **SQLite** | Session management, checkpoints, conversation history |
| **OpenAI Vector Store** | Vector-based document retrieval |

### External APIs & Services

| Service | Purpose |
|---------|---------|
| **OpenAI API** | GPT models, Whisper (speech), DALL-E (image) |
| **Firecrawl API** | Web scraping and search |
| **Google Cloud Platform** | ADK project infrastructure |
| **yfinance** | Stock market data retrieval |
| **MCP Servers** | Model Context Protocol (Yahoo Finance, Time, Context7) |

### Deployment

| Technology | Purpose |
|-----------|---------|
| **Railway** | Cloud deployment (NIXPACKS builder) |
| **uvicorn** | ASGI production server |

### Testing

| Technology | Purpose |
|-----------|---------|
| **pytest** | Unit and integration testing |
| **LLM-based Evaluation** | Automated AI response quality assessment |

### Core Libraries

| Library | Purpose |
|---------|---------|
| **Pydantic** | Data validation and structured output |
| **LangChain** | LLM chains and tool integration |
| **python-dotenv** | Environment variable management |
| **sounddevice** | Audio I/O processing |
| **numpy** | Numerical operations |

---

## Architecture & Design Patterns

### Applied Patterns Overview

| Pattern | Description | Applied In |
|---------|-------------|-----------|
| **StateGraph** | State-based workflow management with conditional routing | All LangGraph projects |
| **Supervisor** | Central coordinator routes tasks to specialized agents | multi-agent-architectures |
| **Send (Parallel)** | Dynamic dispatch for parallel execution with result aggregation | workflow-architectures, youtube-thumbnail-maker |
| **Human-in-the-Loop** | User feedback via `interrupt()` for iterative refinement | hello-langgraph, youtube-thumbnail-maker |
| **Agent Chain** | Sequential agent execution with output passing | job-hunter-agent, content-pipeline-agent |
| **ParallelAgent** | Concurrent sub-agent execution | youtube-shorts-maker, financial-analyst |
| **Flow (CrewAI)** | `@start`, `@listen`, `@router` decorator-based flow control | content-pipeline-agent |
| **Handoff** | Context-preserving agent-to-agent transfers | customer-support-agent |
| **Guardrails** | Input/output filtering for safety and accuracy | customer-support-agent |
| **A2A Protocol** | JSON-RPC-based inter-agent communication | a2a |

### State Management Strategies

- **MessagesState** — Conversation history tracking
- **TypedDict** — Type-safe state structure definitions
- **Annotated List** — Automatic merging of parallel processing results
- **SQLite Checkpoint** — Workflow state persistence and restoration

---

## Detailed Project Descriptions

---

### 1. Hello LangGraph

> An introductory project for learning the fundamentals of LangGraph

**Framework:** LangGraph  
**Key Features:**
- Simple conversational agent implementation
- Poetry generation with Human-in-the-Loop feedback cycle
- SQLite-based conversation state persistence (memory checkpoints)

**Technical Highlights:**
- `interrupt()` function for user intervention patterns
- `SqliteSaver` for state save/restore
- Understanding StateGraph node-edge architecture

**Key Takeaways:**
- Node-edge-based graph structure in LangGraph
- Fundamentals of state-based workflow design
- Checkpoint-driven state persistence

---

### 2. Tutor Agent — Personalized Educational System

> A 4-agent system that delivers personalized education based on the learner's level

**Framework:** LangGraph  
**Key Features:**
- **Classification Agent**: Analyzes learner questions and determines proficiency level
- **Teacher Agent**: Provides step-by-step concept explanations
- **Feynman Agent**: Simplifies complex concepts using the Feynman technique
- **Quiz Agent**: Generates quizzes and delivers assessment feedback
- Web search tool integration for up-to-date information

**Architecture:**

```
User Question → Classification Agent → Level Assessment
                                          ├→ Teacher Agent (standard explanation)
                                          ├→ Feynman Agent (simplified explanation)
                                          └→ Quiz Agent (quiz & assessment)
```

**Technical Highlights:**
- Conditional routing (Conditional Edge) for automatic agent selection based on learner level
- Tool integration for web search capabilities
- Structured state management to maintain conversation context

---

### 3. Multi-Agent Architectures — Supervisor Pattern

> A multilingual customer support system using the Supervisor pattern

**Framework:** LangGraph  
**Key Features:**
- Central Supervisor detects user language and routes to the appropriate agent
- Dedicated agents for Korean, Spanish, and Greek
- AgentTool pattern — wrapping agents as reusable tools

**Architecture:**

```
User Input → Supervisor Agent
               ├→ Korean Agent (Korean response)
               ├→ Spanish Agent (Spanish response)
               └→ Greek Agent (Greek response)
```

**Technical Highlights:**
- Supervisor pattern: central coordinator distributes tasks to specialized agents
- AgentTool: wrapping agents as tools for flexible composition
- Language-specific agent isolation for improved domain quality

---

### 4. YouTube Thumbnail Maker — Video-to-Thumbnail Pipeline

> Automated thumbnail candidate generation from video with user-driven final selection

**Framework:** LangGraph  
**Key Features:**
- Full pipeline: Video → Audio extraction → Transcription → Summarization → Thumbnail generation
- Send pattern for parallel thumbnail candidate generation
- Human-in-the-Loop for final selection via user feedback

**Architecture:**

```
Video Input → ffmpeg (Audio) → Whisper (Transcription) → GPT (Summary)
                                                            ↓
                                                     [Send Pattern]
                                                ├→ DALL-E (Thumbnail 1)
                                                ├→ DALL-E (Thumbnail 2)
                                                └→ DALL-E (Thumbnail 3)
                                                            ↓
                                                User Selection (interrupt)
```

**Technical Highlights:**
- LangGraph Send pattern for dynamic parallel processing
- Integration of ffmpeg, Whisper, and DALL-E as external tools
- End-to-end multimedia processing pipeline design

---

### 5. Workflow Architectures — Parallel Document Summarization

> Optimized large document processing through chunk-based parallel summarization

**Framework:** LangGraph  
**Key Features:**
- Split large documents into chunks
- Summarize each chunk in parallel (Send pattern)
- Aggregate results into a final comprehensive summary

**Technical Highlights:**
- AI agent implementation of the Map-Reduce pattern
- Scalable parallel processing through dynamic worker creation
- Annotated List for automatic result merging

---

### 6. Email Refiner Agent — Automated Email Processing

> Automatic email classification, priority scoring, and response drafting system

**Framework:** LangGraph  
**Key Features:**
- Email classification: Spam / Normal / Urgent
- Priority scoring (1–10)
- Automated response draft generation
- Bonus: Travel Advisor agent (weather, exchange rates, attractions)

**Architecture:**

```
Email Input → Classification (Spam / Normal / Urgent)
               → Priority Scoring (1–10)
               → Response Drafting (auto-generated reply)
```

**Technical Highlights:**
- Pydantic models for structured output
- Sequential workflow design
- Session-based state persistence

---

### 7. Workflow Testing — Systematic Test Strategies

> Comprehensive testing patterns for LangGraph workflows

**Framework:** LangGraph + pytest  
**Key Features:**
- End-to-end graph testing
- Individual node unit testing
- LLM-based automated response quality evaluation
- Partial execution testing (resume from specific points)

**Test Code Example:**

```python
@pytest.mark.parametrize(
    "email, expected_category, min_score, max_score",
    [
        ("this is urgent!", "urgent", 8, 10),
        ("i wanna talk to you", "normal", 4, 7),
        ("i have an offer for you", "spam", 1, 3),
    ],
)
def test_full_graph(email, expected_category, min_score, max_score):
    result = graph.invoke({"email": email})
    assert result["category"] == expected_category
    assert min_score <= result["priority_score"] <= max_score
```

**Technical Highlights:**
- Test strategy design for AI systems
- Parametrized tests for multi-scenario validation
- Meta-evaluation: using LLMs to evaluate LLM output quality

---

### 8. Content Pipeline Agent — SEO & Virality Optimization

> Automated content generation and optimization system driven by quality scores

**Framework:** CrewAI Flow  
**Key Features:**
- Iterative loop: Research → Content Generation → Score Evaluation → Rewrite
- Auto-generates blog posts, tweets, and LinkedIn posts
- SEO score and virality score evaluation
- Automatic rewrite trigger when score < 7

**Architecture:**

```
Research → Content Generation → Score Evaluation
                                      ↓
                                score >= 7 → Done
                                score < 7  → Rewrite → Re-evaluate (loop)
```

**Technical Highlights:**
- CrewAI Flow decorators: `@start`, `@listen`, `@router`
- Quality-driven conditional loop design
- Composition of two independent Crews (SEO Crew + Virality Crew)

---

### 9. Job Hunter Agent — Automated Job Search & Interview Prep

> A 5-agent chain that automates resume-based job matching and interview preparation

**Framework:** CrewAI  
**Key Features:**
- **Search Agent**: Collects job postings
- **Matching Agent**: Matches resume against postings (1–5 score)
- **Selection Agent**: Selects the best-fit posting
- **Resume Optimizer Agent**: Tailors resume for the selected job
- **Company Research Agent**: Researches the company and prepares interview materials

**Architecture:**

```
Job Search → Resume Matching (1–5 score) → Job Selection
→ Resume Optimization → Company Research → Interview Prep
```

**Technical Highlights:**
- YAML configuration files for agent/task management (`agents.yaml`, `tasks.yaml`)
- Knowledge Source integration for resume data
- 5-stage sequential agent chain with structured data flow

---

### 10. News Reader Agent — Automated News Curation

> Automated news collection with multi-tier summarization and curation

**Framework:** CrewAI  
**Key Features:**
- 3-stage process: Collection → Summarization → Curation
- Web search and scraping for news gathering
- Multi-tier summaries: Tweet / Executive / Detailed
- Credibility and relevance score filtering

**Technical Highlights:**
- Firecrawl web scraping tool integration
- Multi-tier summarization strategy
- Score-based content filtering

---

### 11. A2A — Agent-to-Agent Communication Protocol

> Cross-framework agent communication via the A2A protocol

**Framework:** Google ADK + LangGraph + FastAPI  
**Key Features:**
- Communication between LangGraph agents and Google ADK agents
- Agent discovery via Agent Card JSON
- JSON-RPC protocol-based message exchange
- Remote agents used as sub-agents

**Architecture:**

```
User-Facing Agent
  ├→ Local LangGraph Agent
  └→ Remote ADK Agent (FastAPI Server)
       ├→ Agent Card (.well-known/agent-card.json)
       └→ JSON-RPC Message Handler
```

**Technical Highlights:**
- A2A (Agent-to-Agent) protocol standard implementation
- Cross-framework interoperability
- FastAPI-based agent server design

---

### 12. Financial Analyst — Stock Analysis System

> Parallel analysis of stock data, financials, and news to generate investment reports

**Framework:** Google ADK  
**Key Features:**
- Main agent orchestrates 3 sub-agents in parallel:
  - **Data Agent**: Stock data retrieval via yfinance
  - **Financial Agent**: Financial statement analysis
  - **News Agent**: Relevant news collection and analysis
- Automated comprehensive investment advisory report generation

**Architecture:**

```
Main Agent (Financial Advisor)
  ├→ Data Sub-Agent (yfinance)     ─┐
  ├→ Financial Sub-Agent            ├→ Consolidated Report
  └→ News Sub-Agent (Web Search)   ─┘
         [ParallelAgent — concurrent execution]
```

**Technical Highlights:**
- Google ADK ParallelAgent for concurrent sub-agent execution
- Real-time stock data API (yfinance) integration
- Structured investment report output

---

### 13. YouTube Shorts Maker — Fully Automated Video Generation

> End-to-end automation from topic input to final video assembly

**Framework:** Google ADK  
**Key Features:**
- Content planning: Automatic scene list generation
- Asset generation: Parallel image and voice creation
- Video assembly: Combines per-scene assets into the final video
- Input filtering callback to block inappropriate requests

**Architecture:**

```
Topic Input → Content Planner (Scene List)
               → [ParallelAgent]
                 ├→ Image Generator (per-scene images)
                 └→ Voice Generator (per-scene narration)
               → Video Assembler (final video)
```

**Technical Highlights:**
- Pydantic structured output (Scene list)
- Callback-based input filtering
- Parallel multimedia asset generation and assembly

---

### 14. ChatGPT Clone — Multi-Tool Conversational AI

> A feature-rich conversational AI assistant integrating multiple tools and MCP servers

**Framework:** OpenAI Agents SDK + Streamlit  
**Key Features:**
- **Web Search**: Real-time information retrieval
- **File Search**: Vector Store-based document search
- **Image Generation**: DALL-E-powered image creation
- **Code Execution**: Code interpreter
- **MCP Server Integration**: Yahoo Finance, Time, Context7
- Streaming response support
- File upload (text/images)

**Technical Highlights:**
- Model Context Protocol (MCP) server integration
- OpenAI Vector Store for file search
- Streamlit-based real-time streaming UI
- Dynamic multi-tool selection and execution

---

### 15. Customer Support Agent — Voice-Powered Support System

> Voice-based customer support with automatic classification, routing, and guardrails

**Framework:** OpenAI Agents SDK + Streamlit  
**Key Features:**
- **Triage Agent**: Classifies inquiries and routes to specialized agents
- **Account Agent**: Handles account-related inquiries
- **Billing Agent**: Handles payment/billing inquiries
- **Order Agent**: Handles order-related inquiries
- **Technical Agent**: Handles technical support inquiries
- VoicePipeline for voice input/output
- Input/Output Guardrails for safety assurance

**Architecture:**

```
Voice Input → VoicePipeline → Triage Agent
                                 ├→ Account Agent   ──┐
                                 ├→ Billing Agent    ──┤→ Handoff
                                 ├→ Order Agent      ──┤   (context preserved)
                                 └→ Technical Agent  ──┘
                                            ↓
                                 Output Guardrails → Voice Output
```

**Technical Highlights:**
- OpenAI VoicePipeline for voice-based interaction
- Handoff mechanism for context-preserving agent-to-agent transfers
- Input Guardrails: Off-topic request filtering
- Output Guardrails: Response accuracy and safety validation

---

### 16. Deployment — Production API Deployment

> Real-world example of deploying an AI agent as a RESTful API

**Framework:** FastAPI + OpenAI Agents SDK  
**Key Features:**
- Conversation creation and management API
- Synchronous and asynchronous message handling
- Server-Sent Events (SSE) streaming responses
- Railway cloud deployment configuration

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/conversations` | Create conversation |
| `POST` | `/conversations/{id}/message` | Send message (sync) |
| `POST` | `/conversations/{id}/message-stream` | Send message (streaming) |
| `POST` | `/conversations/{id}/message-stream-all` | Stream all events |

**Technical Highlights:**
- FastAPI async processing with SSE streaming
- OpenAI Conversations API integration
- Automated cloud deployment via Railway

---

### 17. Deep Research Clone — Multi-Agent Research Team

> A collaborative multi-agent team for deep research and report generation

**Framework:** AutoGen  
**Key Features:**
- SelectorGroupChat for team composition
- Research Planner → Research Agent → Termination condition check
- Web search integration for information gathering
- Automated report generation

**Technical Highlights:**
- AutoGen SelectorGroupChat pattern
- Role distribution and collaboration among agents
- Termination condition design for automatic completion

---

### 18. My First Agent — Getting Started Tutorial

> A beginner tutorial for building a basic agent using the OpenAI API directly

**Framework:** OpenAI API (direct usage)  
**Key Features:**
- Function Calling pattern walkthrough
- Weather lookup tool implementation example
- Understanding the fundamental agent architecture

**Technical Highlights:**
- OpenAI API Function Calling mechanism
- Tool definition and execution loop
- Foundational agent architecture concepts

---

## Project Structure

```
ai-agents-practice/
│
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore rules
│
├── [LangGraph-Based]
│   ├── hello-langgraph/               # LangGraph basics
│   ├── tutor-agent/                   # Educational tutor agent
│   ├── multi-agent-architectures/     # Supervisor pattern
│   ├── youtube-thumbnail-maker/       # YouTube thumbnail generator
│   ├── workflow-architectures/        # Parallel processing pattern
│   ├── email-refiner-agent/           # Email processing agent
│   └── workflow-testing/              # Workflow testing
│
├── [CrewAI-Based]
│   ├── content-pipeline-agent/        # Content generation pipeline
│   ├── job-hunter-agent/              # Job search automation
│   └── news-reader-agent/             # News reader & curation
│
├── [Google ADK-Based]
│   ├── a2a/                           # Agent-to-Agent communication
│   ├── financial-analyst/             # Financial analysis system
│   └── youtube-shorts-maker/          # YouTube Shorts generator
│
├── [OpenAI Agents SDK-Based]
│   ├── chatgpt-clone/                 # ChatGPT clone
│   ├── customer-support-agent/        # Customer support agent
│   └── deployment/                    # API deployment example
│
├── [AutoGen-Based]
│   └── deep-research-clone/           # Deep research team
│
└── [Other]
    └── my-first-agent/                # First agent (tutorial)
```

---

## Skills & Competencies Demonstrated

### AI Agent Design

- **Multi-Agent Architecture Design**: Hands-on experience implementing Supervisor, Chain, Parallel, and Handoff composition patterns
- **State-Based Workflow Engineering**: Graph-based modeling of complex business logic using StateGraph
- **Tool Integration Design**: Connecting external APIs, databases, and multimedia tools to agent systems

### Framework Proficiency

- **LangGraph**: State management, conditional routing, parallel processing, Human-in-the-Loop, checkpoints
- **CrewAI**: Role-based agents, task chains, Flow-based workflows, YAML configuration
- **Google ADK**: Sub-agents, ParallelAgent, structured output, callbacks
- **OpenAI Agents SDK**: Handoff, Guardrails, VoicePipeline, MCP integration, session management

### Software Engineering

- **Testing Strategy**: Unit/integration testing with pytest, LLM-based automated evaluation
- **API Design**: RESTful APIs, SSE streaming, conversation management
- **Deployment**: Railway cloud deployment, FastAPI + uvicorn production server
- **Data Modeling**: Type-safe data structures with Pydantic
- **Security**: Guardrail patterns, environment variable management, input/output filtering

### Problem-Solving Experience

| Domain | Problem Solved | Project |
|--------|---------------|---------|
| Education | Automated personalized tutoring based on learner level | Tutor Agent |
| Content | Auto-rewriting loop when quality falls below threshold | Content Pipeline |
| Career | Resume-based job matching and interview preparation | Job Hunter |
| Finance | Parallel stock data collection and investment report generation | Financial Analyst |
| Customer Support | Voice-based auto-classification and specialist agent routing | Customer Support |
| Media | Automated video-to-thumbnail and shorts generation pipeline | YouTube Thumbnail/Shorts |
| Communication | Cross-framework agent communication via A2A protocol | A2A |
| DevOps | Production API deployment of AI agent systems | Deployment |

---

## Future Plans

- Build production-grade agent systems with monitoring and observability
- Advanced RAG (Retrieval-Augmented Generation) implementations
- Deep-dive into agent memory systems (long-term / short-term memory)
- Establish agent evaluation and benchmarking frameworks
- Apply agent patterns to real-world business domain projects

---

## Contact

- **GitHub**: [Your GitHub Profile]
- **Email**: [Your Email Address]
- **LinkedIn**: [Your LinkedIn Profile]

---

> This document is formatted in Markdown for PDF conversion.  
> Recommended conversion tools: [Pandoc](https://pandoc.org/), [md-to-pdf](https://www.npmjs.com/package/md-to-pdf), [Typora](https://typora.io/), VS Code Markdown PDF extension
