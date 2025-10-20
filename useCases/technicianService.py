from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.technician import Technician
from domain.schemas.technician import TechnicianCreate, TechnicianUpdate
from infrastructure.repositories.technicianRepository import (
    create,
    getAll,
    getById,
    delete,
    update
)

def createTechnician(session: Session,technicianData: TechnicianCreate) -> Technician:
    technician = Technician (**technicianData.model_dump())
    return create(session, technician)

def getAllTechnician(session:Session) -> list[Technician]:
    return getAll(session)

def getTechnicianById(session: Session, technicianId: int) -> Technician | None:
    return getById(session, technicianId)

def deleteTechnician(session: Session, technicianId: int) -> bool:
    return delete(session, technicianId)

def updateTechnician(session: Session, technicianId: int, technicianData: TechnicianUpdate) -> Technician | None:
    technician = getById(session, technicianId)
    if not technician:
        return None
    for key, value in technicianData.model_dump(exclude_unset=True).items():
        setattr(technician, key, value)
    return update(session, technician)