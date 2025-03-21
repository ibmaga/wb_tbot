from typing import TypeVar, Generic, Type, Optional

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseDAO(Generic[ModelType]):
    model: Type[ModelType] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **data) -> ModelType:
        stmt = insert(self.model).values(**data).on_conflict_do_nothing()
        await self.session.execute(stmt)
        result = self.model(**data)
        await self.session.commit()
        return result

    async def get(self, id: int) -> Optional[ModelType]:
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, id: int, **data) -> Optional[ModelType]:
        stmt = update(self.model).where(self.model.id == id).values(**data)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def delete(self, id: int) -> Optional[ModelType]:
        instance = await self.get(id)
        if instance:
            await self.session.delete(instance)
            await self.session.commit()
        return instance
