from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data once
with open("q-vercel-python.json") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [data.get(n, None) for n in name]}

@app.get("/api/debug")
def debug():
    return {"keys": list(data.keys())}
