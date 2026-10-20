
from sqlalchemy import Column, Integer, String, CheckConstraint
from database import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "age >= 18 AND age <= 150",
            name="check_user_age"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
