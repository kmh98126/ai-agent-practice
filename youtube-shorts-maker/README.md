# YouTube Shorts Maker

Fully automated YouTube Shorts generation system that plans content, generates assets (images and voice), and assembles complete videos using Google ADK.

## Overview

This project demonstrates a sophisticated multi-agent system that creates complete YouTube Shorts from a topic, including content planning, asset generation, and video assembly.

## Features

- **Content Planning**: Structures video into scenes with narration and visuals
- **Parallel Asset Generation**: Creates images and voice simultaneously
- **Video Assembly**: Combines all assets into final video
- **Structured Output**: Uses Pydantic models for scene definition
- **Input Filtering**: Callback-based content filtering

## Architecture

- **Framework**: Google ADK
- **Pattern**: Main agent with ParallelAgent for assets
- **Sub-Agents**: Content Planner, Asset Generator (Image + Voice), Video Assembler
- **Output**: Complete video files

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Usage

```bash
# Run the shorts maker
uv run python -m youtube_shorts_maker.agent

# Provide a topic to the agent
```

## Agent Structure

### Main Agent: Shorts Producer Agent
- Coordinates all sub-agents
- Manages workflow from topic to video
- Implements input filtering (before_model_callback)
- Orchestrates content planning → asset generation → assembly

### Sub-Agents

#### 1. Content Planner Agent
- **Input**: Topic
- **Output**: ContentPlanOutput (Pydantic model)
  - Topic
  - Total duration (max 20 seconds)
  - List of scenes, each with:
    - Scene ID
    - Narration text
    - Visual description
    - Embedded text and location
    - Duration in seconds

#### 2. Asset Generator Agent (ParallelAgent)
- **Type**: ParallelAgent for simultaneous execution
- **Sub-Agents**:
  - **Image Generator**: Creates images for each scene
  - **Voice Generator**: Generates narration audio
- **Output**: All visual and audio assets

#### 3. Video Assembler Agent
- **Input**: Content plan + generated assets
- **Tools**: `assemble_video()` function
- **Output**: Final assembled video file

## Project Structure

```
youtube-shorts-maker/
├── youtube_shorts_maker/
│   ├── agent.py              # Main producer agent
│   ├── prompt.py             # Agent prompts
│   └── sub_agents/
│       ├── content_planner/
│       │   ├── agent.py
│       │   └── prompt.py
│       ├── asset_generator/
│       │   ├── agent.py      # ParallelAgent
│       │   ├── image_generator/
│       │   └── voice_generator/
│       └── video_assembler/
│           ├── agent.py
│           ├── prompt.py
│           └── tools.py      # Video assembly tool
└── pyproject.toml
```

## Workflow

1. **Content Planning**
   - User provides topic
   - Content Planner creates structured scene plan
   - Defines narration, visuals, text overlays

2. **Asset Generation** (Parallel)
   - Image Generator creates visuals for each scene
   - Voice Generator creates narration audio
   - Both run simultaneously for efficiency

3. **Video Assembly**
   - Video Assembler combines all assets
   - Matches audio with visuals
   - Adds text overlays at specified locations
   - Creates final video file

## Key Features

### Structured Output
```python
class SceneOutput(BaseModel):
    id: int
    narration: str
    visual_description: str
    embedded_text: str
    embedded_text_location: str
    duration: int
```

### Parallel Processing
- Asset generation happens simultaneously
- Reduces total generation time
- Uses ParallelAgent pattern

### Input Filtering
```python
def before_model_callback(callback_context, llm_request):
    # Filter inappropriate content
    if "hummus" in text:
        return blocked_response
    return None
```

## Use Cases

- Automated YouTube content creation
- Social media video generation
- Educational video creation
- Marketing video production
- Content repurposing

## Customization

- Adjust video length limits
- Modify scene structure
- Customize visual style
- Add more asset types
- Implement brand guidelines
- Add music and effects

## Tips

- Provide clear, specific topics
- Review generated content for quality
- Adjust prompts for your style
- Test with different topics
- Optimize for your audience

## Output

- Generated image assets
- Generated voice audio
- Final assembled video file
- Scene metadata and structure

## Dependencies

- google-cloud-aiplatform[adk]
- litellm
- Image generation APIs
- Voice synthesis APIs
- Video editing libraries

