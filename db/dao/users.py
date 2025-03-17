from sqlalchemy import select

from db.dao.base import BaseDAO
from db.models.users import User


class UserDAO(BaseDAO):
    model = User

    async def create_user(self, user):
        user = User(**user)
        self.session.add(user)

        await self.session.commit()
        return user

    async def get_user_by_user_id(self, user_id: int):
        smt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(smt)
        return result.scalar_one_or_none()
