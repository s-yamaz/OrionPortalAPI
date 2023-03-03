from fastapi import APIRouter
from functions.projects import fetch_all_projects

router = APIRouter(tags=["project"], prefix="/projects")


@router.get("/")
def get_projects():
    return fetch_all_projects()
