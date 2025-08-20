# 🧪 Test Plan - Smart Investment Research Aggregator

---

## 🔹 Objectives
- Ensure backend correctly aggregates and synthesizes research data  
- Verify frontend displays research briefs accurately  
- Validate end-to-end flow from input → synthesis → output  

---

## Test Strategy
- **Unit Tests (Backend):**
  - Input: valid company & ticker → Returns structured JSON
  - Input: invalid company → Returns 404 error
  - Edge case: multiple research entries → Conflicts captured
- **Integration Tests:**
  - Run frontend + backend together
  - Submit form with "Apple Inc., AAPL" → Verify rendered consensus, conflicts, risks
- **UI Tests:**
  - Empty form submission → Prevented
  - Loading state → Shows "Loading..."
  - Error state → Displays red error message

---

## Test Cases
| Test Case | Input | Expected Result |
|-----------|-------|-----------------|
| TC1 | Apple Inc., AAPL | JSON with brief (consensus + risks) |
| TC2 | Tesla Inc., TSLA | JSON with brief |
| TC3 | Unknown, XXX | 404 error |
| TC4 | Form empty | No API call, required validation |
| TC5 | Slow API | "Loading..." shown until response |

---

## Tools
- **Manual Testing:** Browser (React UI + FastAPI `/docs`)
- **Automated (optional):**
  - `pytest` for backend
  - React Testing Library for frontend