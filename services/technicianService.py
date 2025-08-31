from sqlalchemy.orm import Session
from sqlmodel import select
from models.technician import Technician,TechnicianBase

def create_technician(session: Session,technician: TechnicianBase) -> Technician:
    db_technician = Technician.model_validate(technician)
    session.add(db_technician)
    session.commit()
    session.refresh(db_technician)
    return db_technician

def get_technician(session:Session) -> list[Technician]:
    result = session.exec(select(Technician))
    return result.all()

def get_technician_by_id(session: Session, technicianId: int) -> Technician | None:
    return session.get(Technician, technicianId)

def delete_technician(session: Session, technicianId: int) -> bool:
    technician = session.get(Technician, technicianId)
    if not technician:
        return False
    session.delete(technician)
    session.commit()
    return True

def update_technician(session: Session, technicianId: int, technician: TechnicianBase) -> Technician | None:
    technicianDB = session.get(Technician, technicianId)
    if not technicianDB:
        return None
    data = technician.model_dump(exclude_unset=True)
    technicianDB.sqlmodel_update(data)
    session.add(technicianDB)
    session.commit()
    session.refresh(technicianDB)
    return technicianDB