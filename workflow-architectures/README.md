# Workflow Architectures

Demonstrates parallel processing patterns in LangGraph using the `Send` pattern to process document chunks concurrently and aggregate results.

## Overview

This project shows how to efficiently process large documents by splitting them into chunks, processing each chunk in parallel, and then combining the results into a final summary.

## Features

- **Parallel Processing**: Process multiple document chunks simultaneously
- **Send Pattern**: LangGraph's `Send` pattern for concurrent execution
- **Result Aggregation**: Combines parallel results into coherent output
- **Efficient Processing**: Reduces total processing time through concurrency

## Architecture

- **Framework**: LangGraph
- **Pattern**: Send pattern for parallel execution
- **State Management**: TypedDict with annotated list merging
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
# Run the workflow
uv run jupyter notebook main.ipynb
```

## How It Works

### 1. Document Input
- Receives a document as input
- Documents are typically large text files

### 2. Chunking
- Splits document into paragraphs (using `\n\n` separator)
- Creates chunks with index tracking
- Prepares chunks for parallel processing

### 3. Parallel Summarization
- Uses `Send` pattern to dispatch multiple summarizer workers
- Each chunk is processed independently
- Results are automatically merged into state

### 4. Final Summary
- Combines all individual summaries
- Creates comprehensive final summary
- Maintains context across all chunks

## Project Structure

```
workflow-architectures/
├── main.ipynb           # Example notebook
├── fed_transcript.md    # Sample document (optional)
└── pyproject.toml       # Dependencies
```

## Key Concepts

### Send Pattern
The `Send` pattern allows dynamic parallel execution:

```python
def dispatch_summarizers(state: State):
    chunks = state["document"].split("\n\n")
    return [
        Send("summarize_p", {"paragraph": chunk, "index": index})
        for index, chunk in enumerate(chunks)
    ]
```

### Annotated List Merging
Using `Annotated[list[dict], add]` automatically merges results:

```python
class State(TypedDict):
    summaries: Annotated[list[dict], add]  # Automatically merges
```

### Conditional Edges
Routes to parallel processing based on dispatch:

```python
graph_builder.add_conditional_edges(
    "document_input",
    dispatch_summarizers,
    ["summarize_p"]  # Dynamic destinations
)
```

## Use Cases

- **Large Document Processing**: Summarize long documents efficiently
- **Batch Processing**: Process multiple items in parallel
- **Data Analysis**: Analyze multiple data points concurrently
- **Content Processing**: Process multiple content pieces simultaneously

## Benefits

1. **Performance**: Significantly faster than sequential processing
2. **Scalability**: Can process many chunks simultaneously
3. **Efficiency**: Better resource utilization
4. **Flexibility**: Easy to adjust chunk size and processing logic

## Customization

- Adjust chunk size and splitting strategy
- Modify summarization prompts
- Add preprocessing steps
- Implement result filtering
- Add progress tracking
- Optimize for specific document types

## Patterns Demonstrated

1. **Parallel Execution**: Multiple workers processing simultaneously
2. **State Aggregation**: Automatic merging of parallel results
3. **Dynamic Routing**: Conditional edges based on input
4. **TypedDict**: Type-safe state management

## Next Steps

- Add error handling for individual chunks
- Implement retry logic for failed chunks
- Add chunk prioritization
- Monitor and log processing times
- Implement result caching

