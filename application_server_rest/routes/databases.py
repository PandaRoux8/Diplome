from fastapi import APIRouter
from typing import List

from models.out_models import Database

route = APIRouter()


@route.get(
    "",
    response_model=List[Database]
)
def list_databases(database_id: int):
    """
    Search and list all client databases.
    """
    pass
