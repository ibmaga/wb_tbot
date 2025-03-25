from sqlalchemy import select, update

from db.dao.base import BaseDAO
from db.models.users import APIToken


class APITokenDAO(BaseDAO[APIToken]):
    model = APIToken

    async def get_api_tokens_by_user_id(self, user_id: int) -> model | None:
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_api_token_by_user_id(self, user_id: int, **data) -> model | None:
        stmt = update(self.model).where(self.model.user_id == user_id).values(**data)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()
