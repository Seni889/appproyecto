from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from basedatos import SessionLocal
from crud.planusuarios import get_plan, get_planes, create_plan, delete_plan, update_plan
from schemas.planusuarios import PlanCreate, PlanUsuarioOut

router = APIRouter(
    prefix="/planes",
    tags=["Planes de Usuario"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PlanUsuarioOut])
async def read_planes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    planes = get_planes(db, skip=skip, limit=limit)
    return planes

@router.get("/{plan_id}", response_model=PlanUsuarioOut)
async def read_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = get_plan(db, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
    return plan

@router.post("/", response_model=PlanUsuarioOut)
async def crear_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    return create_plan(db, plan)

@router.put("/{plan_id}", response_model=PlanUsuarioOut)
async def actualizar_plan(plan_id: int, plan: PlanCreate, db: Session = Depends(get_db)):
    updated_plan = update_plan(db, plan_id, plan)
    if not updated_plan:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
    return updated_plan

@router.delete("/{plan_id}", response_model=PlanUsuarioOut)
async def eliminar_plan(plan_id: int, db: Session = Depends(get_db)):
    deleted_plan = delete_plan(db, plan_id)
    if not deleted_plan:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
    return deleted_plan