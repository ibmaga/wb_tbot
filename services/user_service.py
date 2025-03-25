from sqlalchemy.ext.asyncio import AsyncSession

from db.dao.api_tokens import APITokenDAO
from db.dao.users import UserDAO
from db.models.users import User, APIToken
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.user_dao = UserDAO(session)
        self.api_token_dao = APITokenDAO(session)

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

    async def get_api_token(self, user_id: int, type_token: str) -> str | None:
        api_tokens: APIToken = await self.api_token_dao.get_api_tokens_by_user_id(
            user_id
        )
        if api_tokens:
            return getattr(api_tokens, type_token)
