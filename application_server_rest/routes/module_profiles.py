from fastapi import APIRouter
from typing import List

from models.out_models import ModuleProfile, ID
from models.in_models import ModuleProfile as IMP

route = APIRouter()


@route.get(
    "",
    response_model=List[ModuleProfile]
)
def list_module_profiles():
    """
    Search and return all module profiles from database.
    """
    pass


@route.post(
    "",
    response_model=ID
)
def create_module_profiles(module_profile_values: IMP):
    """
    Create a module profile in the database with the values sent in parameters.
    Return the database id of the object created
    """
    pass


@route.post("/{module_profile_id}")
def update_module_profiles(module_profile_id: int, module_profile_values: IMP):
    """
    Update the module profile (with the id passed in parameters) on the database with the values sent in parameters.
    """
    pass


@route.delete("/{module_profile_id}")
def delete_module_profiles(module_profile_id: int):
    """
    Delete the module profile (with the id passed in parameters) from the database.
    """
    pass
