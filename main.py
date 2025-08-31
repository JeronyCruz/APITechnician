from typing import Annotated, List
from fastapi import FastAPI, Query, HTTPException
from sqlalchemy import select
from Connection import SessionDep, create_db_and_tables
from models.technician import Technician, TechnicianResponse, TechnicianBase
from services.technicianService import (
    create_technician,
    get_technician,
    get_technician_by_id,
    delete_technician,
    update_technician,
)



app = FastAPI(
    title= "API de Tecnicos",
    version= "1.0.0"
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