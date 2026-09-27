Smart Expense Tracker

A backend REST API for tracking personal expenses and getting AI-powered budgeting advice — built with FastAPI, PostgreSQL, and Google's Gemini API.

This was my first backend project, built from scratch as a way to learn real-world API development, database design, and how to integrate an LLM into a working application rather than just calling it in isolation.

Features
User authentication — registration and login with bcrypt password hashing
Bank account management — create and track accounts per user
Expense logging — log one or more expenses at once, with automatic category breakdown and totals (via pandas)
AI-powered budget advice — a Retrieval-Augmented Generation (RAG) pipeline that pulls a user's real spending history from the database, builds a grounded prompt, and asks Google Gemini for personalized, specific recommendations
Input validation — Pydantic constraints reject invalid data (e.g. negative expense amounts) before it ever reaches the database
Resilient external API calls — retry logic with backoff handles transient failures from the Gemini API gracefully
Fully containerized — one command (docker compose up --build) spins up the API and a PostgreSQL database together

Tech Stack:
Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy 2.0
Validation: Pydantic
Data processing: pandas
AI: Google Gemini API (via async httpx)
Auth: bcrypt
Containerization: Docker, Docker Compose

Architecture:
The codebase follows a layered architecture to keep concerns separated and testable:

├── routers/        # Thin HTTP route handlers — parse requests, call services, shape responses
├── services/        # Business logic and orchestration
├── repositories/     # Database access only — no business logic
├── db/
│   ├── models.py      # SQLAlchemy ORM models
│   ├── engine.py       # Database engine setup
│   └── session.py      # Session dependency for FastAPI
├── schemas.py       # Pydantic request/response schemas
├── ai_logic.py       # Prompt construction and the Gemini API call
├── calculations.py     # Expense aggregation logic (pandas)
└── main.py         # App setup, lifespan, router registration

Each layer only depends on the one directly below it — routers never touch the database directly, and repositories never contain business logic.

API Endpoints
Method	Endpoint	Description
POST	/Registration	Create a new user account
POST	/Login	Authenticate a user
POST	/Accounts	Create a bank account for a user
POST	/Categories	Log one or more expenses and get a category breakdown
POST	/AI	Get AI-generated budgeting advice based on real spending history

Full interactive documentation is available at /docs once the app is running.

Running Locally
With Docker (recommended)
Copy .env.example to .env and fill in your own values.
Run:
   docker compose up --build
Visit http://localhost:8000/docs.

Without Docker
Install dependencies:
   pip install -r requirements.txt
Set up a local PostgreSQL database and a .env file with your credentials.
Run:
   uvicorn main:app --reload

What I Learned:

Building a REST API with FastAPI, including dependency injection
Modeling relational data with SQLAlchemy and enforcing integrity with foreign keys
Structuring a codebase into repository/service/router layers for maintainability
Implementing a RAG pipeline connecting a real database to an LLM
Async Python, and specific pitfalls like forgetting to await a coroutine
Containerizing a multi-service app with Docker Compose
Managing secrets safely with environment variables instead of hardcoded config

Future Improvements:
Proper JWT-based authentication (the current version is a simplified, account-ID-based system)
Automated tests with pytest
A frontend (React) to consume this API
Multi-turn conversation support for the AI budgeting assistant