from fastapi import APIRouter, Depends, status, HTTPException, Response
# 프레임워크 기준은 working dir 이기 때문에 from .. 필요없음
import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from typing import List
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# http status_code Search
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)



@router.get('/{id}', response_model= schemas.ShowBlog)
def show(id, response:Response, db:Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(database.get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session = Depends(database.get_db)):
    return blog.update(id, request, db)