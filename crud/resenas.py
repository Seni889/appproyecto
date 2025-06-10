from sqlalchemy.orm import Session
from models.resenas import Resenas
from schemas.resenas import ResenaCreate
from datetime import datetime

def get_resena(db: Session, resena_id: int):
    return db.query(Resenas).filter(Resenas.id == resena_id).first()

def get_resenas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Resenas).offset(skip).limit(limit).all()

def create_resena(db: Session, resena: ResenaCreate):
    db_resena = Resenas(
        calificacion=resena.calificacion,
        comentario=resena.comentario,
        id_usuario=resena.id_usuario,
        id_negocio=resena.id_negocio,
        fecha=datetime.now()
    )
    db.add(db_resena)
    db.commit()
    db.refresh(db_resena)
    return db_resena

def delete_resena(db: Session, resena_id: int):
    resena = get_resena(db, resena_id)
    if resena:
        db.delete(resena)
        db.commit()
    return resena

def update_resena(db: Session, resena_id: int, resena_update: ResenaCreate):
    resena = get_resena(db, resena_id)
    if resena:
        resena.calificacion = resena_update.calificacion
        resena.comentario = resena_update.comentario
        resena.id_usuario = resena_update.id_usuario
        resena.id_negocio = resena_update.id_negocio
        db.commit()
        db.refresh(resena)
    return resena

def get_resenas_by_usuario(db: Session, id_usuario: int, skip: int = 0, limit: int = 100):
    return db.query(Resenas).filter(Resenas.id_usuario == id_usuario).offset(skip).limit(limit).all()

def get_resenas_by_negocio(db: Session, id_negocio: int, skip: int = 0, limit: int = 100):
    return db.query(Resenas).filter(Resenas.id_negocio == id_negocio).offset(skip).limit(limit).all()
