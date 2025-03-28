from typing import Any, Callable, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject, User, CallbackQuery

from services.user_service import UserService
from services.wb_service import WildberriesService
from tgbot.keyboards.user.menus import back, CFactory
from utils.wb_api.wb_api import WildberriesAPI
from tgbot.states import UserState


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


# Сохранение предыдущих состояний клавиатуры для последующих возвращений
class History(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any],
    ):
        state: FSMContext = data["state"]
        history: list = (await state.get_data()).get("history", [])
        key: str = CFactory.unpack(event.data).name
        print(event)

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
        event: CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        texts = data["texts"]
        user_service: UserService = data["user_service"]
        user_id = event.from_user.id
        state: FSMContext = data["state"]
        wb_token = await user_service.get_api_token(
            user_id=user_id, type_token="supplies"
        )

        # написать функцию, которая будет показывать сообщение про то что нужно отправить api token или "у вас нет api token"

        try:
            wb_service = WildberriesService(wb_api=WildberriesAPI(api_token=wb_token))
            await wb_service.validated_token()
            data["wb_service"] = wb_service
            return await handler(event, data)
        except Exception as e:
            error_text = f"Ошибка API: {e}\nПожалуйста, обновите API ключ."
            await event.message.edit_text(text=error_text, reply_markup=back)
            await state.set_state(UserState.send_token)
            print(e)
            return
