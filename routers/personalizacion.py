from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from basedatos import get_db
from crud.personalizacion import (
    get_personalizaciones, get_personalizacion, create_personalizacion,
    get_detalle_personalizaciones, get_detalle_personalizacion, create_detalle_personalizacion,
    get_productos_personalizados, get_producto_personalizado, create_producto_personalizado,
)
from schemas.personalizacion import (
    PersonalizacionOut, PersonalizacionCreate,
    DetallePersonalizacionOut, DetallePersonalizacionCreate,
    ProductoPersonalizadoOut, ProductoPersonalizadoCreate,
)

router = APIRouter(prefix="/personalizaciones", tags=["Personalizaciones"])

# Personalizaciones
@router.get("/", response_model=List[PersonalizacionOut])
def read_personalizaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_personalizaciones(db, skip=skip, limit=limit)

@router.get("/{personalizacion_id}", response_model=PersonalizacionOut)
def read_personalizacion(personalizacion_id: int, db: Session = Depends(get_db)):
    db_personalizacion = get_personalizacion(db, personalizacion_id)
    if not db_personalizacion:
        raise HTTPException(status_code=404, detail="Personalización no encontrada")
    return db_personalizacion

@router.post("/", response_model=PersonalizacionOut)
def create_new_personalizacion(personalizacion: PersonalizacionCreate, db: Session = Depends(get_db)):
    return create_personalizacion(db, personalizacion)

# DetallePersonalizacion
@router.get("/detalles/", response_model=List[DetallePersonalizacionOut])
def read_detalle_personalizaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_detalle_personalizaciones(db, skip=skip, limit=limit)

@router.get("/detalles/{detalle_id}", response_model=DetallePersonalizacionOut)
def read_detalle_personalizacion(detalle_id: int, db: Session = Depends(get_db)):
    db_detalle = get_detalle_personalizacion(db, detalle_id)
    if not db_detalle:
        raise HTTPException(status_code=404, detail="Detalle Personalización no encontrado")
    return db_detalle

@router.post("/detalles/", response_model=DetallePersonalizacionOut)
def create_new_detalle_personalizacion(detalle: DetallePersonalizacionCreate, db: Session = Depends(get_db)):
    return create_detalle_personalizacion(db, detalle)

# ProductoPersonalizado
@router.get("/productos_personalizados/", response_model=List[ProductoPersonalizadoOut])
def read_productos_personalizados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_productos_personalizados(db, skip=skip, limit=limit)

@router.get("/productos_personalizados/{producto_id}", response_model=ProductoPersonalizadoOut)
def read_producto_personalizado(producto_id: int, db: Session = Depends(get_db)):
    db_producto = get_producto_personalizado(db, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto Personalizado no encontrado")
    return db_producto

@router.post("/productos_personalizados/", response_model=ProductoPersonalizadoOut)
def create_new_producto_personalizado(producto: ProductoPersonalizadoCreate, db: Session = Depends(get_db)):
    return create_producto_personalizado(db, producto)
