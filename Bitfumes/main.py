from fastapi import FastAPI




app = FastAPI()


@app.get('/')
async def index():
    return {'data':{'name':'sarthak'}}


@app.get('/about')
def about():
    return {'data': {'about page'}}