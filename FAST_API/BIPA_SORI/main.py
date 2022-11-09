from fastapi import FastAPI

#
import requests

# 모델 / 사용자로부터 post방식으로 입력받을 것
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {'Hello': "world"}

db = []

# 입력 BaseModel
class City(BaseModel):
    name: str
    timezone: str

@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        strs = f'http://worldtimeapi.org/api/timezone/{city["timezone"]}'
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({ 'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time })
    return results

# 건별 조회
@app.get("/cities/{city_id}")
def get_city(city_id : int):
    city = db[city_id -1]
    strs = f'http://worldtimeapi.org/api/timezone/{city["timezone"]}'
    r = requests.get(strs)
    cur_time = r.json()['datetime']
    return {
                'name':city['name'], 
                'timezone':city['timezone'], 
                'current_time':cur_time }


@app.post("/cities")
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete("/cities/{city_id}")
def delete_city(city_id : int):
    db.pop(city_id-1)
    return {}
