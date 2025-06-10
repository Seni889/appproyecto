from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from schemas.planusuarios import PlanUsuarioOut
from sqlmodel import Field
from schemas.pedidos import PedidoOut
from schemas.negocio import NegocioOut
from schemas.resenas import ResenaOut

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono : str
    direccion : Optional[str] = None
    id_plan : int

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    fecha_registro : datetime = Field(default_factory=datetime.utcnow)

    plan : Optional[PlanUsuarioOut]
    pedidos : List[PedidoOut] = []
    resenas : List[ResenaOut] = []
    negocio : Optional[NegocioOut] = None

    class Config:
        orm_mode = True