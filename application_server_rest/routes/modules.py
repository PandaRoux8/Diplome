from fastapi import APIRouter, Header
from typing import List

from models.out_models import Module

route = APIRouter()


@route.get(
    "",
    response_model=List[Module],
)
def list_modules(session_token: str = Header(None)):
    """
    Search and return the list of available modules on all file providers.
    """
    pass


@route.get("/{module_id}")
def get_module(module_id: int, task_id: int, client_id: str = Header(None)):
    """
    Search for the module with the parameter module_id. Then, we create and return an archive (.zip) with the file of the module.
    """
    pass


@route.post("/install/{module_id}/{database_id}")
def module_install(module_id: int, database_id: int, task_id: int, session_token: str = Header(None)):
    """
    Send an installation request of the selected module (module_id) on a targeted database (database_id).
    """
    pass


@route.post("/install/{module_id}")
def module_install_everywhere(module_id: int, task_id: int, session_token: str = Header(None)):
    """
    Send an installation request of the selected module (module_id) on all registered databases.
    """
    pass


@route.post("/update/{module_id}/{database_id}")
def module_update(module_id: int, database_id: int, task_id: int, session_token: str = Header(None)):
    """
    Send an update request of the selected module (module_id) on a targeted database (database_id).
    """
    pass


@route.post("/update/{module_id}")
def module_update_everywhere(module_id: int, task_id: int, session_token: str = Header(None)):
    """
    Send an update request of the selected module (module_id) on all registered databases.
    """
    pass


@route.post("/uninstall/{module_id}/{database_id}")
def module_uninstall(module_id: int, database_id: int, task_id: int, session_token: str = Header(True)):
    """
    Send an uninstalling request of the selected module (module_id) on a targeted database (database_id).
    """
    pass


@route.post("/uninstall/{module_id}")
def module_uninstall_everywhere(module_id: int, task_id: int, session_token: str = Header(None)):
    """
    Send an uninstalling request of the selected module (module_id) on all registered databases.
    """
    pass

