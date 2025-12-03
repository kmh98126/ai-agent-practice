# Job Hunter Agent

Comprehensive job search and interview preparation system that finds jobs, optimizes resumes, researches companies, and prepares interview strategies using CrewAI.

## Overview

This multi-agent system helps job seekers by automating the entire job search process: finding opportunities, matching to resume, optimizing resume, researching companies, and preparing for interviews.

## Features

- **Job Discovery**: Searches and extracts job listings from web
- **Smart Matching**: Scores jobs based on resume alignment (1-5)
- **Resume Optimization**: Tailors resume for specific job postings
- **Company Research**: Deep research on hiring companies
- **Interview Prep**: Comprehensive interview preparation guides
- **Knowledge Source**: Uses resume as knowledge base

## Architecture

- **Framework**: CrewAI
- **Agents**: 5 specialized agents working in chain
- **Configuration**: YAML files for agents and tasks
- **Knowledge**: TextFileKnowledgeSource for resume data

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
cat > .env << EOF
OPENAI_API_KEY=your_key_here
FIRECRAWL_API_KEY=your_key_here
EOF

# Add your resume to knowledge/
cp your_resume.txt knowledge/resume.txt
```

## Usage

```bash
# Run the job hunter
uv run python main.py

# Or customize in code:
result = JobHunterCrew().crew().kickoff(
    inputs={
        "level": "Senior",
        "position": "Golang Developer",
        "location": "Netherlands",
    }
)
```

## Agent Chain

### 1. Job Search Agent
- **Role**: Senior Job Market Research Specialist
- **Task**: Search and extract job listings
- **Tools**: Web search tool
- **Output**: JobList (structured job data)

### 2. Job Matching Agent
- **Role**: Job Matching Expert
- **Task**: Evaluate job-resume alignment
- **Knowledge**: Resume text file
- **Output**: RankedJobList (jobs with match scores 1-5)

### 3. Job Selection Task
- **Role**: Job Selection Expert
- **Task**: Select best-fit job
- **Output**: ChosenJob (single selected job)

### 4. Resume Optimization Agent
- **Role**: Resume Optimization Specialist
- **Task**: Rewrite resume for selected job
- **Knowledge**: Original resume
- **Output**: Optimized resume (Markdown)

### 5. Company Research Agent
- **Role**: Company Research and Interview Strategist
- **Task**: Research hiring company
- **Tools**: Web search tool
- **Output**: Company research report (Markdown)

### 6. Interview Prep Agent
- **Role**: Interview Strategist and Preparation Coach
- **Task**: Create comprehensive interview guide
- **Context**: Job, optimized resume, company research
- **Output**: Interview preparation document (Markdown)

## Project Structure

```
job-hunter-agent/
├── main.py                    # Main crew orchestration
├── models.py                  # Pydantic models (JobList, etc.)
├── tools.py                   # Web search tool
├── config/
│   ├── agents.yaml           # Agent configurations
│   └── tasks.yaml            # Task definitions
├── knowledge/
│   └── resume.txt            # Your resume (add here)
└── output/
    ├── rewritten_resume.md   # Generated optimized resume
    ├── company_research.md   # Generated company research
    └── interview_prep.md     # Generated interview prep
```

## Configuration

### Agents (config/agents.yaml)
- Define agent roles, goals, and backstories
- Configure LLM models
- Set verbose mode

### Tasks (config/tasks.yaml)
- Define task descriptions
- Specify expected outputs
- Set agent assignments
- Configure output files

## Output Files

All outputs are saved in `output/` directory:

1. **rewritten_resume.md**: Tailored resume for selected job
2. **company_research.md**: Company overview, mission, recent news, interview topics
3. **interview_prep.md**: Comprehensive interview preparation guide

## Key Features

### Resume Matching
- Analyzes tech stack alignment
- Matches role level and experience
- Considers industry preferences
- Evaluates remote/work flexibility
- Scores from 1 (poor fit) to 5 (perfect fit)

### Resume Optimization
- Reorders and highlights relevant skills
- Matches job keywords
- Maintains honesty (no fabrication)
- ATS-friendly formatting

### Interview Prep
- Job overview and fit analysis
- Resume highlights for the role
- Company summary and values
- Predicted interview questions
- Questions to ask interviewer
- Strategic advice

## Customization

- Modify agent configurations in YAML
- Adjust matching criteria
- Add more job sources
- Customize resume templates
- Add industry-specific prep
- Implement tracking and follow-up

## Use Cases

- Job search automation
- Resume optimization
- Interview preparation
- Career transition support
- Skill gap analysis

## Tips

- Keep resume.txt up to date
- Provide specific location and level
- Review and refine generated content
- Customize agents for your industry
- Use output as starting point, not final version

## Example Output Structure

### Interview Prep Document
```markdown
# Interview Prep: Company Name – Job Title

## Job Overview
## Why This Job Is a Fit
## Resume Highlights for This Role
## Company Summary
## Predicted Interview Questions
## Questions to Ask Them
## Concepts To Know/Review
## Strategic Advice
```

