# fast api 기본 class
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "hello"

@app.get("/data")
def data():
    return {'hello' : 1234 }

# html 파일 전송
from fastapi.responses import FileResponse
@app.get('/index')
def index():
    return FileResponse('index.html')

# 유저가 서버에 데이터 보내기 

# 유저에게 데이터를 받으려면 모델 생성해야함
from pydantic import BaseModel
class Model(BaseModel):
    name : str
    phone : int


@app.post("/send")
def send(data : Model):
    print(data.name)
    print(data.phone)
    return data

# 비동기처리 
# 코루틴 
import asyncio
@app.get("/async")
async def asy():
    print('hello')
    await asyncio.sleep(5)
    print('world')
    return "hello"