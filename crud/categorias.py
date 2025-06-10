from sqlalchemy.orm import Session
from models.negocio import Categoria
from schemas.categorias import CategoriaCreate

def crear_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def obtener_categorias_por_negocio(db: Session, negocio_id: int):
    return db.query(Categoria).filter(Categoria.id == negocio_id).all()

def eliminar_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
    return categoria

def actualizar_categoria(db: Session, categoria_id: int, nombre: str):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria:
        categoria.nombre = nombre
        db.commit()
        db.refresh(categoria)
    return categoria
