# ChatGPT Clone

A full-featured ChatGPT-like conversational AI assistant with web search, file search, image generation, code execution, and MCP server integration.

## Overview

This project recreates the ChatGPT experience with Streamlit, featuring multiple tools, vector store integration, MCP servers, and real-time streaming responses.

## Features

- **Conversational Interface**: Streamlit-based chat interface
- **Multiple Tools**: 
  - Web search for current information
  - File search with vector store
  - Image generation (DALL-E)
  - Code interpreter for code execution
  - MCP server integration
- **Streaming Responses**: Real-time response streaming
- **Session Management**: SQLite-based conversation history
- **File Upload**: Support for text and image files

## Architecture

- **Framework**: OpenAI Agents SDK, Streamlit
- **Session**: SQLiteSession for persistence
- **Vector Store**: OpenAI Vector Store for file search
- **MCP Integration**: Model Context Protocol servers

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
cat > .env << EOF
OPENAI_API_KEY=your_key_here
VECTOR_STORE_ID=your_vector_store_id
EOF
```

## Usage

```bash
# Run the Streamlit app
uv run streamlit run main.py
```

## Features Detail

### Web Search Tool
- Searches the web for current information
- Automatically triggered when needed
- Provides real-time web results

### File Search Tool
- Uses OpenAI Vector Store
- Searches uploaded files
- Returns relevant file snippets

### Image Generation
- DALL-E integration
- High-quality image generation
- Partial image streaming
- JPEG output format

### Code Interpreter
- Python code execution
- Automatic container management
- Code streaming display
- Results visualization

### MCP Servers
Integrated servers:
- **Yahoo Finance**: Stock market data
- **Time**: Time zone and date information
- **Context7**: Software documentation

### File Upload
- Text files: Added to vector store
- Images: Included in conversation context
- Automatic processing

## Project Structure

```
chatgpt-clone/
├── main.py                    # Streamlit app
├── facts.txt                  # Sample knowledge file
├── chat-gpt-clone-memory.db  # SQLite session (generated)
└── pyproject.toml            # Dependencies
```

## Key Components

### Agent Configuration
```python
agent = Agent(
    name="ChatGPT Clone",
    instructions="You are a helpful assistant...",
    tools=[
        WebSearchTool(),
        FileSearchTool(vector_store_ids=[VECTOR_STORE_ID]),
        ImageGenerationTool(...),
        CodeInterpreterTool(...),
        HostedMCPTool(...),
    ],
)
```

### Session Management
- SQLiteSession for conversation persistence
- Message history tracking
- File and image context storage

### Streaming
- Real-time text streaming
- Code execution streaming
- Image generation progress
- Status indicators

## Setup Vector Store

1. Create a vector store in OpenAI
2. Get the vector store ID
3. Add to `.env`:
```env
VECTOR_STORE_ID=vs_your_store_id
```

## MCP Server Setup

### Yahoo Finance
```bash
uvx mcp-yahoo-finance
```

### Time Server
```bash
uvx mcp-server-time --local-timezone=America/New_York
```

## Use Cases

- General-purpose AI assistant
- Research assistant
- Code helper
- Image generation
- File analysis
- Market data queries

## Customization

- Add custom tools
- Integrate additional MCP servers
- Customize agent instructions
- Modify UI components
- Add more file types
- Implement user profiles

## Tips

- Upload relevant files for better context
- Use specific queries for best results
- Review generated code before execution
- Monitor API usage
- Customize agent instructions for your use case

## Features in Action

1. **Research Query**: "What's the latest news about AI?"
   - Agent uses web search tool
   - Returns current information

2. **File Analysis**: Upload a document and ask questions
   - Agent searches vector store
   - Answers based on file content

3. **Image Generation**: "Create an image of a sunset"
   - Agent generates image
   - Displays in chat

4. **Code Execution**: "Write Python code to sort a list"
   - Agent writes and executes code
   - Shows results

