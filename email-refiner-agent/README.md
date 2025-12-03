# Email Refiner Agent

Automatically classifies emails, assigns priority scores, and drafts appropriate responses using a sequential LangGraph workflow.

## Overview

This project demonstrates a complete email processing pipeline that categorizes emails (spam/normal/urgent), assigns priority scores, and generates contextually appropriate responses.

## Features

- **Email Classification**: Categorizes emails into spam, normal, or urgent
- **Priority Scoring**: Assigns priority scores from 1-10 based on category and content
- **Response Drafting**: Generates appropriate responses for each category
- **Structured Workflow**: Sequential processing with clear state transitions
- **Type Safety**: Uses Pydantic models for structured output

## Architecture

- **Framework**: LangGraph
- **State Management**: TypedDict with email state
- **Structured Output**: Pydantic models for classification and scoring
- **LLM**: OpenAI GPT-4o with structured output support

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the email refiner
uv run python main.py
```

## Workflow Stages

### 1. Email Classification
- Analyzes email content
- Categorizes into: spam, normal, or urgent
- Uses structured output for consistent classification

### 2. Priority Assignment
- Considers email category and content
- Assigns score from 1-10:
  - Urgent: usually 8-10
  - Normal: usually 4-7
  - Spam: usually 1-3

### 3. Response Drafting
- Generates category-appropriate responses
- Acknowledges urgency for urgent emails
- Professional tone for normal emails
- Brief notice for spam

## Project Structure

```
email-refiner-agent/
├── main.py                    # Main workflow (workflow-architectures style)
├── travel_advisor_agent/      # Bonus: Travel advisor agent
│   ├── agent.py              # Travel agent implementation
│   └── prompt.py             # Travel agent prompts
└── session.db                # SQLite session (generated)
```

## Key Features

### Structured Output
Using Pydantic for reliable classification:

```python
class EmailClassificationOuput(BaseModel):
    category: Literal["spam", "normal", "urgent"]
```

### Sequential Workflow
Clear state transitions:
```
START → categorize_email → assign_priority → draft_response → END
```

### State Management
TypedDict ensures type safety:

```python
class EmailState(TypedDict):
    email: str
    category: Literal["spam", "normal", "urgent"]
    priority_score: int
    response: str
```

## Travel Advisor Agent (Bonus)

Includes a travel advisor agent with tools for:
- Weather information
- Currency exchange rates
- Local attractions lookup

## Testing

The project includes comprehensive tests:
- Full workflow testing
- Individual node testing
- Partial execution testing
- LLM-based response evaluation

Run tests:
```bash
uv run pytest tests.py
```

## Use Cases

- Email triage systems
- Automated customer service
- Email routing and prioritization
- Response suggestion systems
- Email filtering and classification

## Customization

- Adjust priority scoring criteria
- Customize response templates
- Add more categories
- Implement email threading
- Add sender reputation checking
- Integrate with email providers

## Next Steps

- Add email thread context
- Implement sender verification
- Add attachment handling
- Create email templates
- Integrate with email APIs
- Add multi-language support

