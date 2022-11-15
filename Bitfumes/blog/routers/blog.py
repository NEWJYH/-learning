from fastapi import APIRouter, Depends, status, HTTPException, Response
# 프레임워크 기준은 working dir 이기 때문에 from .. 필요없음
import schemas, database, models
from sqlalchemy.orm import Session
from typing import List
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db)):
    # blogs = db.query(models.Blog).all()
    # return blogs 
    return blog.get_all(db)


# http status_code Search
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    # new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    return blog.create(request, db)



@router.get('/{id}', response_model= schemas.ShowBlog)
def show(id, response:Response, db:Session = Depends(database.get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'Blog with th id == {id} is not available')
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(database.get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found" )
    # blog.delete(synchronize_session=False)
    # db.commit()
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session = Depends(database.get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail=f"Blog with id {id} not found" )
    # blog.update(request)
    # db.commit()
    return blog.update(id, request, db)