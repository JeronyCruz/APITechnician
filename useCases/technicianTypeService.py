from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.technicianType import TechnicianType
from domain.schemas.technicianType import TechnicianTypeCreate, TechnicianTypeUpdate
from infrastructure.repositories.technicianTypeRepository import (
    create,
    getAll,
    getById,
    delete,
    update
)

def createTechnicianType(session: Session,technicianTypeData: TechnicianTypeCreate) -> TechnicianType:
    technician = TechnicianType (**technicianTypeData.model_dump())
    return create(session, technician)

def getAllTechnicianType(session:Session) -> list[TechnicianType]:
    return getAll(session)

def getTechnicianTypeById(session: Session, technicianTypeId: int) -> TechnicianType | None:
    return getById(session, technicianTypeId)

def deleteTechnicianType(session: Session, technicianTypeId: int) -> bool:
    return delete(session, technicianTypeId)

def updateTechnicianType(session: Session, technicianTypeId: int, technicianTypeData: TechnicianTypeUpdate) -> TechnicianType | None:
    technicianType = getById(session, technicianTypeId)
    if not technicianType:
        return None
    for key, value in technicianTypeData.model_dump(exclude_unset=True).items():
        setattr(technicianType, key, value)
    return update(session, technicianType)