# routes/negocio.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from basedatos import get_db
from crud.negocio import get_negocio, get_negocios, create_negocio, update_negocio, delete_negocio
from schemas.negocio import NegocioOut, NegocioCreate

router = APIRouter(prefix="/negocios", tags=["Negocios"])

@router.get("/", response_model=List[NegocioOut])
def listar_negocios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    negocios = get_negocios(db, skip=skip, limit=limit)
    return negocios

@router.get("/{negocio_id}", response_model=NegocioOut)
def obtener_negocio(negocio_id: int, db: Session = Depends(get_db)):
    negocio = get_negocio(db, negocio_id)
    if not negocio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Negocio no encontrado")
    return negocio

@router.post("/", response_model=NegocioOut, status_code=status.HTTP_201_CREATED)
def crear_negocio(negocio: NegocioCreate, db: Session = Depends(get_db)):
    return create_negocio(db, negocio)

@router.put("/{negocio_id}", response_model=NegocioOut)
def actualizar_negocio(negocio_id: int, negocio_data: NegocioCreate, db: Session = Depends(get_db)):
    negocio = update_negocio(db, negocio_id, negocio_data)
    if not negocio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Negocio no encontrado")
    return negocio

@router.delete("/{negocio_id}", response_model=NegocioOut)
def eliminar_negocio(negocio_id: int, db: Session = Depends(get_db)):
    negocio = delete_negocio(db, negocio_id)
    if not negocio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Negocio no encontrado")
    return negocio

