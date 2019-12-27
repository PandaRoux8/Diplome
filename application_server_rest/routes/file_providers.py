from fastapi import APIRouter
from typing import List

from models.out_models import FileProvider, ID
from models.in_models import FileProvider as IFP


route = APIRouter()


@route.get(
    "",
    response_model=List[FileProvider]
)
def list_file_providers():
    """
    Search and return all file providers from database.
    """
    pass


@route.post(
    "",
    response_model=ID
)
def create_file_providers(file_provider_values: IFP):
    """
    Create a file provider in the database with the values sent in parameters.
    Return the database id of the object created
    """
    pass


@route.post("/{file_provider_id}")
def update_file_providers(file_provider_id: int, file_provider_values: IFP):
    """
    Update the file provider (with the id passed in parameters) on the database with the values sent in parameters.
    """
    pass


@route.delete("/{file_provider_id}")
def delete_file_providers(file_provider_id: int):
    """
    Delete the file provider (with the id passed in parameters) from the database.
    """
    pass
