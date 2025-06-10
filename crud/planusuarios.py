from sqlalchemy.orm import Session
from models.planusuarios import PlanUsuario
from schemas.planusuarios import PlanCreate

def get_plan(db: Session, plan_id: int):
    return db.query(PlanUsuario).filter(PlanUsuario.id == plan_id).first()

def get_planes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PlanUsuario).offset(skip).limit(limit).all()

def create_plan(db: Session, plan: PlanCreate):
    db_plan = PlanUsuario(
        nombre=plan.nombre,
        descripcion=plan.descripcion,
        precio_mensual=plan.precio_mensual
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def update_plan(db: Session, plan_id: int, plan_data: PlanCreate):
    plan_db = get_plan(db, plan_id)
    if not plan_db:
        return None
    plan_db.nombre = plan_data.nombre
    plan_db.descripcion = plan_data.descripcion
    plan_db.precio_mensual = plan_data.precio_mensual
    db.commit()
    db.refresh(plan_db)
    return plan_db

def delete_plan(db: Session, plan_id: int):
    plan_db = get_plan(db, plan_id)
    if not plan_db:
        return None
    db.delete(plan_db)
    db.commit()
    return plan_db
