from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from models.pedidos import EstadoPedidoEnum


class DetallePedidoCreate(BaseModel):
    producto_id: int
    cantidad: int

class DetallePedidoOut(BaseModel):
    producto_id: int
    cantidad: int
    precio: float
    class Config:
        orm_mode = True


class PedidoCreate(BaseModel):
    notas: Optional[str] = None
    detalles : List[DetallePedidoCreate]

class PedidoOut(BaseModel):
    id: int
    id_usuario: int
    id_negocio: Optional[int]
    notas :str
    detalles: List[DetallePedidoOut]

    class Config:
        orm_mode = True

class PedidoEstadoUpdate(BaseModel):
    estado: EstadoPedidoEnum

    class Config:
        orm_mode = True