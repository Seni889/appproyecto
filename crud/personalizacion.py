from sqlalchemy.orm import Session
from models.personalizacion import Personalizacion, DetallePersonalizacion, ProductoPersonalizado
from schemas.personalizacion import PersonalizacionCreate, DetallePersonalizacionCreate, ProductoPersonalizadoCreate

# CRUD Personalizacion
def get_personalizaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Personalizacion).offset(skip).limit(limit).all()

def get_personalizacion(db: Session, personalizacion_id: int):
    return db.query(Personalizacion).filter(Personalizacion.id == personalizacion_id).first()

def create_personalizacion(db: Session, personalizacion: PersonalizacionCreate):
    db_personalizacion = Personalizacion(**personalizacion.dict())
    db.add(db_personalizacion)
    db.commit()
    db.refresh(db_personalizacion)
    return db_personalizacion


# CRUD DetallePersonalizacion
def get_detalle_personalizaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DetallePersonalizacion).offset(skip).limit(limit).all()

def get_detalle_personalizacion(db: Session, detalle_id: int):
    return db.query(DetallePersonalizacion).filter(DetallePersonalizacion.id == detalle_id).first()

def create_detalle_personalizacion(db: Session, detalle: DetallePersonalizacionCreate):
    db_detalle = DetallePersonalizacion(**detalle.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle


# CRUD ProductoPersonalizado
def get_productos_personalizados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProductoPersonalizado).offset(skip).limit(limit).all()

def get_producto_personalizado(db: Session, producto_id: int):
    return db.query(ProductoPersonalizado).filter(ProductoPersonalizado.id == producto_id).first()

def create_producto_personalizado(db: Session, producto: ProductoPersonalizadoCreate):
    db_producto = ProductoPersonalizado(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
