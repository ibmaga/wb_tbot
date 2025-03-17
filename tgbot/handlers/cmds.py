from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from tgbot.keyboards.user import menus

router = Router()


@router.message(Command("start"))
async def cmd_menu(message: Message, texts: dict):
    await message.answer(texts["/menu"], reply_markup=menus.menu)
