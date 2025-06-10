from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from basedatos import Base

class PlanUsuario(Base):
    __tablename__ = "planes_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    descripcion = Column(String(255))
    precio_mensual = Column(Float)

    usuarios = relationship("Usuario", back_populates="plan")