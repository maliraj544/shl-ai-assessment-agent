# SHL AI Assessment Recommendation System

An AI-powered recommendation system for SHL assessments using semantic search and LLM-based reasoning.

## Features

- Semantic search using Sentence Transformers
- FAISS vector database
- Conversational AI recommendations
- FastAPI backend
- SHL assessment recommendation engine
- REST API endpoints

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- FAISS
- OpenRouter LLM
- Uvicorn

## Endpoints

### Health Check

GET /health

### Assessment Recommendation

POST /recommend

Example Request:

```json
{
  "query": "I want to hire frontend developers"
}