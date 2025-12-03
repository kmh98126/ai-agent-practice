# Multi-Agent Architectures

Demonstrates the supervisor pattern using LangGraph, where a central supervisor agent routes requests to specialized language-specific agents.

## Overview

This project implements a multilingual customer support system with a supervisor that intelligently routes customer inquiries to appropriate language-specific agents (Korean, Spanish, Greek).

## Features

- **Supervisor Pattern**: Central agent coordinates multiple specialized agents
- **Language Detection**: Automatically routes based on detected language
- **AgentTool Pattern**: Converts agents into tools for the supervisor
- **Dynamic Agent Creation**: Each language agent is created as a reusable tool

## Architecture

- **Framework**: LangGraph
- **Pattern**: Supervisor with AgentTool integration
- **State Management**: AgentsState with current_agent tracking
- **LLM**: OpenAI GPT-4o

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the multi-agent system
uv run python main.py
```

## Architecture Details

### Supervisor Agent
- Main entry point that receives all customer inquiries
- Analyzes the language and content of the request
- Routes to appropriate language-specific agent using AgentTool
- Maintains conversation context across agent transfers

### Language-Specific Agents
- **Korean Agent**: Handles Korean customer support
- **Spanish Agent**: Handles Spanish customer support
- **Greek Agent**: Handles Greek customer support

### AgentTool Pattern
Each language agent is converted into a tool using `make_agent_tool()`:
- Agent functionality wrapped as a callable tool
- State injection using `InjectedState`
- Results integrated back into supervisor's conversation

## Project Structure

```
multi-agent-architectures/
├── graph.py              # Supervisor graph implementation
├── langgraph.json        # LangGraph configuration
└── main.ipynb            # Example usage notebook
```

## Key Concepts

1. **Supervisor Pattern**: Central coordinator managing specialized workers
2. **AgentTool**: Converting agents into tools for flexible composition
3. **InjectedState**: Passing full state context to agent tools
4. **Conditional Routing**: Dynamic routing based on LLM decisions

## Code Highlights

```python
def make_agent_tool(tool_name, tool_description, system_prompt, tools):
    # Creates a standalone agent graph
    agent = agent_builder.compile()
    
    @tool(name_or_callable=tool_name)
    def agent_tool(state: Annotated[dict, InjectedState]):
        result = agent.invoke(state)
        return result["messages"][-1].content
    
    return agent_tool
```

## Use Cases

- Customer support with language specialization
- Domain-specific routing (technical, billing, sales)
- Skill-based agent selection
- Hierarchical agent organizations

## Extending the System

- Add more language agents
- Implement agent-to-agent communication
- Add fallback mechanisms
- Implement agent performance monitoring
- Add conversation handoff between agents

