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
    erp_version: str
    user: str
    password: str
    module_profile_ids: List[int]
    client_app_id: int


class Module(BaseModel):
    id: int
    name: str
    version: str
    description: str
    author: str
    file_provider_id: int
    module_profile_ids: List[int]


class FileProvider(BaseModel):
    id: int
    name: str
    type: str
    path: str
    username: str
    password: str
    token: str
    last_update: datetime


class ModuleProfile(BaseModel):
    id: int
    name: str
    module_ids: List[int]


class UserProfile(BaseModel):
    id: int


class User(BaseModel):
    id: int
    username: str
    password: str
    mail: str
    session_token: str
    user_profile_id: int
    database_ids: List[int]
    is_admin: bool


class ID(BaseModel):
    id: int


class Task(BaseModel):
    id: int
    name: str
    priority: str
    state: str
    create_date: datetime
    write_date: datetime
    target_db_id: int
    origin: str
    user_id: int
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
