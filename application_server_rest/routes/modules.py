from fastapi import APIRouter

route = APIRouter()


@route.get("")
def list_modules():
    pass


@route.get("/{module_id}")
def get_module(module_id: int):
    pass


@route.post("/install/{module_id}/{database_id}")
def module_install(module_id: int, database_id: int):
    pass


@route.post("install/{module_id}")
def module_install_everywhere(module_id: int):
    pass


@route.post("/update/{module_id}/{database_id}")
def module_update(module_id: int, database_id: int):
    pass


@route.post("/uninstall/{module_id}/{database_id}")
def module_uninstall(module_id: int, database_id: int):
    pass
