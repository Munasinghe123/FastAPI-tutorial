
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user_schema import UserCreate, UserUpdate
from controllers.user_controller import create_user,get_users,update_user,delete_user

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

@router.patch("/{user_id}")
def update(user_id:int, user:UserUpdate,db:Session=Depends(get_db)):
    updated_user = update_user(db,user_id,user.name)
    
    if not updated_user:
        raise HTTPException(status_code=404,detail = "User not found")
    
    return updated_user      
        
@router.delete("/{user_id}")
def delete(user_id:int,db:Session =Depends(get_db)):
    deleted_user = delete_user(db,user_id)
    
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return{"message":"user deleted successfully"}