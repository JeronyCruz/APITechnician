from sqlalchemy.orm import Session
from sqlmodel import select
from models.technicianType import TechnicianType, TechnicianTypeBase

def CreateTechnicianType(session: Session, technicianType: TechnicianTypeBase) -> TechnicianType:
    db_technician = TechnicianType.model_validate(technicianType)
    session.add(db_technician)
    session.commit()
    session.refresh(db_technician)
    return db_technician

def GetTechnician(session:Session) -> list[TechnicianType]:
    result = session.exec(select(TechnicianType))
    return result.all()

def GetTechnicianById(session: Session, technicianTypeId: int) -> TechnicianType | None:
    return session.get(TechnicianType, technicianTypeId)

def DeleteTechnicianType(session: Session, technicianTypeId: int) -> bool:
    technicianType = session.get(TechnicianType, technicianTypeId)
    if not technicianType:
        return False
    session.delete(technicianType)
    session.commit()
    return True

def UpdateTechnicianType(session: Session, technicianTypeId: int, technicianType: TechnicianTypeBase) -> TechnicianType | None:
    technicianTypeDB = session.get(TechnicianType, technicianTypeId)
    if not technicianTypeDB:
        return None
    data = technicianType.model_dump(exclude_unset=True)
    technicianTypeDB.sqlmodel_update(data)
    session.add(technicianTypeDB)
    session.commit()
    session.refresh(technicianTypeDB)
    return technicianTypeDB