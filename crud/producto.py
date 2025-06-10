from sqlalchemy.orm import Session
from models.productos import Producto
from schemas.producto import ProductoCreate

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        disponible=producto.disponible,
        id_categoria=producto.id_categoria,
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

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
