import json
from pathlib import Path
from app.db.database import SessionLocal
from app.db.models import (
    LandDetails,
    BuildingDetails,
    ContactDetails,
    Address
)

DATA_PATH = Path("app/data/telangana.json")

db = SessionLocal()

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

for state, districts in data.items():
    for district, projects in districts.items():
        for item in projects:
            p = item["project"]

            # --- Land Details ---
            land = item.get("landDetails")
            if land:
                db.add(
                    LandDetails(
                        projectId=p["projectId"],
                        surveyNumbers=land["surveyNumbers"],
                        plotNumber=land["plotNumber"],
                        totalAreaSqmts=land["totalAreaSqmts"],
                        netAreaSqmts=land["netAreaSqmts"]
                    )
                )

            # --- Building Details ---
            building = item.get("buildingDetails")
            if building:
                db.add(
                    BuildingDetails(
                        projectId=p["projectId"],
                        approvedBuiltUpAreaSqmts=building["approvedBuiltUpAreaSqmts"],
                        mortgageAreaSqmts=building["mortgageAreaSqmts"],
                        totalBuildings=building["totalBuildings"],
                        overallUnits=building["overallUnits"],
                        bookedUnits=building["bookedUnits"],
                        remainingUnits=building["remainingUnits"]
                    )
                )

            # --- Contact Details ---
            contact = item.get("contactDetails")
            if contact:
                db.add(
                    ContactDetails(
                        projectId=p["projectId"],
                        officeNumber=contact["officeNumber"],
                        websiteUrl=contact["websiteUrl"]
                    )
                )

            # --- Address ---
            addr = item.get("address")
            if addr:
                db.add(
                    Address(
                        projectId=p["projectId"],
                        houseNumber=addr["houseNumber"],
                        buildingName=addr["buildingName"],
                        street=addr["street"],
                        locality=addr["locality"],
                        mandal=addr["mandal"],
                        district=addr["district"],
                        state=addr["state"],
                        pincode=addr["pincode"]
                    )
                )

db.commit()
db.close()

print("✅ Remaining Agent JSON tables loaded successfully")
