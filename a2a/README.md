# A2A (Agent-to-Agent)

Demonstrates Agent-to-Agent communication protocols, allowing agents to communicate and work together using standardized interfaces.

## Overview

This project shows how to implement A2A (Agent-to-Agent) communication, enabling agents to discover, communicate with, and utilize other agents as tools or sub-agents.

## Features

- **LangGraph Agent**: Basic conversational agent using LangGraph
- **A2A Server**: FastAPI server exposing agent capabilities via Agent Card JSON
- **Remote Agent Integration**: Connect to and use remote agents
- **JSON-RPC Protocol**: Standardized communication protocol

## Architecture

- **Framework**: LangGraph, Google ADK, FastAPI
- **Protocol**: JSON-RPC 2.0
- **Discovery**: Agent Card JSON endpoint
- **Communication**: HTTP-based agent communication

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

### Running the LangGraph Agent Server

```bash
cd langraph_agent
uv run python server.py
# Server runs on http://localhost:8002
```

### Using Remote Agents

```bash
cd remote_adk_agent
uv run python agent.py
```

### User-Facing Agent with Remote Sub-Agents

```bash
cd user-facing-agent
# Uses remote agents as sub-agents
```

## Project Structure

```
a2a/
├── langraph_agent/
│   ├── graph.py          # LangGraph agent implementation
│   └── server.py         # FastAPI A2A server
├── remote_adk_agent/
│   └── agent.py          # Remote ADK agent setup
└── user-facing-agent/
    └── user_facing_agent/
        └── agent.py      # Main agent using remote sub-agents
```

## Key Concepts

### Agent Card JSON

Each agent exposes its capabilities via `.well-known/agent-card.json`:

```json
{
  "name": "AgentName",
  "description": "Agent description",
  "capabilities": {},
  "defaultInputModes": ["text/plain"],
  "defaultOutputModes": ["text/plain"],
  "protocolVersion": "0.3.0",
  "preferredTransport": "JSONRPC",
  "url": "http://localhost:8002/messages"
}
```

### JSON-RPC Messages

Agents communicate using JSON-RPC 2.0 protocol:

```json
{
  "jsonrpc": "2.0",
  "method": "message",
  "params": {
    "message": {
      "parts": [{"text": "User message"}]
    }
  }
}
```

### Remote Agent Usage

```python
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

remote_agent = RemoteA2aAgent(
    name="HistoryHelperAgent",
    description="Helps with history homework",
    agent_card="http://127.0.0.1:8001/.well-known/agent-card.json",
)
```

## Components

### LangGraph Agent Server
- FastAPI server exposing LangGraph agent
- Agent Card endpoint for discovery
- JSON-RPC message handling
- Simple START → LLM → END graph

### Remote ADK Agent
- Google ADK agent configured for remote access
- Exposes agent via A2A protocol
- Can be discovered and used by other agents

### User-Facing Agent
- Main agent that uses remote agents as sub-agents
- Demonstrates agent composition
- Shows distributed agent architecture

## Use Cases

- Multi-agent systems
- Distributed agent networks
- Agent service discovery
- Agent composition and orchestration
- Microservices-style agent architecture

## Benefits

- **Modularity**: Agents can be developed independently
- **Reusability**: Agents can be used by multiple systems
- **Scalability**: Distribute agents across services
- **Discovery**: Standardized agent discovery mechanism

## Extending

- Add more agent types
- Implement agent discovery registry
- Add authentication and security
- Implement agent versioning
- Add monitoring and logging
- Create agent marketplace

