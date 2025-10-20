from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.technician import Technician

def create(db: Session, technician: Technician) -> Technician:
    db.add(technician)
    db.commit()
    db.refresh(technician)
    return technician

def getAll(session: Session) -> list[Technician]:
    return session.exec(select(Technician)).all()

def getById(session: Session, technicianId: int) -> Technician | None:
    return session.get(Technician, technicianId)

def delete(session: Session, technicianId: int) -> bool:
    technician = session.get(Technician, technicianId)
    if not technician:
        return False
    session.delete(technician)
    session.commit()
    return True

def update(session: Session, technician: Technician) -> Technician:
    session.add(technician)
    session.commit()
    session.refresh(technician)
    return technician