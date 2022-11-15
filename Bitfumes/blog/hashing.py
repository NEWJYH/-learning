# 비밀번호 해쉬 부분을 옮겨보자.
from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)