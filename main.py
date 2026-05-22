import asyncio
import logging

import uvicorn

from app import create_app
from sqlite.database import Base, database

app = create_app()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=database._engine)


async def run():
    config = uvicorn.Config("main:app", host="0.0.0.0",
                            port=8000, reload=False)
    server = uvicorn.Server(config=config)
    tasks = (asyncio.create_task(server.serve()), )
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
