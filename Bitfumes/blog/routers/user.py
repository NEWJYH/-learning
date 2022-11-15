from fastapi import APIRouter, Depends
# 프레임워크 기준은 working dir 이기 때문에 from .. 필요없음
import schemas, database
from sqlalchemy.orm import Session
from repository import user

router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
    return user.get(id, db)
