from fastapi import APIRouter

route = APIRouter()


@route.post("/client-db")
def update_client_db():
    """
    Update the client db list on the server's database.
    """
    pass


@route.post("/client-modules")
def update_client_modules():
    """
    Update the client modules list on the server's database.
    """
    pass


@route.post("/client-app")
def update_client_app():
    """
    Update the client application information on the server's database.
    """
    pass

