from sqlalchemy.orm import Session, joinedload
from models.pedidos import Pedido, DetallePedido
from schemas.pedidos import PedidoCreate, DetallePedidoCreate
from models.productos import Producto
from fastapi import HTTPException
# CRUD para Pedidos
def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pedido).options(joinedload(Pedido.detalles)).offset(skip).limit(limit).all()

def get_pedido(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def create_pedido(db: Session, pedido: PedidoCreate, id_usuario: int, id_negocio: int):
    if not pedido.detalles:
        raise HTTPException(status_code=400, detail="Debe seleccionar al menos un producto.")

    total = 0.0

    # Validar productos antes de crear el pedido
    for detalle in pedido.detalles:
        producto = db.query(Producto).filter(Producto.id == detalle.producto_id).first()
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto con ID {detalle.producto_id} no encontrado.")
        
        # Verificar que el producto pertenezca al negocio correcto
        if producto.id_negocio != id_negocio:
            raise HTTPException(status_code=400, detail=f"El producto {producto.nombre} no pertenece al negocio seleccionado.")

        total += producto.precio * detalle.cantidad

    # Crear pedido
    db_pedido = Pedido(
        id_usuario=id_usuario,
        id_negocio=id_negocio,
        total=0.0,  # Se actualizará después
        notas=pedido.notas
    )
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)

    # Crear detalles de pedido
    for detalle in pedido.detalles:
        producto = db.query(Producto).filter(Producto.id == detalle.producto_id).first()
        db_detalle = DetallePedido(
            pedido_id=db_pedido.id,
            producto_id=detalle.producto_id,
            cantidad=detalle.cantidad,
            precio=producto.precio
        )
        db.add(db_detalle)

    db_pedido.total = total
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



def update_pedido(db: Session, pedido_id: int, pedido_data: PedidoCreate):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        return None

    for key, value in pedido_data.dict(exclude_unset=True).items():
        setattr(pedido, key, value)

    db.commit()
    db.refresh(pedido)
    return pedido

def delete_pedido(db: Session, pedido_id: int):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        return None

    db.delete(pedido)
    db.commit()
    return pedido

def update_detalle_pedido(db: Session, detalle_id: int, detalle_data: DetallePedidoCreate):
    detalle = db.query(DetallePedido).filter(DetallePedido.id == detalle_id).first()
    if not detalle:
        return None

    for key, value in detalle_data.dict(exclude_unset=True).items():
        setattr(detalle, key, value)

    db.commit()
    db.refresh(detalle)
    return detalle

def delete_detalle_pedido(db: Session, detalle_id: int):
    detalle = db.query(DetallePedido).filter(DetallePedido.id == detalle_id).first()
    if not detalle:
        return None

    db.delete(detalle)
    db.commit()
    return detalle
