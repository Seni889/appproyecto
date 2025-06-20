from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from basedatos import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    telefono = Column(String(10),nullable=False )
    direccion = Column(String(200))
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    id_plan = Column(Integer, ForeignKey("planes_usuarios.id"))
    
    hashed_password = Column(String(200), nullable=False)
    rol = Column(String(50), default="usuario") #usuario o admin

    plan = relationship("PlanUsuario", back_populates="usuarios")
    pedidos = relationship("Pedido", back_populates="usuarios")
    resenas = relationship("Resenas", back_populates="usuarios")
    negocios = relationship("Negocio", back_populates="usuarios")

