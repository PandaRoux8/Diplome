from pydantic import BaseModel
from datetime import datetime
from typing import List


class ClientID(BaseModel):
    client_id: str


class SessionToken(BaseModel):
    session_token: str


class Database(BaseModel):
    id: int
    name: str
    uuid: str
    module_profile: List[int]
    user: str
    password: str
    client_app_id: int


class Module(BaseModel):
    id: int
    name: str
    version: str
    author: str


class FileProvider(BaseModel):
    id: int
    name: str
    type: str
    path: str


class ModuleProfile(BaseModel):
    id: int
    name: str


class UserProfile(BaseModel):
    id: int


class User(BaseModel):
    username: str
    password: str


class ID(BaseModel):
    id: int


class Task(BaseModel):
    id: int
    name: str
    priority: str
    state: str
    create_date: datetime
    write_date: datetime
    origin: str
    user_name: str
    action_id: int
    code: str
    values: dict
    error_message: str


class ClientApp(BaseModel):
    id: int
    name: str
    address: str
    os: str
    os_version: str
    client_id: str
