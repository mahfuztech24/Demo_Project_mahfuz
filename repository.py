
from sqlalchemy.orm import Session
from user import User


class UserRepository:
    def create_user(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_id(self, db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def get_all_user(self, db: Session):
        return db.query(User).all()
