import json
from fastapi import APIRouter, HTTPException
from pathlib import Path

router = APIRouter()

BASE_PATH = Path("app/geo")

def normalize(name: str) -> str:
    return name.lower().replace(" ", "_")

# ---------------- INDIA ----------------

@router.get("/india")
def get_india_geo():
    path = BASE_PATH / "india" / "india.geojson"
    if not path.exists():
        raise HTTPException(status_code=404, detail="India GeoJSON not found")

    with open(path, encoding="utf-8") as f:
        return json.load(f)

# ---------------- STATE ----------------

@router.get("/state")
def get_state_geo(state: str):
    filename = f"{state.replace(' ', '_')}.geojson"
    path = BASE_PATH / "states" / filename

    if not path.exists():
        raise HTTPException(status_code=404, detail="State GeoJSON not found")

    with open(path, encoding="utf-8") as f:
        return json.load(f)

# ---------------- DISTRICT ----------------

@router.get("/district")
def get_district_geo(state: str, district: str):
    filename = f"{state.replace(' ', '_')}.geojson"
    path = BASE_PATH / "states" / filename

    if not path.exists():
        raise HTTPException(status_code=404, detail="State GeoJSON not found")

    geo = json.load(open(path, encoding="utf-8"))
    district_norm = normalize(district)

    filtered = [
        feature
        for feature in geo["features"]
        if normalize(feature["properties"].get("district", "")) == district_norm
    ]

    if not filtered:
        raise HTTPException(status_code=404, detail="District not found")

    return {
        "type": "FeatureCollection",
        "features": filtered
    }
