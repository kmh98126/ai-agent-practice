# Tutor Agent

An intelligent educational tutor system that adapts to each learner's style and provides personalized learning experiences through multiple specialized agents.

## Overview

This project implements a multi-agent tutoring system that classifies learners and routes them to specialized teaching agents: Teacher Agent (structured learning), Feynman Agent (concept validation), and Quiz Agent (active recall).

## Features

- **Learner Classification**: Automatically assesses learning style and knowledge level
- **Multi-Agent System**: Four specialized agents working together
  - Classification Agent: Routes learners to appropriate learning path
  - Teacher Agent: Step-by-step structured teaching with confirmation
  - Feynman Agent: Validates understanding through simple explanations
  - Quiz Agent: Generates and administers quizzes
- **Web Search Integration**: Fetches up-to-date information for teaching
- **Adaptive Learning**: Adjusts teaching approach based on learner responses

## Architecture

- **Framework**: LangGraph
- **Agents**: ReAct agents using `create_react_agent`
- **State Management**: MessagesState with current_agent tracking
- **Tools**: Web search, agent transfer, quiz generation

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the tutor agent
uv run python main.py
```

## Agent Details

### Classification Agent
- Assesses learner's topic, current knowledge, and learning preferences
- Routes to: quiz_agent, teacher_agent, or feynman_agent
- Uses strategic questions to identify optimal learning approach

### Teacher Agent
- **Teaching Process**: Research → Break Down → Explain → Confirm → Progress
- Validates understanding after each concept
- Provides re-explanations using different approaches if needed
- One concept at a time for optimal learning

### Feynman Agent
- Uses Feynman Technique: "If you can't explain it simply, you don't understand it"
- Challenges learners to explain concepts as if teaching a child
- Identifies gaps through clarification questions
- Cycles until true understanding is achieved

### Quiz Agent
- Generates structured quizzes with multiple-choice questions
- Three difficulty levels: easy, medium, hard
- Provides detailed feedback for each answer
- Tracks scores and provides performance summaries

## Project Structure

```
tutor-agent/
├── main.py                    # Graph orchestration
├── agents/
│   ├── classification_agent.py
│   ├── teacher_agent.py
│   ├── feynman_agent.py
│   └── quiz_agent.py
├── tools/
│   ├── shared_tools.py       # Agent transfer, web search
│   └── quiz_tools.py         # Quiz generation
└── langgraph.json            # LangGraph configuration
```

## Key Features

1. **Routing Logic**: Conditional edges based on agent selection
2. **Tool-Based Transfer**: Agents can transfer control using `transfer_to_agent` tool
3. **Web Search**: Teacher and Quiz agents fetch current information
4. **Structured Output**: Quiz generation with structured question format

## Example Flow

1. Learner asks: "I want to learn about quantum physics"
2. Classification Agent assesses their level and preferences
3. Routes to Teacher Agent for structured learning
4. Teacher researches, breaks down concepts, explains step-by-step
5. After learning, learner can transfer to Quiz Agent for practice
6. Quiz Agent generates quiz and provides detailed feedback

## Customization

- Modify agent prompts in respective agent files
- Adjust quiz difficulty and length preferences
- Add new specialized agents for different learning styles
- Integrate additional tools (calculator, code executor, etc.)

