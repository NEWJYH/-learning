from fastapi import FastAPI
import models
from database import engine

# 비밀번호 해쉬
# from passlib.context import CryptContext

from routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

#Router
app.include_router(blog.router)
app.include_router(user.router)

