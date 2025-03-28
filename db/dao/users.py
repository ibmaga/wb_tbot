from sqlalchemy import select, update

from db.dao.base import BaseDAO
from db.models.users import User


class UserDAO(BaseDAO[User]):
    model = User

    async def get_user_by_user_id(self, user_id: int) -> model:
        smt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(smt)
        return result.scalar_one_or_none()

    async def update_user_by_user_id(self, user_id: int, **data) -> model:
        stmt = update(self.model).where(self.model.user_id == user_id).values(**data)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()
