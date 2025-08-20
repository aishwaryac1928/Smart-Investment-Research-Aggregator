## 🏗️ System Architecture – Smart Investment Research Aggregator

This document explains the architecture and workflow of the Smart Investment Research Aggregator project.

## 📌 1. System Overview

The system is designed to aggregate multiple investment research sources, synthesize conflicting opinions using AI, and provide a structured research brief for financial analysts.

# Key components:

- Frontend (React): User interface for search and displaying research briefs.

- Backend (FastAPI): Handles data aggregation, AI synthesis, and API responses.

- AI Engine: Performs natural language synthesis to identify consensus, conflicts, confidence scores, and risks.

- Data Layer (Mock CSV): Stores simulated research inputs from different sources.


## 📐 2. System Architecture Diagram

flowchart LR

    User([User]) --> FE[Frontend (React)]
    FE --> BE[Backend (FastAPI)]
    BE --> AI[AI Engine (Synthesis)]
    BE --> Data[(Research Data - CSV)]
    AI --> BE
    BE --> FE
    FE --> User([Research Brief Output])

# Explanation:

- User interacts with the React app.

- The app calls FastAPI backend for research synthesis.

- Backend pulls data from mock CSV dataset.
 
- AI engine synthesizes conflicting information and produces structured insights.

- Results are returned to the frontend for display.


## 🔄 3. Workflow Diagram

flowchart TD

User[User enters Company Name & Ticker] --> FE[Frontend (React App)]
FE --> BE[Backend (FastAPI API)]
BE -->|Fetch mock data| Data[(Research Dataset - CSV)]
BE --> AI[AI Engine: Conflict Resolution & Synthesis]
AI --> BE
BE --> FE
FE --> User[User sees Research Report]

subgraph Research Report
    Consensus[Consensus Views]
    Conflicts[Conflicting Opinions]
    Risks[Key Risks]
    Confidence[Confidence Scores]
end

AI --> Research Report

# Explanation:

1. User searches a company (by name/ticker).

2. Frontend sends request to FastAPI backend.

3. Backend fetches research data from CSV (mock dataset).

4. AI engine synthesizes:

  - Consensus views

  - Conflicting opinions

  - Key risks

  - Confidence scores

5. Structured report returned to frontend for display.


## 📊 4. Key Design Choices

- React chosen for responsive and interactive frontend.

- FastAPI provides high-performance backend for API handling.

- CSV (mock) data simulates multiple research sources (can scale to APIs/DBs later).

- AI synthesis ensures comprehensive coverage of perspectives, even when analysts disagree.