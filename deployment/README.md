# Deployment

Production-ready API deployment example for AI agents using FastAPI, demonstrating RESTful endpoints, streaming responses, and conversation management.

## Overview

This project shows how to deploy an AI agent as a production API service with conversation management, streaming support, and standard REST endpoints.

## Features

- **RESTful API**: Standard HTTP endpoints
- **Conversation Management**: OpenAI Conversations API integration
- **Streaming Support**: Server-Sent Events (SSE) for real-time responses
- **FastAPI**: Modern, fast web framework
- **Production Ready**: Railway deployment configuration included

## Architecture

- **Framework**: FastAPI, OpenAI Agents SDK
- **API**: RESTful endpoints
- **Streaming**: Server-Sent Events
- **Deployment**: Railway-ready configuration

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

### Development

```bash
# Run the API server
uv run uvicorn main:app --reload

# Server runs on http://localhost:8000
```

### Production

```bash
# Using Railway or similar platform
# Railway will auto-detect and deploy
```

## API Endpoints

### Health Check
```
GET /
Response: {"message": "hello world"}
```

### Create Conversation
```
POST /conversations
Response: {
    "conversation_id": "conv_..."
}
```

### Send Message (Sync)
```
POST /conversations/{conversation_id}/message
Body: {
    "question": "Your question here"
}
Response: {
    "answer": "Agent's response"
}
```

### Send Message (Stream)
```
POST /conversations/{conversation_id}/message-stream
Body: {
    "question": "Your question here"
}
Response: text/plain stream (SSE)
```

### Send Message (Stream All Events)
```
POST /conversations/{conversation_id}/message-stream-all
Body: {
    "question": "Your question here"
}
Response: All events as JSON lines
```

## Project Structure

```
deployment/
├── main.py              # FastAPI application
├── railway.json         # Railway deployment config
├── api.http             # API testing file
└── pyproject.toml       # Dependencies
```

## Key Components

### Agent Setup
```python
agent = Agent(
    name="Assistant",
    instructions="You help users with their questions.",
)
```

### Conversation Management
```python
# Create conversation
conversation = await client.conversations.create()

# Use conversation ID for context
answer = await Runner.run(
    starting_agent=agent,
    input=question,
    conversation_id=conversation_id,
)
```

### Streaming
```python
async def event_generator():
    events = Runner.run_streamed(...)
    async for event in events.stream_events():
        if event.data.type == "response.output_text.delta":
            yield event.data.delta

return StreamingResponse(event_generator(), media_type="text/plain")
```

## Deployment

### Railway

1. Connect your GitHub repository
2. Railway auto-detects the project
3. Set environment variables:
   - `OPENAI_API_KEY`
4. Deploy automatically

### Manual Deployment

```bash
# Build and run
uv sync
uv run uvicorn main:app --host 0.0.0.0 --port $PORT
```

## API Testing

Use the included `api.http` file or tools like:
- Postman
- curl
- httpie
- Insomnia

### Example curl Commands

```bash
# Create conversation
curl -X POST http://localhost:8000/conversations

# Send message
curl -X POST http://localhost:8000/conversations/{id}/message \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello!"}'

# Stream response
curl -X POST http://localhost:8000/conversations/{id}/message-stream \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello!"}' \
  --no-buffer
```

## Use Cases

- Production AI agent services
- API-first agent architectures
- Microservices integration
- Mobile app backends
- Web application backends
- Enterprise integrations

## Customization

- Add authentication (API keys, OAuth)
- Implement rate limiting
- Add request logging
- Customize agent instructions
- Add more endpoints
- Implement webhooks
- Add monitoring and metrics

## Security Considerations

- Add API authentication
- Implement rate limiting
- Validate input
- Sanitize outputs
- Add CORS configuration
- Use HTTPS in production

## Performance

- FastAPI async support
- Streaming for large responses
- Efficient conversation management
- Connection pooling
- Scalable architecture

## Monitoring

- Add logging
- Implement health checks
- Track API usage
- Monitor response times
- Error tracking
- Analytics integration

