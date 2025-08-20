

# import json
# from fastapi import FastAPI, HTTPException
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# from pydantic import BaseModel
# import os
# import pandas as pd
# import requests

# # =============================
# # FastAPI app
# # =============================
# app = FastAPI(title="V Smart Investment Research Aggregator")

# # =============================
# # Serve React Build
# # =============================
# react_build_path = os.path.join(os.path.dirname(__file__), "..", "React", "my-app", "build")
# app.mount("/static", StaticFiles(directory=os.path.join(react_build_path, "static")), name="static")

# @app.get("/{full_path:path}")
# async def serve_react_app(full_path: str):
#     index_file = os.path.join(react_build_path, "index.html")
#     return FileResponse(index_file)

# # =============================
# # OpenRouter Setup
# # =============================
# OPENROUTER_API_KEY = "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"
# OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"  # OpenRouter endpoint
# MODEL_NAME = "openrouter/deepseek/deepseek-r1-0528:free"  # choose the OpenRouter model

# # =============================
# # Request / Response Models
# # =============================
# class ResearchRequest(BaseModel):
#     company: str
#     ticker: str

# class ResearchBrief(BaseModel):
#     consensus_view: str
#     conflicting_opinions: list
#     confidence_score: float
#     key_risks: list

# # =============================
# # API Endpoint
# # =============================
# @app.post("/api/research", response_model=dict)
# async def generate_research(request: ResearchRequest):
#     """Fetch research data from CSV and synthesize with OpenRouter"""
#     try:
#         # Load CSV file (ensure it's in backend/data.csv)
#         csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
#         df = pd.read_csv(csv_path)

#         # Filter company info
#         company_data = df[
#             (df["company"].str.lower() == request.company.lower()) |
#             (df["ticker"].str.upper() == request.ticker.upper())
#         ]

#         if company_data.empty:
#             raise HTTPException(status_code=404, detail="Company not found in dataset")

#         # Collect research texts
#         research_texts = company_data["research_text"].tolist()
#         combined_text = "\n\n".join(research_texts)

#         # OpenRouter API request
#         prompt = f"""
#         You are an expert financial analyst.
#         Given the following research texts for {request.company} ({request.ticker}):

#         {combined_text}

#         Please synthesize into a structured research brief with:
#         1. Consensus view
#         2. Conflicting opinions
#         3. Confidence score (0-1)
#         4. Key risks
#         Format output in JSON.
#         """

#         headers = {
#     "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#     "Content-Type": "application/json"
# }

#         payload = {
#     "model": MODEL_NAME,
#     "messages": [{"role": "user", "content": prompt}],
#     "temperature": 0.7,
#     "max_tokens": 500,
#     "stream": False
# }

#         response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
#         response.raise_for_status()
#         result = response.json()

#         # Extract model's text output
#         model_output = result["choices"][0]["message"]["content"]

#         try:
#             brief_json = json.loads(model_output)
#         except json.JSONDecodeError:
#             raise HTTPException(status_code=500, detail="Failed to parse model output as JSON")

#         return {"company": request.company, "ticker": request.ticker, "brief": brief_json}


#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import json
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import pandas as pd
import requests
import logging

# Set up logging to help debug
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================
# FastAPI app
# =============================
app = FastAPI(title="V Smart Investment Research Aggregator")

# =============================
# Serve React Build
# =============================
react_build_path = os.path.join(os.path.dirname(__file__), "..", "React", "my-app", "build")
app.mount("/static", StaticFiles(directory=os.path.join(react_build_path, "static")), name="static")

@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_file = os.path.join(react_build_path, "index.html")
    return FileResponse(index_file)

# =============================
# OpenRouter Setup
# =============================
OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Fix: Use correct model name format
MODEL_NAME = "deepseek/deepseek-r1"  # Simplified model name

# =============================
# Request / Response Models
# =============================
class ResearchRequest(BaseModel):
    company: str
    ticker: str

class ResearchBrief(BaseModel):
    consensus_view: str
    conflicting_opinions: list
    confidence_score: float
    key_risks: list

# =============================
# API Endpoint
# =============================
@app.post("/api/research", response_model=dict)
async def generate_research(request: ResearchRequest):
    """Fetch research data from CSV and synthesize with OpenRouter"""
    try:
        # Load CSV file (ensure it's in backend/data.csv)
        csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
        df = pd.read_csv(csv_path)
        
        # Filter company info
        company_data = df[
            (df["company"].str.lower() == request.company.lower()) |
            (df["ticker"].str.upper() == request.ticker.upper())
        ]
        
        if company_data.empty:
            raise HTTPException(status_code=404, detail="Company not found in dataset")
        
        # Collect research texts
        research_texts = company_data["research_text"].tolist()
        combined_text = "\n\n".join(research_texts)
        
        # Improved prompt with clearer JSON structure
        prompt = f"""You are an expert financial analyst. Analyze the following research for {request.company} ({request.ticker}) and return a JSON response with this exact structure:

{{
  "consensus_view": "string describing the overall consensus",
  "conflicting_opinions": ["list", "of", "conflicting", "viewpoints"],
  "confidence_score": 0.85,
  "key_risks": ["list", "of", "key", "risks"]
}}

Research data:
{combined_text[:3000]}

Return only valid JSON, no additional text."""

        # Fix: Proper headers and payload structure
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",  # Add referer for OpenRouter
            "X-Title": "V Smart Investment Research"  # Optional: helps with OpenRouter tracking
        }
        
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system", 
                    "content": "You are a financial analyst. Always respond with valid JSON only."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            "temperature": 0.3,  # Lower temperature for more consistent JSON output
            "max_tokens": 1000,   # Increased tokens
            "top_p": 1.0,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        
        # Log the request for debugging
        logger.info(f"Sending request to OpenRouter with model: {MODEL_NAME}")
        logger.info(f"Payload keys: {list(payload.keys())}")
        
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=30)
        
        # Better error handling
        if response.status_code != 200:
            logger.error(f"OpenRouter API error: {response.status_code}")
            logger.error(f"Response: {response.text}")
            
            if response.status_code == 400:
                error_detail = response.json().get('error', {}) if response.text else {}
                raise HTTPException(
                    status_code=400, 
                    detail=f"OpenRouter API error: {error_detail.get('message', response.text)}"
                )
            elif response.status_code == 401:
                raise HTTPException(status_code=401, detail="Invalid OpenRouter API key")
            elif response.status_code == 429:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
            else:
                response.raise_for_status()
        
        result = response.json()
        
        # Extract and parse model output
        if "choices" not in result or not result["choices"]:
            raise HTTPException(status_code=500, detail="No response from model")
            
        model_output = result["choices"][0]["message"]["content"].strip()
        logger.info(f"Raw model output: {model_output}")
        
        # Clean up the output in case there's extra text
        try:
            # Find JSON in the response
            start_idx = model_output.find('{')
            end_idx = model_output.rfind('}') + 1
            
            if start_idx == -1 or end_idx == 0:
                raise ValueError("No JSON found in response")
                
            json_str = model_output[start_idx:end_idx]
            brief_json = json.loads(json_str)
            
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(f"JSON parsing error: {e}")
            logger.error(f"Model output: {model_output}")
            
            # Fallback response
            brief_json = {
                "consensus_view": "Unable to parse model response",
                "conflicting_opinions": ["Analysis unavailable"],
                "confidence_score": 0.0,
                "key_risks": ["Data parsing error"]
            }
        
        return {
            "company": request.company, 
            "ticker": request.ticker, 
            "brief": brief_json
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
        raise HTTPException(status_code=503, detail=f"External API error: {str(e)}")
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Health check endpoint for testing
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}

# Test OpenRouter connection
@app.get("/api/test-openrouter")
async def test_openrouter():
    """Test endpoint to verify OpenRouter connection"""
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000"
        }
        
        payload = {
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": "Hello, please respond with: 'Connection successful'"}],
            "max_tokens": 50
        }
        
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            return {
                "status": "success", 
                "model": MODEL_NAME,
                "response": result.get("choices", [{}])[0].get("message", {}).get("content", "No content")
            }
        else:
            return {
                "status": "error",
                "status_code": response.status_code,
                "error": response.text
            }
            
    except Exception as e:
        return {"status": "error", "message": str(e)}
