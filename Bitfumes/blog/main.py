from fastapi import FastAPI
import models
from database import engine



from routers import blog, user, authentication

import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)

#Router
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)