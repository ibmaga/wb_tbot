import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis

from core.config import settings
from core.logger import get_logger
from db.setup import async_session
from tgbot.handlers.commands import router as commands_router
from tgbot.handlers.user.base_menu import router as user_router
from tgbot.handlers.user.internal_menu import router as internal_menu_router
from tgbot.keyboards import default_menu
from tgbot.lexicon.lexicon import TEXTS
from tgbot.middlewares import (
    SaveUser,
    History,
    DbSessionMiddleware,
    TextsMiddleware,
    WildberriesMiddleware,
)

redis = Redis()
storage = RedisStorage(redis=redis)


async def main():
    dp = Dispatcher()
    bot = Bot(
        settings.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logger = get_logger(__name__)
    dp.include_routers(commands_router, user_router, internal_menu_router)

    dp.update.outer_middleware(DbSessionMiddleware(async_session))
    dp.update.outer_middleware(TextsMiddleware(TEXTS))
    commands_router.message.middleware(SaveUser())
    user_router.callback_query.middleware(History())
    internal_menu_router.callback_query.middleware(WildberriesMiddleware())

    dp.startup.register(default_menu.set_main_menu)
    await dp.start_polling(bot)


asyncio.run(main())
