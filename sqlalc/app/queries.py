from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User, Post



session = SessionLocal()

def create_user(session: Session, email, password):
    new_user = User(
        email=email,
        password=password
    )


    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    print("User created:", new_user.id, new_user.email, new_user.password)
    

def update_user(session: Session, user_id, email=None, password=None):
    stmt = select(User).where(User.id == user_id)
    
    res = session.execute(stmt)
    user_obj = res.scalars().first()
    
    user_obj.email = email
    user_obj.password = password
    
    session.commit()
    session.refresh(user_obj)
    
    return user_obj


def delete_user(session: Session, user_id):
    stmt = select(User).where(User.id == user_id)
    res = session.execute(stmt)
    user_obj = res.scalars().first()
    
    session.delete(user_obj)
    session.commit()
    
    return 204


print(update_user(session=session, user_id=3, email="gishmat@gmail.com", password="gishmat01"))
print(delete_user(session=session, user_id=1))