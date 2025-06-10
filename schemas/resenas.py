from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ResenaBase(BaseModel):
    calificacion: int
    comentario: str
    id_usuario: int
    id_negocio: int

class ResenaCreate(ResenaBase):
    pass

class ResenaOut(ResenaBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
