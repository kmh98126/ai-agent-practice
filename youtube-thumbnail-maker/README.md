# YouTube Thumbnail Maker

Automatically generates YouTube thumbnails from video content by extracting audio, transcribing, summarizing, and creating multiple thumbnail candidates for user selection.

## Overview

This project implements a complete workflow that processes video files to generate optimized YouTube thumbnails. It demonstrates advanced LangGraph patterns including parallel processing, human-in-the-loop feedback, and integration with external tools.

## Features

- **Video Processing**: Extracts and speeds up audio from video files
- **Speech-to-Text**: Transcribes audio using OpenAI Whisper
- **Intelligent Summarization**: 
  - Parallel chunk summarization for efficiency
  - Mega summary that combines all chunks
- **Thumbnail Generation**: Creates 5 thumbnail candidates in parallel
- **Human-in-the-Loop**: User selects best thumbnail and provides feedback
- **High-Quality Output**: Generates final HD thumbnail based on feedback

## Architecture

- **Framework**: LangGraph
- **External Tools**: ffmpeg, OpenAI Whisper, DALL-E (via OpenAI)
- **Patterns**: Send pattern for parallel processing, interrupt for feedback
- **State Management**: TypedDict for type safety

## Installation

```bash
# Install dependencies
uv sync

# Install ffmpeg (required for audio extraction)
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the thumbnail generator
uv run python main.py

# The workflow will:
# 1. Process your video file
# 2. Generate 5 thumbnail candidates
# 3. Wait for your feedback
# 4. Generate final HD thumbnail
```

## Workflow Stages

### 1. Audio Extraction
- Extracts audio from video file using ffmpeg
- Speeds up audio 2x for faster processing
- Converts to MP3 format

### 2. Transcription
- Uses OpenAI Whisper for accurate transcription
- Supports language hints and custom prompts
- Returns full text transcript

### 3. Parallel Summarization
- Splits transcript into 500-character chunks
- Uses `Send` pattern to process chunks in parallel
- Each chunk summarized independently

### 4. Mega Summary
- Combines all individual summaries
- Creates comprehensive video summary
- Used for thumbnail prompt generation

### 5. Parallel Thumbnail Generation
- Generates 5 different thumbnail concepts simultaneously
- Each with unique visual descriptions
- Creates low-quality preview images

### 6. Human Feedback
- User reviews all 5 thumbnails
- Selects favorite and provides feedback
- System waits for input using `interrupt()`

### 7. Final HD Thumbnail
- Incorporates user feedback into prompt
- Generates high-quality final thumbnail
- Optimized for YouTube thumbnail specifications

## Project Structure

```
youtube-thumbnail-maker/
├── graph.py              # Main workflow graph
├── langgraph.json        # LangGraph configuration
├── main.ipynb            # Example notebook
└── thumbnail_*.jpg       # Generated thumbnails (ignored by git)
```

## Key LangGraph Patterns

1. **Send Pattern**: Parallel processing of thumbnail candidates
   ```python
   def dispatch_artists(state: State):
       return [Send("generate_thumbnails", {...}) for i in [1,2,3,4,5]]
   ```

2. **Interrupt Pattern**: Collecting user feedback
   ```python
   def human_feedback(state: State):
       answer = interrupt({"chosen_thumbnail": "...", "feedback": "..."})
       return answer
   ```

3. **TypedDict State**: Type-safe state management

## Customization

- Adjust chunk size for summarization
- Modify number of thumbnail candidates
- Change thumbnail generation prompts
- Add filters or post-processing steps
- Integrate with YouTube API for automatic upload

## Tips

- Use high-quality video files for better transcription
- Provide clear feedback for better final results
- Experiment with different thumbnail concepts
- Consider your YouTube channel's visual style

## Dependencies

- langgraph
- openai (for Whisper and DALL-E)
- ffmpeg (system dependency)

## Output

- `thumbnail_1.jpg` through `thumbnail_5.jpg`: Candidate thumbnails
- `thumbnail_final.jpg`: Final high-quality thumbnail

