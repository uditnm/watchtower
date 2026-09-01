from fastapi import FastAPI
from database import SessionLocal
from sqlalchemy import text

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}


with SessionLocal() as session:
    result = session.execute(text("SELECT 1"))
    print(result.first())