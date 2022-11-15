
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
# relationships table connect to table
# 테이블끼리 연결하기
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    # relationships
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='blogs')


class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    # relationships
    blogs = relationship('Blog', back_populates='creator')

