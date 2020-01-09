from fastapi import APIRouter
from typing import List
from models.out_models import ClientApp
from models.in_models import ClientApp as CAI

route = APIRouter()


@route.get(
    "",
    response_model=List[ClientApp]
)
def list_client_app():
    """
    Search and return all users from database.
    """
    pass


@route.post("/{client_app_id}")
def update_users(client_app_id: int, client_app_values: CAI):
    """
    Update the user (with the id passed in parameters) on the database with the values sent in parameters.
    """
    pass


@route.delete("/{client_app_id}")
def delete_users(client_app_id: int, user_id: int):
    """
    Delete the user (with the id passed in parameters) from the database.
    """
    pass
