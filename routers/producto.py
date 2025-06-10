from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from basedatos import get_db
from schemas.producto import ProductoCreate, ProductoOut
from crud.producto import get_producto, get_productos, create_producto, update_producto, delete_producto

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=List[ProductoOut])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = get_productos(db, skip=skip, limit=limit)
    return productos

@router.get("/{producto_id}", response_model=ProductoOut)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = get_producto(db, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoOut)
def create_new_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return create_producto(db, producto)

@router.put("/{producto_id}", response_model=ProductoOut)
def update_existing_producto(producto_id: int, producto: ProductoCreate, db: Session = Depends(get_db)):
    updated_producto = update_producto(db, producto_id, producto)
    if updated_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_producto

@router.delete("/{producto_id}", response_model=ProductoOut)
def delete_existing_producto(producto_id: int, db: Session = Depends(get_db)):
    deleted_producto = delete_producto(db, producto_id)
    if deleted_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return deleted_producto
