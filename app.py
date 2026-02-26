from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.categories import categories_router
from api.users import users_router
from api.locations import locations_router


def create_app():
    app = FastAPI(root_path="/api/v1")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(categories_router, prefix="/categories")
    app.include_router(users_router, prefix="/users")
    app.include_router(locations_router, prefix="/locations")
    return app
