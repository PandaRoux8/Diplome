from fastapi import FastAPI, Depends, Header, HTTPException
from routes import databases, modules, notify


app = FastAPI()

app.include_router(
    modules.route,
    prefix="/modules",
    tags=["Modules"],
    responses={
        404: {"description": "Module not found."},
    },

)

app.include_router(
    databases.route,
    prefix="/databases",
    tags=["Databases"],
)

app.include_router(
    notify.route,
    prefix="/notify",
    tags=["Notify"],
)
