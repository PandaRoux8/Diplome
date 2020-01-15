from fastapi import FastAPI, Depends, Header, HTTPException
from routes import databases, modules, tasks


app = FastAPI()


async def get_token_header(client_id: str = Header(...)):
    if client_id != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="Session-Token invalid")

app.include_router(
    modules.route,
    prefix="/modules",
    tags=["Modules"],
    dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Module not found."},
    },

)

app.include_router(
    databases.route,
    prefix="/databases",
    tags=["Databases"],
    dependencies=[Depends(get_token_header)],
)

app.include_router(
    tasks.route,
    prefix="/tasks",
    tags=["Tasks"],
    dependencies=[Depends(get_token_header)],
)
