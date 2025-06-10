from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DetallePedidoBase(BaseModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    precio: float

class DetallePedidoCreate(DetallePedidoBase):
    pass

class DetallePedidoOut(DetallePedidoBase):
    id: int
    pedido_id: int
    producto_id: int
    cantidad: int
    class Config:
        orm_mode = True


class PedidoBase(BaseModel):
    id_usuario: int
    id_negocio: int
    total: Optional[float] = 0.0
    notas: Optional[str] = None
    detalles : List[DetallePedidoCreate]

class PedidoCreate(PedidoBase):
    pass

class PedidoOut(PedidoBase):
    id: int
    usuario_id: int
    restaurante_id: int
    detalles: List[DetallePedidoOut]

    class Config:
        orm_mode = True