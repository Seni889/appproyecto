from pydantic import BaseModel
from typing import Optional, List

class PersonalizacionBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio_extra: float

class PersonalizacionCreate(PersonalizacionBase):
    pass

class PersonalizacionOut(PersonalizacionBase):
    id: int
    

    class Config:
        orm_mode = True



class DetallePersonalizacionBase(BaseModel):
    id_detalle_pedido: int
    id_personalizacion: int

class DetallePersonalizacionCreate(DetallePersonalizacionBase):
    pass

class DetallePersonalizacionOut(DetallePersonalizacionBase):
    id: int

    class Config:
        orm_mode = True


class ProductoPersonalizadoBase(BaseModel):
    id_producto: int
    id_personalizacion: int

class ProductoPersonalizadoCreate(ProductoPersonalizadoBase):
    pass

class ProductoPersonalizadoOut(ProductoPersonalizadoBase):
    id: int

    class Config:
        orm_mode = True
