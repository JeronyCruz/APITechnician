from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.schemas.technicianType import TechnicianTypeCreate, TechnicianTypeUpdate, TechnicianTypeResponse
from useCases import technicianTypeService
from dependencies import get_session

router = APIRouter(
    prefix="/techniciansTypes",
    tags=["Technicians Types"])

@router.post("/", response_model=TechnicianTypeResponse)
def createTechnicianType(technicianType: TechnicianTypeCreate, session: Session = Depends(get_session)):
    return technicianTypeService.createTechnicianType(session,technicianType)

@router.get("/", response_model=list[TechnicianTypeResponse])
def getTechniciansTypes(session: Session = Depends(get_session)):
    return technicianTypeService.getAllTechnicianType(session)

@router.get("/{technicianTypeId}", response_model=TechnicianTypeResponse)
def getTechnician(technicianTypeId: int, session: Session = Depends(get_session)):
    technicianType = technicianTypeService.getTechnicianTypeById(session, technicianTypeId)
    if not technicianType:
        raise HTTPException(status_code=404, detail="Technician Type not found")
    return technicianType

@router.delete("/{technicianTypeId}")
def deleteTechnician(technicianTypeId: int, session: Session = Depends(get_session)):
    if not technicianTypeService.deleteTechnicianType(session, technicianTypeId):
        raise HTTPException(status_code=404, detail="Technician Type not found")
    return {"message": "Technician deleted successfully"}

@router.patch("/{technicianTypeid}", response_model=TechnicianTypeResponse)
def updateTechnician(technicianTypeId: int, technicianTypeData: TechnicianTypeUpdate, session: Session = Depends(get_session)):
    technicianType = technicianTypeService.updateTechnicianType(session, technicianTypeId, technicianTypeData)
    if not technicianType:
        raise HTTPException(status_code=404, detail="Technician not found")
    return technicianType