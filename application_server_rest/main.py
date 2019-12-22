from fastapi import FastAPI, Depends, Header, HTTPException
from routes import authenticate, databases, file_providers, module_profiles, modules, users, user_profiles


app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(
    authenticate.route,
    prefix="/authenticate",
    tags=["Authenticate"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


app.include_router(
    modules.route,
    prefix="/modules",
    tags=["Modules"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},

)

app.include_router(
    module_profiles.route,
    prefix="/module-profiles",
    tags=["Module Profiles"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    users.route,
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    user_profiles.route,
    prefix="/user-profiles",
    tags=["User Profiles"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    file_providers.route,
    prefix="/file-providers",
    tags=["File Providers"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}, 405: {"description": "Not found"}},
)

app.include_router(
    databases.route,
    prefix="/databases",
    tags=["Databases"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
