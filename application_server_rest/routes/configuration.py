from fastapi import APIRouter

route = APIRouter()


@route.get("/timeout")
def get_timeout():
    """
    Endpoint to get notification for a task
    """
    pass


@route.post("/timeout")
def set_timeout(timeout: int):
    """
    Endpoint to get notification for a task
    """
    pass
