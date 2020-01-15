from fastapi import APIRouter
from typing import List

from models.out_models import Task
from models.in_models import Notify

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


@route.post("")
def notify(notify: Notify):
    """
    Endpoint to get notification for a task
    """
    pass
