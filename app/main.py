from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Falaa API running"}

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"database": "connected"}