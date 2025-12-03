# My First Agent

A beginner-friendly introduction to building AI agents with function calling, demonstrating the basics of tool integration and agent interaction patterns.

## Overview

This is the simplest possible AI agent example that demonstrates the core concepts of function calling, tool definition, and basic agent interaction using OpenAI's API.

## Features

- **Simple Function Calling**: Basic tool integration
- **Tool Definition**: How to define and register tools
- **Agent Interaction**: Basic conversation flow
- **Weather Tool**: Example tool implementation

## Architecture

- **Framework**: OpenAI API (direct usage)
- **Pattern**: Function calling
- **Tools**: Custom Python functions

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run in Jupyter notebook
uv run jupyter notebook main.ipynb
```

## Key Concepts

### Tool Definition
Define tools using OpenAI's function calling format:

```python
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "A function to get the weather of a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to get the weather of.",
                    }
                },
                "required": ["city"],
            },
        },
    }
]
```

### Function Implementation
Implement the actual function:

```python
def get_weather(city):
    return "33 degrees celsius."

FUNCTION_MAP = {
    "get_weather": get_weather,
}
```

### Agent Interaction
1. Send user message to OpenAI
2. Check if function calling is requested
3. Execute function if needed
4. Send function result back
5. Get final response

## Project Structure

```
my-first-agent/
├── main.ipynb          # Main notebook with examples
└── pyproject.toml      # Dependencies
```

## Learning Objectives

After completing this project, you'll understand:

1. **Function Calling**: How agents can call functions
2. **Tool Definition**: How to define tools for agents
3. **Response Processing**: How to handle function calls
4. **Basic Workflow**: The agent-tool interaction cycle

## Next Steps

- Add more tools (calculator, translator, etc.)
- Implement more complex logic
- Add error handling
- Explore other frameworks (LangGraph, CrewAI, etc.)
- Build more sophisticated agents

## Example Interaction

```
User: "What's the weather in Seoul?"

Agent: [calls get_weather("Seoul")]
Tool: Returns "33 degrees celsius."

Agent: "The weather in Seoul is 33 degrees celsius."
```

## Extending

Try adding:
- Calculator tool
- Date/time tool
- Text processing tools
- API integration tools
- Database query tools

## Perfect For

- AI agent beginners
- Learning function calling
- Understanding tool patterns
- Building simple assistants
- Quick prototyping

