from fastapi import FastAPI
from routes import projects, node_logs, conversations

api = FastAPI()

api.include_router(projects.router)
api.include_router(node_logs.router)
api.include_router(conversations.router)


@api.get("/")
def hello():
    return {"message": "hello"}
