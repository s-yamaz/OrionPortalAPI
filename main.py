from fastapi import FastAPI
from database import fetch_all_projects

api = FastAPI()


@api.get("/")
def hello():
    return {"message": "hello"}


@api.get("/projects", tags=["projects"])
async def get_projects():
    return await fetch_all_projects()
