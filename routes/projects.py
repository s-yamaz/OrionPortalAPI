from fastapi import APIRouter
from database import fetch_all_projects

router = APIRouter(tags=["project"], prefix="/projects")


@router.get("/")
async def get_projects():
    return await fetch_all_projects()
