from fastapi import APIRouter
from typing import List

from models.in_models import Notify

route = APIRouter()


@route.post("")
def notify(notify: Notify):
    """
    Endpoint to get notification for a task
    """
    pass
