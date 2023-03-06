from fastapi import APIRouter
from functions.node_logs import get_all_logs_by_node

router = APIRouter(tags=["node_logs"], prefix="/node_logs")


@router.get("/{node_id}")
def get_by_node(node_id: str):
    return get_all_logs_by_node(node_id)
