from pydantic import BaseModel


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

