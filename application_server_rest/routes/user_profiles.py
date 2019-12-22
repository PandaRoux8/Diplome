from fastapi import APIRouter

route = APIRouter()


@route.get("")
def list_user_profiles():
    pass


@route.post("")
def create_user_profiles():
    pass


@route.post("/{user_profile_id}")
def update_user_profiles(user_profile_id: int):
    pass


@route.delete("/{user_profile_id}")
def delete_user_profiles(user_profile_id: int):
    pass
