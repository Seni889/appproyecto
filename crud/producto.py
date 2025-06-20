from sqlalchemy.orm import Session, joinedload
from models.productos import Producto
from schemas.producto import ProductoCreate
from fastapi import HTTPException
from models.negocio import Categoria, Negocio

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def create_producto(db: Session, producto_data: ProductoCreate, current_user_id: int):
    # Buscar el negocio del usuario actual
    negocio = db.query(Negocio).filter(Negocio.id_usuario == current_user_id).first()
    if not negocio:
        raise HTTPException(status_code=404, detail="No tienes un negocio registrado.")

    # Obtener automáticamente los IDs
    id_categoria = negocio.id_categoria
    id_negocio = negocio.id

    # Crear producto con los campos necesarios
    nuevo_producto = Producto(
        nombre=producto_data.nombre,
        descripcion=producto_data.descripcion,
        precio=producto_data.precio,
        id_categoria=id_categoria,
        id_negocio=id_negocio
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def update_producto(db: Session, producto_id: int, producto: ProductoCreate):
    db_producto = get_producto(db, producto_id)
    if db_producto is None:
        return None
    db_producto.nombre = producto.nombre
    db_producto.descripcion = producto.descripcion
    db_producto.precio = producto.precio
    db_producto.disponible = producto.disponible
    db_producto.id_categoria = producto.id_categoria
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id)
    if db_producto is None:
        return None
    db.delete(db_producto)
    db.commit()
    return db_producto
