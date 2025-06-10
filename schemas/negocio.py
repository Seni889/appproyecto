from pydantic import BaseModel, Field
from typing import Optional
from datetime import time

class NegocioBase(BaseModel):
    nombre: str
    direccion: Optional[str] = None
    descripcion : str
    telefono : str
    horario_apertura : time
    horario_cierre : time
    activo : Optional[bool] = True 
    logo_url : Optional[str] = Field(default=None, max_length=255)

class NegocioCreate(NegocioBase):
    pass
    id_usuario : int
    id_categoria : int

class NegocioOut(NegocioBase):
    id: int
    nombre: str
    direccion : Optional[str] = None
    class Config:
        orm_mode = True