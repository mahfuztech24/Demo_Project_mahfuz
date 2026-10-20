from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schema import UserCreateRequest
from database import get_db
from service import UserService

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserCreateRequest,
    db: Session = Depends(get_db)
):
    service = UserService()
    result = service.create_user(db, payload)

    return result