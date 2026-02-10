from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base

app = FastAPI(title="RERA Backend")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "RERA Backend Running"}
