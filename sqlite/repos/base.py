from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sqlite.database import Base


class BaseRepository:
    def __init__(self, model, session):
        self.model = model
        self.session = session

    async def get(self, obj_id):
        return await self.session.get(self.model, obj_id)

    async def get_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, data: dict):
        db_obj = self.model(**data)
        self.session.add(db_obj)
        await self.session.flush()
        return db_obj

    async def update(self, db_obj, update_data):
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
        self.session.add(db_obj)
        await self.session.flush()
        return db_obj

    async def delete(self, db_obj):
        await self.session.delete(db_obj)
        await self.session.flush()
