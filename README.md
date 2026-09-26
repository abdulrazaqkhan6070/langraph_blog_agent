# AI Blog Writer Agent

An AI-powered blog writing system built with LangGraph, FastAPI, Gemini, and Groq.

## Project Overview

This project uses multiple AI agents to automatically create and improve a blog post.

The workflow consists of:

1. **Researcher** — gathers useful information about the topic.
2. **Writer** — creates the initial blog draft.
3. **Editor** — reviews the draft.
4. **Router** — decides whether the draft should be approved or revised.
5. **Writer** — rewrites the draft when improvements are required.

The system can perform multiple revision cycles before producing the final blog.

## Technologies Used

* Python
* LangGraph
* LangChain
* Google Gemini
* Groq
* FastAPI
* Pydantic
* Uvicorn
* Python-dotenv
* Docker

## Workflow

```text
Client
  ↓
FastAPI
  ↓
Researcher
  ↓
Writer
  ↓
Editor
  ↓
Router
  ↓
Approved → Final Response
  ↓
Revision Required
  ↓
Writer → Editor
```

## API Endpoint

### POST `/blog`

Example request:

```json
{
  "topic": "Artificial Intelligence"
}
```

Example response:

```json
{
  "topic": "Artificial Intelligence",
  "draft": "Generated blog post...",
  "approved": true,
  "revision_count": 1
}
```

## Running with Docker

### 1. Build the Docker image

```bash
docker build -t ai-blog-agent .
```

### 2. Run the container

```bash
docker run -d -p 8000:8000 --env-file .env --name blog-agent ai-blog-agent
```

The application will run inside the Docker container and be accessible at:

```text
http://localhost:8000
```

### 3. Open FastAPI documentation

Open:

```text
http://localhost:8000/docs
```

You can use the Swagger UI to test the `/blog` endpoint.

### 4. View container logs

```bash
docker logs blog-agent
```

### 5. Stop the container

```bash
docker stop blog-agent
```

### 6. Start the container again

```bash
docker start blog-agent
```

## Environment Variables

Create a `.env` file containing the required API keys.

Example:

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

**Do not upload `.env` to GitHub.** API keys should remain private.

## Project Structure

```text
langraph_blog_agent/
│
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── graph.py
├── llm.py
├── main.py
├── nodes.py
├── requirements.txt
├── state.py
├── test_api.py
└── README.md
```
