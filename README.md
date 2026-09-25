# AIDesk — Enterprise AI Analyst

AIDesk is an enterprise AI analytics platform that allows users to interact with structured business data and unstructured documents using natural language.

## Project Goals

AIDesk aims to combine:

- LLMs
- Retrieval-Augmented Generation (RAG)
- Text-to-SQL
- Agentic AI
- Tool calling
- Guardrails
- AI evaluation
- Observability
- Production deployment

## Core Capabilities

### 1. SQL Analytics

Users can ask questions about structured business data using natural language.

Example:

> What were the total sales in 2025?

AIDesk generates and safely executes SQL against PostgreSQL.

### 2. Document Intelligence

Users can ask questions about uploaded documents.

AIDesk retrieves relevant information using RAG and generates an answer with evidence.

### 3. Agentic Reasoning

AIDesk can determine whether a question requires:

- SQL
- RAG
- Multiple tools
- Multi-step reasoning

## Technology Stack

- Python
- FastAPI
- Streamlit
- PostgreSQL
- pgvector
- LangGraph
- LLMs
- Embeddings
- Docker
- GitHub Actions
- Prometheus
- Grafana
- MLflow
- LangSmith

## Project Status

Currently completing:

- Milestone 1 — Project Definition + Architecture
- Milestone 2 — GitHub Repository + Professional Structure

## Repository Structure

```text
AIDesk/
├── backend/
├── frontend/
├── agents/
├── sql_agent/
├── rag/
├── guardrails/
├── evaluation/
├── database/
├── tests/
├── monitoring/
├── scripts/
├── docs/
├── data/
├── docker/
├── .github/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md