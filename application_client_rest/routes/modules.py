from fastapi import APIRouter
from typing import List

from models.out_models import Module, DatabaseModule

route = APIRouter()


@route.get(
    "",
    response_model=List[DatabaseModule],
)
def list_modules():
    """
    Search and return the list of all modules on every database.
    """
    pass


@route.get(
    "/{db_name}",
    response_model=List[Module]
)
def list_modules_on_db(db_name: str):
    """
    Search all modules available on the database precised by the db_name parameter.
    """
    pass


@route.post("/install/{module_id}/{database_name}")
def module_install(module_id: int, database_name: str):
    """
    Endpoint on which you receive an installation request.
    Create a task for the installation of the module.
    """
    pass


@route.post("/update/{module_id}/{database_name}")
def module_update(module_id: int, database_name: int):
    """
    Endpoint on which you receive an update request.
    Create a task for the update of the module.
    """
    pass


@route.post("/uninstall/{module_id}/{database_name}")
def module_uninstall(module_id: int, database_name: int):
    """
    Endpoint on which you receive an uninstall request.
    Create a task for the uninstall of the module.
    """
    pass
