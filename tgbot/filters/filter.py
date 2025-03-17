from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsToken(BaseFilter):
    async def __call__(self, callback: CallbackQuery, users_db: dict):
        pass
