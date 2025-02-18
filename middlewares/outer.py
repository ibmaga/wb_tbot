from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from db.database import user_db
from lexicon.lexicon import LEXICON, VIEW_WAREHOUSES


class AddUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        data["lexicon"] = LEXICON
        data["view_warehouses_lexicon"] = VIEW_WAREHOUSES

        user: User = data["event_from_user"]

        if "users_db" not in data:
            data["users_db"] = {}

        # сохранение данных пользователя
        data["users_db"][str(user.id)] = data.get(str(user.id), user_db)
        return await handler(event, data)
