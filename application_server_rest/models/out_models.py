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


class UserProfile(BaseModel):
    id: int


class User(BaseModel):
    username: str
    password: str


class ID(BaseModel):
    id: int
