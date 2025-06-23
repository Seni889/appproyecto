from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from basedatos import Base

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    nombre = Column(String(255), nullable=False)
    descripcion =Column(String(255))
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean)
    id_negocio = Column(Integer, ForeignKey("negocio.id"))

    negocio = relationship("Negocio", back_populates="productos")
    categoria = relationship("Categoria", back_populates="productos")
    detalle_pedidos = relationship("DetallePedido", back_populates="productos")

