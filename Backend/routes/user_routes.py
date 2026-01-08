
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user_schema import UserCreate
from controllers.user_controller import create_user,get_users

router= APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/")
def create(user:UserCreate, db:Session = Depends(get_db)):
    return create_user(db,user.name)

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return get_users(db)        
        