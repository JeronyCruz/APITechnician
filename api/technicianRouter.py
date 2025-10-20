from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.schemas.technician import TechnicianCreate, TechnicianUpdate, TechnicianResponse
from useCases import technicianService
from dependencies import get_session

router = APIRouter(
    prefix="/technicians",
    tags=["Technicians"])

@router.post("/", response_model=TechnicianResponse)
def createTechnician(technician: TechnicianCreate, session: Session = Depends(get_session)):
    return technicianService.createTechnician(session,technician)

@router.get("/", response_model=list[TechnicianResponse])
def getTechnicians(session: Session = Depends(get_session)):
    return technicianService.getAllTechnician(session)

@router.get("/{technicianId}", response_model=TechnicianResponse)
def getTechnician(technicianId: int, session: Session = Depends(get_session)):
    technician = technicianService.getTechnicianById(session, technicianId)
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    return technician

@router.delete("/{technicianId}")
def deleteTechnician(technicianId: int, session: Session = Depends(get_session)):
    if not technicianService.deleteTechnician(session, technicianId):
        raise HTTPException(status_code=404, detail="Technician not found")
    return {"message": "Technician deleted successfully"}

@router.patch("/{technician_id}", response_model=TechnicianResponse)
def updateTechnician(technician_id: int, technicianData: TechnicianUpdate, session: Session = Depends(get_session)):
    technician = technicianService.updateTechnician(session, technician_id, technicianData)
    if not technician:
        raise HTTPException(status_code=404, detail="Technician not found")
    return technician