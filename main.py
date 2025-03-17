import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis

from core.config import settings
from tgbot.handlers import cmds, menu_proc
from tgbot.keyboards import base_menu
from tgbot.middlewares import AddUser, History


redis = Redis()
storage = RedisStorage(redis=redis)


async def main():
    dp = Dispatcher()
    bot = Bot(
        settings.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp.include_routers(cmds.router, menu_proc.router)

    dp.update.outer_middleware(AddUser())
    menu_proc.router.callback_query.middleware(History())

    dp.startup.register(base_menu.set_main_menu)
    await dp.start_polling(bot)


asyncio.run(main())
