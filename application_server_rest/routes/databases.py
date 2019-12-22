from fastapi import APIRouter

route = APIRouter()


@route.get("")
def list_databases():
    pass
