from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine
from app.api.auth.routes import router as auth_router


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Falaa API running"}

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"database": "connected"}

app.include_router(auth_router)