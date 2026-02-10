from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base
from app.routers import rera
from app.routers import rera, geo
app = FastAPI(title="RERA Backend API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "RERA backend + tables ready"}
app.include_router(rera.router, prefix="/api/rera")
app.include_router(geo.router, prefix="/api/geo")
app = FastAPI()

@app.get("/")
def root():
    return {"status": "RERA backend running"}