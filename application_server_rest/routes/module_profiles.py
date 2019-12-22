from fastapi import APIRouter

route = APIRouter()


@route.get("")
def list_module_profiles():
    pass


@route.post("")
def create_module_profiles():
    pass


@route.post("/{module_profile_id}")
def update_module_profiles(module_profile_id: int):
    pass


@route.delete("/{module_profile_id}")
def delete_module_profiles(module_profile_id: int):
    pass
