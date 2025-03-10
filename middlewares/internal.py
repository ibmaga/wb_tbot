from typing import Any, Callable, Awaitable, Dict
from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, User, Chat, Update
from aiogram.fsm.context import FSMContext


# проверка на наличие API ключа // временно не используется
class IsToken(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user: User = data['event_from_user']
        chat: Chat = data['event_chat']
        bot: Bot = data['bot']
        update: Update = data['event_update']
        token = data['users_db'][str(user.id)]['tokens'][event.data]

        if token is not None:
            return await handler(event, data)

        await bot.answer_callback_query(callback_query_id=update.callback_query.id, text='')
        await bot.send_message(chat_id=chat.id, text=data['lexicon']['send_token'])


# Сохранение предыдущих состояний клавиатуры для последующих возвращений
class History(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        state: FSMContext = data['state']
        history: list = (await state.get_data()).get('history', [])
        key: str = event.data.split('|')[1]

        # добавляем меню в начало
        keyboard = {
            'lexicon_key': '/menu',
            'keyboard': 'menu'
        }
        if keyboard not in history:
            history.append(keyboard)

        if key != 'back':
            keyboard = {
                'lexicon_key': key,
                'keyboard': key
            }

            if keyboard not in history:
                history.append(keyboard)

            await state.update_data(history=history)
        result = await handler(event, data)

        return result
