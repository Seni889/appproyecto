from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from basedatos import get_db
from schemas.categorias import CategoriaCreate, CategoriaOut
from crud.categorias import (crear_categoria_db, obtener_categorias_db, obtener_categorias_por_negocio_db,
                            obtener_categoria_db, eliminar_categoria_db, actualizar_categoria_db
                             )
from autenti import get_current_admin, get_current_user 
from models.usuarios import Usuario

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=CategoriaOut)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db), current_admin : Usuario= Depends(get_current_admin)):
    return crear_categoria_db(db, categoria)

@router.get("/todas", response_model=list[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return obtener_categorias_db(db)


@router.get("/{categoria_id}", response_model=CategoriaOut)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = obtener_categoria_db(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.get("/negocio/{negocio_id}", response_model=list[CategoriaOut])
def obtener_categorias_de_negocio(negocio_id: int, db: Session = Depends(get_db)):
    return obtener_categorias_por_negocio_db(db, negocio_id)

@router.delete("/{categoria_id}", response_model=CategoriaOut)
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = eliminar_categoria_db(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.put("/{categoria_id}", response_model=CategoriaOut)
def actualizar_categoria(categoria_id: int, nombre: str, db: Session = Depends(get_db)):
    categoria = actualizar_categoria_db(db, categoria_id, nombre)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria
