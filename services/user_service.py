from sqlalchemy.ext.asyncio import AsyncSession

from db.dao.users import UserDAO
from db.models.users import User
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.user_dao = UserDAO(session)

    async def create_user(
        self,
        user_id: int,
        username: str,
        full_name: str,
    ) -> User:
        user = await self.user_dao.create(
            user_id=user_id,
            username=username,
            full_name=full_name,
        )
        return user
