from fastapi import APIRouter
from typing import List
from models.out_models import ClientApp, ClientID, SessionToken
from models.in_models import ClientApp as CAI
from models.in_models import User


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
def update_client_app(client_app_id: int, client_app_values: CAI):
    """
    Update the user (with the id passed in parameters) on the database with the values sent in parameters.
    """
    pass


@route.delete("/{client_app_id}")
def delete_client_app(client_app_id: int, user_id: int):
    """
    Delete the user (with the id passed in parameters) from the database.
    """
    pass


@route.post(
    "/authenticate",
    response_model=ClientID,
    response_model_include=["client_id"],
)
def authenticate(user: User, client_values: CAI):
    """
    Generate a client_id allowing the client app and admin app to authenticate to the application server.
    """
    pass
