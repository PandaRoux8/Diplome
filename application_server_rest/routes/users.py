from fastapi import APIRouter
from typing import List

from models.out_models import User, ID
from models.in_models import User as IU
from models.in_models import UserAuth
from models.out_models import SessionToken


route = APIRouter()


@route.get(
    "",
    response_model=List[User]
)
def list_users():
    """
    Search and return all users from database.
    """
    pass


@route.post(
    "",
    response_model=ID
)
def create_users(user_values: IU):
    """
    Create a user in the database with the values sent in parameters.
    Return the database id of the object created
    """
    pass


@route.post("/{user_id}")
def update_users(user_id: int, user_values: IU):
    """
    Update the user (with the id passed in parameters) on the database with the values sent in parameters.
    """
    pass


@route.delete("/{user_id}")
def delete_users(user_id: int):
    """
    Delete the user (with the id passed in parameters) from the database.
    """
    pass


@route.post("/{user_id}/reset-password")
def reset_password(user_id: int, password):
    """
    Send an email to the user with the link of the webpage to reset his password
    """
    pass


@route.post(
    "/authenticate",
    response_model=SessionToken,
    response_model_include=["session_token"],
)
def authenticate_user(user: UserAuth):
    """
    Compare password sent with the password on the db.
    If the passwords match we generate session token that we send back to the user.
    The user will authenticate himself with this token .
    """
    pass
