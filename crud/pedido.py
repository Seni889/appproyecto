from sqlalchemy.orm import Session, joinedload
from models.pedidos import Pedido, DetallePedido
from schemas.pedidos import PedidoCreate, DetallePedidoCreate

# CRUD para Pedidos
def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pedido).options(joinedload(Pedido.detalles)).offset(skip).limit(limit).all()

def get_pedido(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def create_pedido(db: Session, pedido: PedidoCreate):
    db_pedido = Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# CRUD para DetallePedido
def get_detalles_pedido(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DetallePedido).offset(skip).limit(limit).all()

def get_detalle_pedido(db: Session, detalle_id: int):
    return db.query(DetallePedido).filter(DetallePedido.id == detalle_id).first()

def create_detalle_pedido(db: Session, detalle: DetallePedidoCreate):
    db_detalle = DetallePedido(**detalle.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

#Creacion de pedido con detalle

