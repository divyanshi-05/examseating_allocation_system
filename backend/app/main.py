from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.database import engine

app = FastAPI(
    title="Exam Seating Allocation System",
    description="Backend API for examination management",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Backend is running successfully"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/db-health")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "database": "connected"
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )