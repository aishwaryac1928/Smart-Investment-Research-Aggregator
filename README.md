# 📊 Smart Investment Research Aggregator

A full-stack project that aggregates investment research insights (consensus, risks, conflicting views) from multiple sources.  


---

## 🚀 Features
- Input: Company name & ticker
- Aggregates research data from multiple mock sources
- AI-powered synthesis:
  - Consensus views  
  - Conflicting opinions  
  - Confidence scores  
  - Key risks  
- Save & export research briefs
- Frontend (React) + Backend (FastAPI)
---

## How to Run

### 1. Backend (FastAPI)
```bash
cd backend
python -m venv venv
# Activate venv:
#   Linux/Mac: source venv/bin/activate
#   Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will be available at: http://127.0.0.1:8000


### 2. Frontend (React)
```bash
cd frontend
npm install
npm start
```

Frontend will run at: http://localhost:3000
(Connects automatically to FastAPI backend)


### Project Structure

Smart-Investment-Research-Aggregator/
│── backend/              # FastAPI app
│   ├── main.py           # API routes
│   ├── data.csv          # Mock research dataset
│   └── requirements.txt
│
│── frontend/             # React app
│   ├── src/App.js        # Main React component
│   ├── src/App.css       # Styles
│   └── package.json
│
│── docs/                 # Documentation
│   ├── Architecture.md
│   ├── AI_USAGE.md
│   └── TEST_PLAN.md
│
├── README.md            # Setup & usage
├── ARCHITECTURE.md      # System design docs
├── AI_USAGE.md          # AI usage documentation
├── TEST_PLAN.md         # Testing approach
└── .gitignore



### 📦 Tech Stack

- Frontend: React + CSS

- Backend: FastAPI + Uvicorn

- AI Integration: Text synthesis + contradiction detection

- Data: Mock CSV research data


### 🔮 Future Improvements

- Integrate real financial APIs (e.g., Alpha Vantage, Yahoo Finance).

- Add authentication for personalized dashboards.

- Store data in a database instead of CSV.

- Implement caching for faster repeat queries.

- Use LLM summarization for smarter aggregation of research text.

- Add unit & integration tests with CI/CD pipeline.


## 📸 Frontend Walkthrough

1. Landing Page – Input Form

- The user is presented with a simple and clean interface.

- Two input fields: Company Name and Ticker Symbol.

- A "Get Research Brief" button triggers the research aggregation process.

- The design is minimal and intuitive, making it easy for analysts to start their research.

![alt text](<Screenshot (30)-1.png>)


2. Research Brief – Consensus View & Conflicting Opinions

- After submitting a query, the system generates a structured research brief:

- Consensus View: A synthesized summary of the overall market opinion.

- Conflicting Opinions: Contradictory perspectives (e.g., growth potential vs. margin pressures).

- This ensures that users see both the broad agreement and the nuances in analyst reports.

<img width="1920" height="1080" alt="Screenshot (31)" src="https://github.com/user-attachments/assets/47bb7ab7-2606-4eab-968f-5425a634a872" />



3. Research Brief – Confidence Score & Export

- The detailed brief also includes:

- Confidence Score: AI-estimated measure of reliability for the consensus.

- Key Risks: Highlighting potential downside factors and uncertainties.

- Export Feature: A button to Export as DOCX, allowing users to save and share the research brief in a professional format.

<img width="1920" height="1080" alt="Screenshot (32)" src="https://github.com/user-attachments/assets/f767f6b0-7f54-4583-b6f5-c34b64489a7d" />

