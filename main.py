from fastapi import FastAPI
from routes import projects

api = FastAPI()

api.include_router(projects.router)


@api.get("/")
def hello():
    return {"message": "hello"}
