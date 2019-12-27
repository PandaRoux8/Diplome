from fastapi import APIRouter
from typing import List

from models.out_models import UserProfile, ID
from models.in_models import UserProfile as IUP

route = APIRouter()


@route.get(
    "",
    response_model=List[UserProfile]
)
def list_user_profiles():
    """
    Search and return all user profiles from database.
    """
    pass


@route.post(
    "",
    response_model=ID
)
def create_user_profiles(user_profile_values: IUP):
    """
    Create a user profile in the database with the values sent in parameters.
    Return the database id of the object created
    """
    pass


@route.post("/{user_profile_id}")
def update_user_profiles(user_profile_id: int, user_profile_values: IUP):
    """
    Update the user profile (with the id passed in parameters) on the database with the values sent in parameters.
    """
    pass


@route.delete("/{user_profile_id}")
def delete_user_profiles(user_profile_id: int):
    """
    Delete the user profile (with the id passed in parameters) from the database.
    """
    pass
