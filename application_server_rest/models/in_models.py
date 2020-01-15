from pydantic import BaseModel
from typing import List


class FileProvider(BaseModel):
    name: str
    type: str
    path: str
    username: str = None
    password: str = None
    token: str = None


class ModuleProfile(BaseModel):
    name: int


class UserProfile(BaseModel):
    name: int


class User(BaseModel):
    username: str
    password: str


class Notify(BaseModel):
    task_id: int
    state: str
    error_message: str


class Database(BaseModel):
    id: int
    name: str
    uuid: str
    module_profile: List[int]
    user: str
    password: str
    client_app_id: int


class ClientApp(BaseModel):
    name: str
    address: str
    os: str
    os_version: str



