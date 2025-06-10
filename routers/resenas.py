from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from crud import resenas as crud_resenas
from basedatos import SessionLocal
from schemas.resenas import ResenaCreate, ResenaOut
from crud.resenas import get_resena, get_resenas, create_resena, delete_resena, update_resena

router = APIRouter(
    prefix="/resenas",
    tags=["Resenas"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/resenas/usuario/{id_usuario}", response_model=List[ResenaOut])
def leer_resenas_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return crud_resenas.get_resenas_by_usuario(db, id_usuario)

@router.get("/resenas/negocio/{id_negocio}", response_model=List[ResenaOut])
def leer_resenas_por_negocio(id_negocio: int, db: Session = Depends(get_db)):
    return crud_resenas.get_resenas_by_negocio(db, id_negocio)


@router.get("/", response_model=List[ResenaOut])
def read_resenas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_resenas(db, skip=skip, limit=limit)

@router.get("/{resena_id}", response_model=ResenaOut)
def read_resena(resena_id: int, db: Session = Depends(get_db)):
    db_resena = get_resena(db, resena_id)
    if not db_resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
    return db_resena

@router.post("/", response_model=ResenaOut, status_code=status.HTTP_201_CREATED)
def create_new_resena(resena: ResenaCreate, db: Session = Depends(get_db)):
    return create_resena(db, resena)

@router.put("/{resena_id}", response_model=ResenaOut)
def update_existing_resena(resena_id: int, resena: ResenaCreate, db: Session = Depends(get_db)):
    db_resena = update_resena(db, resena_id, resena)
    if not db_resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
    return db_resena

@router.delete("/{resena_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_resena(resena_id: int, db: Session = Depends(get_db)):
    db_resena = delete_resena(db, resena_id)
    if not db_resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
    return None
