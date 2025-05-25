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
    result = []
    for n in name:
        # Search for the student with the given name
        found = next((student for student in data["students"] if student["name"] == n), None)
        result.append(found)
    return {"marks": result}

@app.get("/api/debug")
def debug():
    return {"keys": list(data.keys())}
