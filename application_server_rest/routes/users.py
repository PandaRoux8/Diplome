from fastapi import APIRouter

route = APIRouter()


@route.get("")
def list_users():
    pass


@route.post("")
def create_users():
    pass


@route.post("/{user_id}")
def update_users(user_id: int):
    pass


@route.delete("/{user_id}")
def delete_users(user_id: int):
    pass
