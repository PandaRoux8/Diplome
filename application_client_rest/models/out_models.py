from typing import List
from pydantic import BaseModel
from datetime import datetime


class ClientID(BaseModel):
    client_id: str


class SessionToken(BaseModel):
    session_token: str


class Database(BaseModel):
    name: str
    uuid: str
    erp_version: str


class Module(BaseModel):
    name: str
    version: str
    author: str
    description: str
    database_name: str
    module_profile_ids: List[int]
    installed: bool


class FileProvider(BaseModel):
    id: int
    name: str
    type: str
    path: str


class ModuleProfile(BaseModel):
    id: int


class UserProfile(BaseModel):
    id: int


class User(BaseModel):
    username: str
    password: str


class ID(BaseModel):
    id: int


class DatabaseModule(BaseModel):
    database_name: str
    modules: List[Module]


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
