from pydantic import BaseModel


class PlanBase(BaseModel):
    nombre: str
    descripcion: str
    precio_mensual : float
    

class PlanCreate(PlanBase):
    pass

class PlanUsuarioOut(PlanBase):
    id: int

    class Config:
        orm_mode = True