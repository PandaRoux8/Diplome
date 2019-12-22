from fastapi import APIRouter

route = APIRouter()


@route.get("")
def list_file_providers():
    pass


@route.post("")
def create_file_providers():
    pass


@route.post("/{file_provider_id}")
def update_file_providers(file_provider_id: int):
    pass


@route.delete("/{file_provider_id}")
def delete_file_providers(file_provider_id: int):
    pass