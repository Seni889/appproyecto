from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from schemas.planusuarios import PlanUsuarioOut
from sqlmodel import Field
from schemas.pedidos import PedidoOut
from schemas.negocio import NegocioOut
from schemas.resenas import ResenaOut
from enum import Enum


class RolUsuario(str, Enum):
    usuario = "usuario"
    admin = "admin"
    
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono : str
    direccion : Optional[str] = None
    id_plan : int = 2
    rol : RolUsuario = RolUsuario.usuario

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    fecha_registro : datetime = Field(default_factory=datetime.utcnow)

    plan : Optional[PlanUsuarioOut]
    pedidos : List[PedidoOut] = []
    resenas : List[ResenaOut] = []
    negocio : Optional[NegocioOut] = None

    class Config:
        orm_mode = True

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str



