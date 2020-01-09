from fastapi import APIRouter
from typing import List

from models.out_models import Task

route = APIRouter()


@route.get(
    "",
    response_model=List[Task]
)
def list_tasks():
    """
    List all tasks on the server
    """
    pass
