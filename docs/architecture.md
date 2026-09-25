# AIDesk Architecture

## High-Level Architecture

User
    |
    v
Streamlit Frontend
    |
    v
FastAPI Backend
    |
    v
LangGraph Agent
    |
    +------------------+
    |                  |
    v                  v
SQL Agent           RAG Agent
    |                  |
    v                  v
PostgreSQL        PostgreSQL + pgvector
    |
    v
Business Data

The system will also contain:

- Guardrails
- Authentication
- Authorization
- Evaluation
- Observability
- Monitoring
- Deployment infrastructure