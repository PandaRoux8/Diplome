from fastapi import FastAPI
import requests
from starlette.responses import JSONResponse, Response

app = FastAPI()

############################################
#            AUTHENTICATION
############################################
@app.post("/authenticate")
def authenticate(username: str, password: str):
    """
    Retourne un le client-id nécessaire pour authentifier les applications clientes et les applications d’administration.
    :param username: Nom de l'utilisateur
    :param passwrod: Mot de passe de l'utilisateur
    :return: {client-id : 9b48918efdad507a55154569ee7ade08005ac494cd528dc63986682776842e80}
    """
    content = {"message": "Hello World"}
    headers = {"application/json": "alone in the world"}
    r = Response()
    r.headers["application/json"] = "application/json"
    return r
    # return JSONResponse(content=content, headers=headers)


@app.post("/authenticate-user")
def authenticate_user(username: str, passwrod: str):
    """
    Retourne le token de session nécessaire pour utiliser l’API REST.
    :param username: Nom de l'utilisateur
    :param passwrod: Mot de passe de l'utilisateur
    :return:{session-token : 3c469e9d6c5875d37a43f353d4f88e61fcf812c66eee3457465a40b0da4153e0}
    """
    pass


############################################
#                 MODULES
############################################
@app.get("/modules")
def list_modules():
    pass


@app.get("/modules/{module_id}")
def get_module(module_id: int):
    pass


@app.post("modules/install/{module_id}/{database_id}")
def module_install(module_id: int, database_id: int):
    pass


@app.post("modules/install/{module_id}")
def module_install_everywhere(module_id: int):
    pass


@app.post("/modules/update/{module_id}/{database_id}")
def module_update(module_id: int, database_id: int):
    pass


@app.post("/modules/uninstall/{module_id}/{database_id}")
def module_uninstall(module_id: int, database_id: int):
    pass


############################################
#                 USERS
############################################
@app.get("/users")
def list_users():
    pass


@app.post("/users")
def create_users():
    pass


@app.post("/users/{user_id}")
def update_users(user_id: int):
    pass


@app.delete("/users/{user_id}")
def delete_users(user_id: int):
    pass


############################################
#           MODULE PROFILES
############################################
@app.get("/module-profiles")
def list_module_profiles():
    pass


@app.post("/module-profiles")
def create_module_profiles():
    pass


@app.post("/module-profiles/{module_profile_id}")
def update_module_profiles(module_profile_id: int):
    pass


@app.delete("/module-profiles/{module_profile_id}")
def delete_module_profiles(module_profile_id: int):
    pass

############################################
#              USER PROFILES
############################################
@app.get("/user-profiles")
def list_user_profiles():
    pass


@app.post("/user-profiles")
def create_user_profiles():
    pass


@app.post("/user-profiles/{user_profile_id}")
def update_user_profiles(user_profile_id: int):
    pass


@app.delete("/user-profiles/{user_profile_id}")
def delete_user_profiles(user_profile_id: int):
    pass

############################################
#               FILE PROVIDERS
############################################
@app.get("/file-providers")
def list_file_providers():
    pass


@app.post("/file-providers")
def create_file_providers():
    pass


@app.post("/file-providers/{file_provider_id}")
def update_file_providers(file_provider_id: int):
    pass


@app.delete("/file-providers/{file_provider_id}")
def delete_file_providers(file_provider_id: int):
    pass

############################################
#               DATABASE
############################################
@app.get("/databases")
def list_databases():
    pass
