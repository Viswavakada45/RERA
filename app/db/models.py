from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    projectId = Column(String, primary_key=True, index=True)
    projectName = Column(String)
    authority = Column(String)
    sector = Column(String)
    status = Column(String)

    approvedDate = Column(String)
    proposedCompletion = Column(String)
    registrationNumber = Column(String)

    state = Column(String)
    district = Column(String)


class Promoter(Base):
    __tablename__ = "promoters"

    id = Column(Integer, primary_key=True, index=True)
    projectId = Column(String, ForeignKey("projects.projectId"))

    name = Column(String)
    type = Column(String)
    experience = Column(String)

    gstNumber = Column(String, nullable=True)
    pastCases = Column(String, nullable=True)
class LandDetails(Base):
    __tablename__ = "land_details"

    id = Column(Integer, primary_key=True, index=True)
    projectId = Column(String, ForeignKey("projects.projectId"))

    surveyNumbers = Column(String)
    plotNumber = Column(String, nullable=True)
    totalAreaSqmts = Column(String)
    netAreaSqmts = Column(String)


class BuildingDetails(Base):
    __tablename__ = "building_details"

    id = Column(Integer, primary_key=True, index=True)
    projectId = Column(String, ForeignKey("projects.projectId"))

    approvedBuiltUpAreaSqmts = Column(String)
    mortgageAreaSqmts = Column(String)
    totalBuildings = Column(Integer)
    overallUnits = Column(Integer)
    bookedUnits = Column(Integer)
    remainingUnits = Column(Integer)


class ContactDetails(Base):
    __tablename__ = "contact_details"

    id = Column(Integer, primary_key=True, index=True)
    projectId = Column(String, ForeignKey("projects.projectId"))

    officeNumber = Column(String, nullable=True)
    websiteUrl = Column(String, nullable=True)


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    projectId = Column(String, ForeignKey("projects.projectId"))

    houseNumber = Column(String, nullable=True)
    buildingName = Column(String)
    street = Column(String)
    locality = Column(String)
    mandal = Column(String)
    district = Column(String)
    state = Column(String)
    pincode = Column(String)