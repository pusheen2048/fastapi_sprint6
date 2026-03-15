from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.users import user_router


def create_app():
    app = FastAPI(root_path="/api/v1")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(user_router, prefix="/users")
    return app
