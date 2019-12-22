from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
import logging
import uuid

route = APIRouter()


@route.post("")
def authenticate(username: str, password: str):
    """
    Retourne un le client-id nécessaire pour authentifier les applications clientes et les applications d’administration.
    :param username: Nom de l'utilisateur
    :param passwrod: Mot de passe de l'utilisateur
    :return: {client-id : 9b48918efdad507a55154569ee7ade08005ac494cd528dc63986682776842e80}
    """
    logging.warning("%s %s" % (username, password))
    data = {'token': uuid.uuid4().hex}
    content = jsonable_encoder(data)
    return JSONResponse(content=content)


@route.post("/user")
def authenticate_user(username: str, passwrod: str):
    """
    Retourne le token de session nécessaire pour utiliser l’API REST.
    :param username: Nom de l'utilisateur
    :param passwrod: Mot de passe de l'utilisateur
    :return:{session-token : 3c469e9d6c5875d37a43f353d4f88e61fcf812c66eee3457465a40b0da4153e0}
    """
    pass
