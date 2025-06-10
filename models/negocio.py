from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Time
from sqlalchemy.orm import relationship
from basedatos import Base
from .usuarios import Usuario

class Negocio(Base):
    __tablename__ = "negocio"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(100), nullable=False)
    direccion = Column(String(200))
    telefono = Column(String(100))
    horario_apertura = Column(Time)
    horario_cierre = Column(Time)
    logo_url = Column(String(255))
    activo = Column(Boolean)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    id_categoria = Column(Integer, ForeignKey("categorias.id"))

    usuarios = relationship("Usuario", back_populates="negocios")
    resenas = relationship("Resenas", back_populates="negocios")
    pedidos = relationship("Pedido", back_populates="negocios")
    categoria = relationship("Categoria", back_populates="negocios")

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    
    productos = relationship("Producto", back_populates="categoria")
    negocios = relationship("Negocio", back_populates="categoria")

