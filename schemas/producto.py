from pydantic import BaseModel
from typing import Optional

# Base común
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    disponible: Optional[bool] = True
    id_categoria: int

# Para crear productos
class ProductoCreate(ProductoBase):
    pass

# Para respuesta al cliente
class ProductoOut(ProductoBase):
    id: int
    nombre : str

    class Config:
        orm_mode = True

