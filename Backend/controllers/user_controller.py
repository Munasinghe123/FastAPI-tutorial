from sqlalchemy.orm import Session
from models.user_model import User

def create_user(db: Session, name: str):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db:Session):
    return db.query(User).all()

def update_user(db:Session,user_id:int,name:str):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return None
    
    user.name = name
    db.commit()
    db.refresh(user)
    return user

def delete_user(db:Session,user_id:int):
     user = db.query(User).filter(User.id == user_id).first()
     
     if not user:
         return None
     
     db.delete(user)
     db.commit()
     return user