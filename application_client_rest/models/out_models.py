from typing import List
from pydantic import BaseModel


class ClientID(BaseModel):
    client_id: str


class SessionToken(BaseModel):
    session_token: str


class Database(BaseModel):
    id: int
    name: str
    uuid: str


class Module(BaseModel):
    name: str
    version: str
    author: str
    description: str
    database_name: str
    module_profile: List[str]
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
    database: List[Module]
