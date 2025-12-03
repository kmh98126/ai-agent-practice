# Customer Support Agent

Voice-enabled multi-agent customer support system with intelligent routing, specialized support agents, and guardrails for safety and quality.

## Overview

This project implements a sophisticated customer support system that handles voice input, routes inquiries to specialized agents, and provides comprehensive support across account, billing, order, and technical domains.

## Features

- **Voice Interface**: Voice input and audio output support
- **Intelligent Routing**: Triage agent classifies and routes inquiries
- **Specialized Agents**: 
  - Account Management Agent
  - Billing Support Agent
  - Order Management Agent
  - Technical Support Agent
- **Guardrails**: Input and output filtering for safety
- **Handoff Mechanism**: Seamless agent-to-agent transfers
- **Context Awareness**: Customer tier-based service levels

## Architecture

- **Framework**: OpenAI Agents SDK, Streamlit
- **Voice**: VoicePipeline for audio processing
- **Session**: SQLiteSession for conversation history
- **Guardrails**: Input and output filtering

## Installation

```bash
# Install dependencies
uv sync

# Install system dependencies for audio
# macOS
brew install portaudio

# Linux
sudo apt-get install portaudio19-dev

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the Streamlit app
uv run streamlit run main.py
```

## Agent Structure

### Triage Agent
- **Role**: Classifies customer inquiries
- **Function**: Routes to appropriate specialist
- **Categories**:
  - Technical Support: Product issues, bugs, how-to
  - Billing Support: Payments, subscriptions, refunds
  - Order Management: Shipping, returns, tracking
  - Account Management: Login, security, profile

### Account Management Agent
- **Tools**:
  - `reset_user_password()`: Password reset
  - `enable_two_factor_auth()`: 2FA setup
  - `update_account_email()`: Email changes
  - `deactivate_account()`: Account closure
  - `export_account_data()`: Data export
- **Focus**: Account access and security

### Billing Support Agent
- **Tools**:
  - `lookup_billing_history()`: Payment history
  - `process_refund_request()`: Refund processing
  - `update_payment_method()`: Payment updates
  - `apply_billing_credit()`: Account credits
- **Focus**: Billing and payment issues

### Order Management Agent
- **Tools**:
  - `lookup_order_status()`: Order tracking
  - `initiate_return_process()`: Returns
  - `schedule_redelivery()`: Redelivery scheduling
  - `expedite_shipping()`: Priority shipping (premium)
- **Focus**: Order status and fulfillment

### Technical Support Agent
- **Tools**:
  - `run_diagnostic_check()`: System diagnostics
  - `provide_troubleshooting_steps()`: Step-by-step help
  - `escalate_to_engineering()`: Advanced issues
- **Guardrails**: Output filtering for technical accuracy
- **Focus**: Product and technical issues

## Project Structure

```
customer-support-agent/
├── main.py                    # Streamlit app and workflow
├── workflow.py                # Voice workflow implementation
├── models.py                  # UserAccountContext model
├── output_guardrails.py       # Output filtering
├── my_agents/
│   ├── triage_agent.py       # Main routing agent
│   ├── account_agent.py      # Account management
│   ├── billing_agent.py      # Billing support
│   ├── order_agent.py        # Order management
│   └── technical_agent.py    # Technical support
├── tools.py                   # Agent tools
└── customer-support-memory.db # SQLite session
```

## Key Features

### Voice Pipeline
- Audio input processing
- Voice-to-text transcription
- Text-to-speech output
- Real-time audio streaming

### Handoff Mechanism
- Agents can transfer to other agents
- Maintains conversation context
- Provides transfer reason
- Visual handoff indicators

### Dynamic Instructions
- Adapts based on customer context
- Tier-based service levels
- Personalized responses
- Context-aware tool selection

### Guardrails

#### Input Guardrail
- Filters off-topic requests
- Ensures appropriate scope
- Prevents abuse

#### Output Guardrail (Technical)
- Filters technical responses
- Ensures accuracy
- Prevents misinformation

## Customer Context

```python
UserAccountContext(
    customer_id=1,
    name="nico",
    tier="basic",  # or "premium", "enterprise"
    email="customer@example.com"
)
```

### Tier-Based Features
- **Premium/Enterprise**: Priority processing
- **Basic**: Standard service
- Different response times and features

## Workflow

1. **Voice Input**: Customer speaks their issue
2. **Transcription**: Voice converted to text
3. **Triage**: Classifies and routes to specialist
4. **Handoff**: Transfers to appropriate agent
5. **Support**: Specialist agent handles inquiry
6. **Voice Output**: Response converted to audio

## Use Cases

- Customer service automation
- Voice-enabled support
- Multi-domain support systems
- Tiered service levels
- Context-aware assistance

## Customization

- Add more specialized agents
- Customize tool implementations
- Modify guardrail rules
- Add new support categories
- Integrate with CRM systems
- Add analytics and tracking

## Tips

- Test voice input/output quality
- Customize agent prompts for your business
- Adjust guardrails for your needs
- Implement proper error handling
- Monitor conversation quality
- Collect feedback for improvements

## Security Considerations

- Input guardrails prevent abuse
- Customer context validation
- Secure tool implementations
- Privacy-compliant data handling
- Audit logging capabilities

