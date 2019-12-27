from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
import uuid
import logging

from models.in_models import User
from models.out_models import ClientID, SessionToken

route = APIRouter()


@route.post(
    "",
    response_model=ClientID,
    response_model_include=["client_id"],
)
def authenticate(user: User):
    """
    Generate a client_id allowing the client app and admin app to authenticate to the application server.
    """
    pass


@route.post(
    "/user",
    response_model=SessionToken,
    response_model_include=["session_token"],
)
def authenticate_user(user: User):
    """
    Generate session token allowing the user to be authenticated.
    """
    pass
