from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    """Функция для установки основного меню бота"""
    menu = [
        BotCommand(command="/start", description="Запуск"),
        # BotCommand(command="/menu", description="Меню"),
        # BotCommand(command="/help", description="Справка"),
    ]

    await bot.set_my_commands(menu)
