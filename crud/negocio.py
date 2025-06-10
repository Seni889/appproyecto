# crud/negocio.py
from sqlalchemy.orm import Session
from models.negocio import Negocio
from schemas.negocio import NegocioCreate

def get_negocio(db: Session, negocio_id: int):
    return db.query(Negocio).filter(Negocio.id == negocio_id).first()

def get_negocios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Negocio).offset(skip).limit(limit).all()

def create_negocio(db: Session, negocio: NegocioCreate):
    db_negocio = Negocio(**negocio.dict())
    db.add(db_negocio)
    db.commit()
    db.refresh(db_negocio)
    return db_negocio

def update_negocio(db: Session, negocio_id: int, negocio_data: NegocioCreate):
    db_negocio = get_negocio(db, negocio_id)
    if not db_negocio:
        return None
    for key, value in negocio_data.dict(exclude_unset=True).items():
        setattr(db_negocio, key, value)
    db.commit()
    db.refresh(db_negocio)
    return db_negocio

def delete_negocio(db: Session, negocio_id: int):
    db_negocio = get_negocio(db, negocio_id)
    if not db_negocio:
        return None
    db.delete(db_negocio)
    db.commit()
    return db_negocio
