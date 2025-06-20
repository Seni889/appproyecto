from sqlalchemy.orm import Session, joinedload
from models.usuarios import Usuario
from schemas.usuarios import UsuarioCreate
from autenti import hash_password

def crear_usuario(db: Session, usuario: UsuarioCreate):
    existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if existente:
        raise ValueError("El correo ya está registrado.")
    hashed_pw = hash_password(usuario.password)
    db_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        telefono=usuario.telefono,
        direccion=usuario.direccion,
        id_plan=2,
        hashed_password=hashed_pw,
        rol=usuario.rol or "usuario"
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).options(joinedload(Usuario.plan)).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).options(joinedload(Usuario.plan)).filter(Usuario.id == usuario_id).first()

def update_usuario(db: Session, usuario_id: int, usuario_data: UsuarioCreate):
    db_usuario = get_usuario(db, usuario_id)
    if not db_usuario:
        return None
    for key, value in usuario_data.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario(db, usuario_id)
    if not db_usuario:
        return None
    db.delete(db_usuario)
    db.commit()
    return db_usuario


