from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from basedatos import get_db
from schemas.categorias import CategoriaCreate, CategoriaOut
import crud.categorias as crud

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=CategoriaOut)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@router.get("/{categoria_id}", response_model=CategoriaOut)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.get("/negocio/{negocio_id}", response_model=list[CategoriaOut])
def obtener_categorias_de_negocio(negocio_id: int, db: Session = Depends(get_db)):
    return crud.obtener_categorias_por_negocio(db, negocio_id)

@router.delete("/{categoria_id}", response_model=CategoriaOut)
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.eliminar_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.put("/{categoria_id}", response_model=CategoriaOut)
def actualizar_categoria(categoria_id: int, nombre: str, db: Session = Depends(get_db)):
    categoria = crud.actualizar_categoria(db, categoria_id, nombre)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria
