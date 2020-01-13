from fastapi import FastAPI, Depends, Header, HTTPException
from routes import authenticate, databases, file_providers, module_profiles, modules, users, user_profiles, tasks, \
                   notify, update_client_data, client_app, configuration


app = FastAPI()


async def get_token_header(session_token: str = Header(...)):
    if session_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="Session-Token invalid")

app.include_router(
    authenticate.route,
    prefix="/authenticate",
    tags=["Authenticate"],
    responses={
        401: {"description": "You don't have the permission to do this."},
        405: {"description": "Wrong username or password"}
    },
)


app.include_router(
    modules.route,
    prefix="/modules",
    tags=["Modules"],
    responses={
        401: {"description": "You don't have the permission to do this."},
        404: {"description": "Module not found."},
    },

)

app.include_router(
    module_profiles.route,
    prefix="/module-profiles",
    tags=["Module Profiles"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
        404: {"description": "Module profile not found."}
    },
)

app.include_router(
    users.route,
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
        404: {"description": "User not found."}
    },
)

app.include_router(
    user_profiles.route,
    prefix="/user-profiles",
    tags=["User Profiles"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
        404: {"description": "User profile not found."}
    },
)

app.include_router(
    file_providers.route,
    prefix="/file-providers",
    tags=["File Providers"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
        404: {"description": "File provider not found."}
    },
)

app.include_router(
    databases.route,
    prefix="/databases",
    tags=["Databases"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
    },
)

app.include_router(
    tasks.route,
    prefix="/tasks",
    tags=["Tasks"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
    },
)

app.include_router(
    notify.route,
    prefix="/notify",
    tags=["Notify"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
    },
)

app.include_router(
    update_client_data.route,
    prefix="/update",
    tags=["Update client data"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
    },
)

app.include_router(
    client_app.route,
    prefix="/client-app",
    tags=["ClientApp"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
    },
)

app.include_router(
    configuration.route,
    prefix="/configuration",
    tags=["Configuration"],
    dependencies=[Depends(get_token_header)],
    responses={
        401: {"description": "You don't have the permission to do this."},
    },
)
