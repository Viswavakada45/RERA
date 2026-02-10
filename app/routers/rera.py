from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.db.models import (
    Project,
    Promoter,
    LandDetails,
    BuildingDetails,
    ContactDetails,
    Address
)

router = APIRouter()

@router.get("/projects")
def get_projects(state: str, district: str, db: Session = Depends(get_db)):

    projects = (
        db.query(Project)
        .filter(Project.state == state, Project.district == district)
        .all()
    )

    agent_projects = []

    for p in projects:
        promoter = db.query(Promoter).filter_by(projectId=p.projectId).first()
        land = db.query(LandDetails).filter_by(projectId=p.projectId).first()
        building = db.query(BuildingDetails).filter_by(projectId=p.projectId).first()
        contact = db.query(ContactDetails).filter_by(projectId=p.projectId).first()
        address = db.query(Address).filter_by(projectId=p.projectId).first()

        agent_projects.append({
            "project": {
                "projectId": p.projectId,
                "projectName": p.projectName,
                "authority": p.authority,
                "sector": p.sector,
                "status": p.status,
                "importantDates": {
                    "approvedDate": p.approvedDate,
                    "proposedCompletion": p.proposedCompletion
                },
                "registration": {
                    "registrationNumber": p.registrationNumber
                }
            },
            "promoter": {
                "name": promoter.name if promoter else None,
                "type": promoter.type if promoter else None,
                "experience": promoter.experience if promoter else None,
                "gstNumber": promoter.gstNumber if promoter else None,
                "pastCases": promoter.pastCases if promoter else None
            },
            "landDetails": {
                "surveyNumbers": land.surveyNumbers,
                "plotNumber": land.plotNumber,
                "totalAreaSqmts": land.totalAreaSqmts,
                "netAreaSqmts": land.netAreaSqmts
            } if land else None,
            "buildingDetails": {
                "approvedBuiltUpAreaSqmts": building.approvedBuiltUpAreaSqmts,
                "mortgageAreaSqmts": building.mortgageAreaSqmts,
                "totalBuildings": building.totalBuildings,
                "overallUnits": building.overallUnits,
                "bookedUnits": building.bookedUnits,
                "remainingUnits": building.remainingUnits
            } if building else None,
            "contactDetails": {
                "officeNumber": contact.officeNumber,
                "websiteUrl": contact.websiteUrl
            } if contact else None,
            "address": {
                "houseNumber": address.houseNumber,
                "buildingName": address.buildingName,
                "street": address.street,
                "locality": address.locality,
                "mandal": address.mandal,
                "district": address.district,
                "state": address.state,
                "pincode": address.pincode
            } if address else None,
            "towers": [],
            "meta": {
                "source": "TG-RERA",
                "lastUpdated": ""
            }
        })

    return {
        state: {
            district: agent_projects
        }
    }
