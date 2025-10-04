from typing import Annotated, List
from fastapi import FastAPI, Query, HTTPException
from sqlalchemy import select
from Connection import SessionDep, create_db_and_tables
from models.technician import Technician, TechnicianResponse, TechnicianBase
from models.technicianType import TechnicianType, TechnicianTypeBase
from fastapi.middleware.cors import CORSMiddleware
from services.technicianService import (
    create_technician,
    get_technician,
    get_technician_by_id,
    delete_technician,
    update_technician,
)
from services.technicianTypeService import (
    CreateTechnicianType,
    GetTechnician,
    GetTechnicianById,
    DeleteTechnicianType,
    UpdateTechnicianType,
)



app = FastAPI(
    title= "API de Tecnicos",
    version= "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# @app.get('/')
# def root():
#     return "Hello World"

@app.post("/technician/",response_model=Technician , tags=["Technician"])
def createHero(technician: TechnicianBase, session: SessionDep):
    return create_technician(session, technician)

@app.get("/technician/", response_model=List[Technician], tags=["Technician"])
def getTechnician(session: SessionDep):
    return get_technician(session)

@app.get("/technician/{technicianId}",response_model=Technician, tags=["Technician"])
def getTechnicianId(technicianId: int, session: SessionDep):
    technician = get_technician_by_id(session, technicianId)
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    return technician

@app.delete("/technician/{technicianId}", tags=["Technician"])
def deleteTechnician(technicianId: int, session: SessionDep):
    technician = delete_technician(session, technicianId)
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    return {"OK" : True}

@app.patch("/technician/{technicianId}",response_model=Technician, tags=["Technician"])
def editTechnician(technicianId: int, technician:TechnicianBase, session: SessionDep) :
    technicianUpdate = update_technician(session, technicianId, technician)
    if not technicianUpdate:
        raise HTTPException(status_code=404, detail="Technician not found")
    return technicianUpdate



@app.post("/technicianType/",response_model=TechnicianType , tags=["TechnicianType"])
def createTechnicianType(technicianType: TechnicianTypeBase, session: SessionDep):
    return CreateTechnicianType(session, technicianType)

@app.get("/technicianType/", response_model=List[TechnicianType], tags=["TechnicianType"])
def getTechnicianType(session: SessionDep):
    return GetTechnician(session)

@app.get("/technicianType/{technicianTypeId}",response_model=TechnicianType, tags=["TechnicianType"])
def getTechnicianTypeId(technicianTypeId: int, session: SessionDep):
    technicianType = GetTechnicianById(session, technicianTypeId)
    if not technicianType:
        raise HTTPException(status_code=404, detail="Technician Type not found")
    return technicianType

@app.delete("/technicianType/{technicianTypeId}", tags=["TechnicianType"])
def deleteTechnicianType(technicianTypeId: int, session: SessionDep):
    technicianType = DeleteTechnicianType(session, technicianTypeId)
    if not technicianType:
        raise HTTPException(status_code=404, detail="Technician Type not found")
    return {"OK" : True}

@app.patch("/technicianType/{technicianTypeId}",response_model=TechnicianType, tags=["TechnicianType"])
def editTechnicianType(technicianTypeId: int, technicianType:TechnicianTypeBase, session: SessionDep) :
    technicianTypeUpdate = UpdateTechnicianType(session, technicianTypeId, technicianType)
    if not technicianTypeUpdate:
        raise HTTPException(status_code=404, detail="Technician Type not found")
    return technicianTypeUpdate