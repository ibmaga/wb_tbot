from typing import TypeVar, Generic, Type, Optional, Any
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import Select, Update

from db.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseDAO(Generic[ModelType]):
    model: Type[ModelType] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **data) -> ModelType:
        instance = self.model(**data)
        await self.session.merge(instance)
        await self.session.commit()
        return instance

    async def get(self, id: int) -> Optional[ModelType]:
        stmt: Select = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, id: int, **data) -> Optional[ModelType]:
        stmt: Update = update(self.model).where(self.model.id == id).values(**data)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def delete(self, id: int) -> Optional[ModelType]:
        instance = await self.get(id)
        if instance:
            await self.session.delete(instance)
            await self.session.commit()
        return instance
