import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis

from logger.logger import logger
from configs.config import settings
from handlers import cmds, menu_proc
from keyboards import set_main_menu
from middlewares import AddUser, History


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

    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)


asyncio.run(main())
