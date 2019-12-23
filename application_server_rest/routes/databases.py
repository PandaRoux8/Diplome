from fastapi import APIRouter
from models.out_model import Database

route = APIRouter()


@route.get(
    "",
    response_model=Database
)
def list_databases(database_id):
    pass
