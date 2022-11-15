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
    # new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"User with id {id} is not available")
#     return user
    return user.get(id, db)
