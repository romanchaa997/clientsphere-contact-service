"""Contact Service - Main Application"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ClientSphere Contact Service",
    description="Contact enrichment & Gmail integration service",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "contact-service"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "ClientSphere Contact Service", "version": "1.0.0"}

# Contact endpoints (placeholders)
@app.post("/contacts")
async def create_contact(email: str, name: str):
    return {"id": 1, "email": email, "name": name, "enriched": False}

@app.get("/contacts/{contact_id}")
async def get_contact(contact_id: int):
    return {"id": contact_id, "email": "test@example.com"}

@app.get("/contacts")
async def list_contacts(skip: int = 0, limit: int = 10):
    return {"total": 0, "contacts": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
