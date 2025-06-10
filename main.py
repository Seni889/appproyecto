from fastapi import FastAPI
from basedatos import Base, engine
from routers import categorias,negocio, pedido, planusuarios, producto, resenas, usuarios, personalizacion

Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡FastAPI está corriendo!"}

app.include_router(usuarios.router)
app.include_router(negocio.router)
app.include_router(categorias.router)
app.include_router(pedido.router)
app.include_router(planusuarios.router)
app.include_router(resenas.router)
app.include_router(producto.router)
app.include_router(personalizacion.router)

