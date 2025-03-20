import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis

from core.config import settings
from core.logger import get_logger
from db.setup import async_session
from tgbot.handlers import commands
from tgbot.handlers.user import menu
from tgbot.keyboards import default_menu
from tgbot.lexicon.lexicon import TEXTS
from tgbot.middlewares import SaveUser, History, DbSessionMiddleware, TextsMiddleware


redis = Redis()
storage = RedisStorage(redis=redis)


async def main():
    dp = Dispatcher()
    bot = Bot(
        settings.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logger = get_logger(__name__)
    dp.include_routers(commands.router, menu.router)

    menu.router.callback_query.middleware(History())
    commands.router.message.middleware(SaveUser())
    dp.update.outer_middleware(DbSessionMiddleware(async_session))
    dp.update.outer_middleware(TextsMiddleware(TEXTS))

    dp.startup.register(default_menu.set_main_menu)
    await dp.start_polling(bot)


asyncio.run(main())
