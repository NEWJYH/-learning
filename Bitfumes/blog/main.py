from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, models, hashing
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
# 비밀번호 해쉬
# from passlib.context import CryptContext

from routers import blog

app = FastAPI()

models.Base.metadata.create_all(engine)

#Router
app.include_router(blog.router)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# http status_code Search
@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request : schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# @app.get('/blog')
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs



# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@app.get('/blog/{id}', response_model= schemas.ShowBlog, tags=['blogs'])
def show(id, response:Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with th id == {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f'detail':'Blog with th id == {id} is not available'}
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found" )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":f"{id} is deleted"}

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with id {id} not found" )
    blog.update(request)
    db.commit()
    return 'updated'


# 비밀번호 설정하려면 해야함 .
# pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

# @app.post('/user')
# def create_user(request:schemas.User, db:Session = Depends(get_db)):
#     #--
#     # 암호화된 PWd를 획득
#     hashedPassoword = pwd_cxt.hash(request.password)
#     #-- 
#     new_user = models.User(name=request.name, email=request.email, password=hashedPassoword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


@app.post('/user', response_model=schemas.ShowUser, tags=['Users'])
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id {id} is not available")
    return user