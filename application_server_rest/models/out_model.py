from pydantic import BaseModel


class ClientID(BaseModel):
    client_id: str


class SessionToken(BaseModel):
    session_token: str


class Database(BaseModel):
    name: str
    uuid: str
    server: int
