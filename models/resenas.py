from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from basedatos import Base
from datetime import datetime

class Resenas(Base):
    __tablename__ = "resenas"
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    id_negocio = Column(Integer, ForeignKey("negocio.id"))
    calificacion = Column(Integer, nullable=False)
    comentario = Column(String(255), unique=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)

    usuarios = relationship("Usuario", back_populates="resenas")
    negocios = relationship("Negocio", back_populates="resenas")


