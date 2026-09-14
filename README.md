# AI Blog Writer Agent

An AI-powered blog writing system built with LangGraph, FastAPI, Gemini, and Groq.

## Project Overview

This project uses multiple AI agents to automatically create and improve a blog post.

The workflow consists of:

1. Researcher — gathers useful information about the topic.
2. Writer — creates the initial blog draft.
3. Editor — reviews the draft.
4. Router — decides whether the draft should be approved or revised.
5. Writer — rewrites the draft when improvements are required.

The system can perform multiple revision cycles before producing the final blog.

## Technologies Used

- Python
- LangGraph
- LangChain
- Google Gemini
- Groq
- FastAPI
- Pydantic
- Uvicorn
- Python-dotenv

## Workflow

Client → FastAPI → Researcher → Writer → Editor → Router

If revision is required:

Router → Writer → Editor

If approved:

Router → Final Response

## API Endpoint

### POST `/blog`

Example request:

```json
{
  "topic": "Artificial Intelligence"
}

{
  "topic": "Artificial Intelligence",
  "draft": "Generated blog post...",
  "approved": true,
  "revision_count": 1
}