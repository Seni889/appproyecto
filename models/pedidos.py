from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from basedatos import Base
from enum import Enum

class EstadoPedidoEnum(str, Enum):
    pendiente = "pendiente"
    procesando = "procesando"
    entregado = "entregado"
    cancelado = "cancelado"

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    id_negocio = Column(Integer, ForeignKey("negocio.id"))
    fecha = Column(DateTime, default=func.now())
    estado = Column(Boolean, default=True)
    total = Column (Float, default=0.0)
    notas = Column(String(150), nullable=True)

    usuarios = relationship("Usuario", back_populates="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedidos")
    negocios = relationship("Negocio", back_populates="pedidos")

class DetallePedido(Base):
    __tablename__ = "detalle_pedido"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    precio = Column(Float)

    pedidos = relationship("Pedido", back_populates="detalles")
    productos = relationship("Producto", back_populates="detalle_pedidos")
    

