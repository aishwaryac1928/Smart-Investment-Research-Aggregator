# 🤖 AI Usage Documentation

This document explains how AI tools were used in building the **Smart Investment Research Aggregator**.

---

## 1. AI Tools Used
- **ChatGPT (GPT-5)** → For code scaffolding, bug fixing, and documentation  
- **GitHub Copilot** → For inline coding suggestions while writing backend and frontend code  

---

## 2. Prompts Used
Examples of prompts used during development:
- My FastAPI endpoint fetches multiple research files and calls an AI summarization model. The response is slow (2–3s).  

- How can I optimize performance — caching, async requests, or background tasks? Can you provide code examples?

- In my React frontend, I want to manage loading state across multiple API calls (fetching research, synthesizing, saving report).  

- Should I use React Context, Redux, or local component state? What’s the cleanest approach for a small but extensible project?

- I need to let users export research briefs as both PDF and Markdown. What’s the best way to implement this in a React + FastAPI stack? 

- Should I generate the PDF on the client or backend, and which libraries are best?

- How should I design a test plan for an AI-driven research app? I want to cover unit tests, integration tests, and some way of validating
  AI-generated summaries for consistency.

---

## 🔹 Output Validation

- Manually reviewed every AI-generated snippet.

- Adjusted boilerplate and rewrote logic when needed.

- Ran unit tests + manual UI checks before accepting.

---

## 🔹 Where AI Helped Most

- Backend endpoint design

- Consensus + synthesis logic

- Confidence scoring algorithms

---

🔹 Where AI Didn’t Help Much

- Debugging React state bugs

- Pixel-perfect CSS adjustments


