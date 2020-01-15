from fastapi import APIRouter
from typing import List

from models.in_models import Database as DI
from models.out_models import Database

route = APIRouter()


@route.get(
    "",
    response_model=List[Database]
)
def list_databases():
    """
    Search and list all client databases.
    """
    pass


@route.get(
    "/{database_id}",
    response_model=Database
)
def get_database(database_id: int):
    """
    Search for a specific database.
    """
    pass
