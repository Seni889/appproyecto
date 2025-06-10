from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from basedatos import Base

class Personalizacion(Base):
    __tablename__ = "personalizacion"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200))
    precio_extra = Column(Float)

    detalle_personalizacion = relationship("DetallePersonalizacion", back_populates="personalizacion")
    producto_personalizado = relationship("ProductoPersonalizado", back_populates="personalizacion")
    
class DetallePersonalizacion(Base):
    __tablename__ = "detalle_personalizacion"
    id = Column(Integer, primary_key=True, index=True)
    id_detalle_pedido = Column(Integer, ForeignKey("detalle_pedido.id"))
    id_personalizacion = Column(Integer, ForeignKey("personalizacion.id"))

    personalizacion = relationship("Personalizacion", back_populates="detalle_personalizacion")
    detalle_pedidos = relationship("DetallePedido", back_populates="detalle_personalizacion")


class ProductoPersonalizado(Base):
    __tablename__ = "producto_personalizacion"
    id = Column(Integer, primary_key=True, index=True)
    id_producto = Column(Integer, ForeignKey("productos.id"))
    id_personalizacion = Column(Integer, ForeignKey("personalizacion.id"))

    personalizacion = relationship("Personalizacion", back_populates="producto_personalizado")
    productos = relationship("Producto", back_populates="producto_personalizacion")