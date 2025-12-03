# Workflow Testing

Comprehensive testing patterns for LangGraph workflows, including end-to-end tests, individual node tests, and LLM-based evaluation.

## Overview

This project demonstrates best practices for testing LangGraph workflows, showing how to test entire graphs, individual nodes, and evaluate outputs using LLMs.

## Features

- **End-to-End Testing**: Test complete workflow execution
- **Node-Level Testing**: Test individual nodes in isolation
- **Partial Execution**: Test workflows from specific points
- **LLM-Based Evaluation**: Use LLMs to evaluate output quality
- **Parametrized Tests**: Test multiple scenarios efficiently

## Architecture

- **Framework**: LangGraph
- **Testing**: Pytest
- **Evaluation**: LLM-based similarity scoring
- **State Management**: EmailState (from email-refiner-agent pattern)

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run all tests
uv run pytest tests.py -v

# Run specific test
uv run pytest tests.py::test_full_graph -v
```

## Testing Patterns

### 1. Full Workflow Testing
Tests the complete graph execution:

```python
def test_full_graph(email, expected_category, min_score, max_score):
    result = graph.invoke({"email": email}, config={"thread_id": "1"})
    assert result["category"] == expected_category
    assert min_score <= result["priority_score"] <= max_score
```

### 2. Individual Node Testing
Tests nodes in isolation:

```python
def test_individual_nodes():
    result = graph.nodes["categorize_email"].invoke({"email": "..."})
    assert result["category"] == "spam"
```

### 3. Partial Execution Testing
Tests workflow from specific points:

```python
def test_partial_execution():
    graph.update_state(config={...}, values={...}, as_node="categorize_email")
    result = graph.invoke(None, config={...}, interrupt_after="draft_response")
```

### 4. LLM-Based Evaluation
Uses LLM to evaluate output quality:

```python
def judge_response(response: str, category: str):
    result = s_llm.invoke(f"Score similarity...")
    return result.similarity_score
```

## Project Structure

```
workflow-testing/
├── main.py              # Workflow implementation (email-refiner pattern)
├── tests.py             # Comprehensive test suite
└── pyproject.toml       # Dependencies
```

## Test Categories

### Parametrized Tests
Test multiple scenarios efficiently:

```python
@pytest.mark.parametrize(
    "email, expected_category, min_score, max_score",
    [
        ("this is urgent!", "urgent", 8, 10),
        ("i wanna talk to you", "normal", 4, 7),
        ("i have an offer for you", "spam", 1, 3),
    ],
)
```

### State Management Tests
Test state updates and persistence:

```python
graph.update_state(
    config={"thread_id": "1"},
    values={"email": "...", "category": "spam"},
    as_node="categorize_email",
)
```

### Output Evaluation
Compare outputs against expected examples:

```python
similarity_score = judge_response(result["response"], "spam")
assert similarity_score >= 70
```

## Key Testing Concepts

1. **Configurable Thread IDs**: Test multiple workflows in parallel
2. **State Manipulation**: Modify state at specific points
3. **Interrupt Testing**: Test human-in-the-loop scenarios
4. **LLM Evaluation**: Use AI to evaluate AI outputs

## Best Practices

- Use parametrized tests for multiple scenarios
- Test both happy paths and edge cases
- Isolate node testing for debugging
- Use LLM evaluation for fuzzy outputs
- Test state persistence and restoration
- Verify error handling

## Use Cases

- Validating workflow correctness
- Regression testing
- Performance benchmarking
- Output quality assurance
- Integration testing
- User acceptance testing

## Extending Tests

- Add more test scenarios
- Implement performance tests
- Add stress testing
- Create visual test reports
- Add continuous integration
- Implement test coverage tracking

