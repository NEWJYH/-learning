from pydantic import BaseModel
from typing import List, Optional

# -------------------------------------------------------
class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True

# # 응답 모델 Response Model
# class ShowBlog(BaseModel):
#     # title만 필요할 경우 title 만지정
#     title : str
#     body : str
#     # relation
#     creator : ShowUser
    
#     # 내부클래스 Config 필요
#     class Config():
#         orm_mode = True
# -------------------------------------------------------

# 유저모델 
class User(BaseModel):
    name: str
    email : str
    password : str

# password 보여줄 필요없음
class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True

# 응답 모델 Response Model
class ShowBlog(BaseModel):
    # title만 필요할 경우 title 만지정
    title : str
    body : str
    # relation
    creator : ShowUser
    # 내부클래스 Config 필요
    class Config():
        orm_mode = True


class Login(BaseModel):
    email : str
    password : str



# JWT Access Token model


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None