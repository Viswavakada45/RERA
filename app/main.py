from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base

from app.routers.rera import router as rera_router
from app.routers.geo import router as geo_router

app = FastAPI(title="RERA Backend")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "RERA Backend Running"}

# ✅ REGISTER ROUTERS
app.include_router(rera_router, prefix="/api/rera", tags=["RERA"])
app.include_router(geo_router, prefix="/api/geo", tags=["Geo"])
