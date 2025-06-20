from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from autenti import get_current_user, get_current_admin
from models.usuarios import Usuario
from basedatos import get_db
from crud.pedido import (
    get_pedidos, get_pedido, create_pedido,
    get_detalles_pedido, get_detalle_pedido, create_detalle_pedido, update_pedido
)
from schemas.pedidos import (
    PedidoOut, PedidoCreate,
    DetallePedidoOut, DetallePedidoCreate, PedidoEstadoUpdate
)

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

# Pedidos
@router.get("/", response_model=List[PedidoOut])
def read_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pedidos(db, skip=skip, limit=limit)

@router.get("/{pedido_id}", response_model=PedidoOut)
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = get_pedido(db, pedido_id)
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return db_pedido

@router.post("/negocios/{id_negocio}", response_model=PedidoOut)
def create_new_pedido(id_negocio: int, pedido: PedidoCreate, db: Session = Depends(get_db), current_user : Usuario= Depends(get_current_user)):
     return create_pedido(db, pedido, current_user.id, id_negocio)

# Detalles de Pedido
@router.get("/detalles/", response_model=List[DetallePedidoOut])
def read_detalles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_detalles_pedido(db, skip=skip, limit=limit)

@router.get("/detalles/{detalle_id}", response_model=DetallePedidoOut)
def read_detalle(detalle_id: int, db: Session = Depends(get_db)):
    db_detalle = get_detalle_pedido(db, detalle_id)
    if not db_detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return db_detalle

@router.post("/detalles/", response_model=DetallePedidoOut)
def create_new_detalle(detalle: DetallePedidoCreate, db: Session = Depends(get_db)):
     return create_detalle_pedido(db, detalle)

@router.patch("/{pedido_id}/estado", response_model=PedidoOut)
def cambiar_estado_pedido(
    pedido_id: int = Path(..., description="ID del pedido"),
    payload: PedidoEstadoUpdate = Depends(),
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    pedido = update_pedido(db, pedido_id, payload.estado)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

# @router.post("/", response_model=PedidoOut)
# def create_pedido_con_detalles(pedido: PedidoCreate, db: Session = Depends(get_db)):
#     # 1. Crear el pedido
#     nuevo_pedido = Pedido(
#         usuario_id=pedido.usuario_id,
#         restaurante_id=pedido.restaurante_id,
#         # Otros campos necesarios del pedido
#     )
#     db.add(nuevo_pedido)
#     db.commit()
#     db.refresh(nuevo_pedido)  # Obtener el ID generado del pedido

#     # 2. Crear los detalles del pedido con el ID del pedido recién creado
#     for detalle in pedido.detalles:
#         nuevo_detalle = DetallePedido(
#             pedido_id=nuevo_pedido.id,
#             producto_id=detalle.producto_id,
#             cantidad=detalle.cantidad,
#             personalizacion_id=detalle.personalizacion_id,
#         )
#         db.add(nuevo_detalle)

#     db.commit()

#     # 3. Opcional: cargar el pedido con detalles para devolver
#     db.refresh(nuevo_pedido)
#     return nuevo_pedido

