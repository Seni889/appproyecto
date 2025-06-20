from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from basedatos import SessionLocal
from schemas.usuarios import Usuario, UsuarioCreate
from crud.usuarios import get_usuario, obtener_usuarios, crear_usuario, update_usuario, delete_usuario
from typing import List
from autenti import get_current_admin

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Usuario])
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_admin: Usuario = Depends(get_current_admin)):
    usuarios = obtener_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.get("/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db), current_admin: Usuario = Depends(get_current_admin)):
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, usuario)

@router.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, usuario_data: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = update_usuario(db, usuario_id, usuario_data)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@router.delete("/{usuario_id}", response_model=Usuario)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db), current_admin: Usuario = Depends(get_current_admin)):
    usuario = delete_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario
