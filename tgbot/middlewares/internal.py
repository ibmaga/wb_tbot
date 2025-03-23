from typing import Any, Callable, Awaitable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject, User, Chat, Update, CallbackQuery, Message

from services.user_service import UserService
from services.wb_service import WildberriesService
from utils.wb_api.wb_api import WildberriesAPI


class SaveUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data["event_from_user"]
        user_service: UserService = data["user_service"]
        await user_service.user_dao.create(
            user_id=user.id,
            username=user.username,
            full_name=user.full_name,
        )
        return await handler(event, data)


# проверка на наличие API ключа // временно не используется
class IsToken(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data["event_from_user"]
        chat: Chat = data["event_chat"]
        bot: Bot = data["bot"]
        update: Update = data["event_update"]
        token = data["users_db"][str(user.id)]["tokens"][event.data]

        if token is not None:
            return await handler(event, data)

        await bot.answer_callback_query(
            callback_query_id=update.callback_query.id, text=""
        )
        await bot.send_message(chat_id=chat.id, text=data["lexicon"]["send_token"])


# Сохранение предыдущих состояний клавиатуры для последующих возвращений
class History(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any],
    ):
        state: FSMContext = data['state']
        history: list = (await state.get_data()).get('history', [])
        key: str = event.data.split('|')[1]

        # добавляем меню в начало
        keyboard = {"lexicon_key": "/menu", "keyboard": "menu"}
        if keyboard not in history:
            history.append(keyboard)

        if key != "back":
            keyboard = {"lexicon_key": key, "keyboard": key}

            if keyboard not in history:
                history.append(keyboard)

            await state.update_data(history=history)
        result = await handler(event, data)

        return result


class WildberriesMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        user_service = data["user_service"]
        user_id = event.from_user.id
        wb_token = await user_service.get_wb_token(user_id)

        if wb_token:
            wb_api = WildberriesAPI(api_token=wb_token)
            wb_service = WildberriesService(wb_api=wb_api)
            data["wb_service"] = wb_service

        return await handler(event, data)
