# Hello LangGraph

A basic introduction to LangGraph framework - creating a simple conversational agent with human-in-the-loop functionality.

## Overview

This project demonstrates the fundamentals of LangGraph by building a poetry generation agent that collects human feedback and iteratively improves its output.

## Features

- **Simple Conversational Agent**: Basic chatbot using LangGraph StateGraph
- **Human-in-the-Loop**: Interactive feedback collection using `interrupt()` function
- **Memory Persistence**: SQLite checkpoint to save conversation state
- **Tool Integration**: Example of integrating custom tools with the agent

## Architecture

- **Framework**: LangGraph
- **State Management**: MessagesState
- **Memory**: SqliteSaver for checkpoints
- **LLM**: OpenAI GPT-4o-mini

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the agent
uv run python main.py
```

## Key Concepts Demonstrated

1. **StateGraph Creation**: Building a simple graph with START → LLM → END
2. **Tool Integration**: Using LangChain tools with the agent
3. **Interrupt Pattern**: Collecting human feedback during execution
4. **Checkpoints**: Saving and restoring conversation state

## Project Structure

```
hello-langgraph/
├── main.py           # Main agent implementation
├── pyproject.toml    # Dependencies
└── memory.db         # SQLite checkpoint (generated)
```

## Code Highlights

The agent uses `get_human_feedback` tool that interrupts the workflow to collect user input:

```python
@tool
def get_human_feedback(poem: str):
    """Get human feedback on a poem."""
    response = interrupt({"poem": poem})
    return response["feedback"]
```

## Next Steps

- Experiment with different tools
- Add conditional edges based on feedback
- Implement multi-turn conversations
- Explore more complex state structures

