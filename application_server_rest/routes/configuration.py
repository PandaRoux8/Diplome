from fastapi import APIRouter

route = APIRouter()


@route.get("/timeout")
def get_timeout():
    """
    Get the configured timeout for the tasks
    """
    pass


@route.post("/timeout")
def set_timeout(timeout: int):
    """
    Set a new time for tasks timeout
    """
    pass
