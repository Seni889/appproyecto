from fastapi import FastAPI
from basedatos import Base, engine
from routers import categorias,negocio, pedido, planusuarios, producto, resenas, usuarios, login
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI()



@app.get("/")
def read_root():
    return {"mensaje": "¡FastAPI está corriendo!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # o ["*"] para todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(usuarios.router)
app.include_router(negocio.router)
app.include_router(categorias.router)
app.include_router(pedido.router)
app.include_router(planusuarios.router)
app.include_router(resenas.router)
app.include_router(producto.router)
app.include_router(login.router)

