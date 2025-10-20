from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.technicianType import TechnicianType

def create(db: Session, technicianType: TechnicianType) -> TechnicianType:
    db.add(technicianType)
    db.commit()
    db.refresh(technicianType)
    return technicianType

def getAll(session: Session) -> list[TechnicianType]:
    return session.exec(select(TechnicianType)).all()

def getById(session: Session, technicianId: int) -> TechnicianType | None:
    return session.get(TechnicianType, technicianId)

def delete(session: Session, technicianId: int) -> bool:
    technicianType = session.get(TechnicianType, technicianId)
    if not technicianType:
        return False
    session.delete(technicianType)
    session.commit()
    return True

def update(session: Session, technicianType: TechnicianType) -> TechnicianType:
    session.add(technicianType)
    session.commit()
    session.refresh(technicianType)
    return technicianType