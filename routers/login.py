from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from autenti import authenticate_user, create_access_token, get_db
from autenti import get_current_user, get_current_admin

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    
    access_token = create_access_token(data={"sub": str(user.id), "rol": user.rol})
    return {"access_token": access_token, "token_type": "bearer", "rol": user.rol}


@router.get("/usuarios")
def solo_usuarios(current_user=Depends(get_current_user)):
    return current_user

@router.get("/admin")
def solo_admins(admin=Depends(get_current_admin)):
    return {"mensaje": "Hola admin"}

