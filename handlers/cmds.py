from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards.user import menus

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, texts: dict):
    await message.answer(texts["/start"])


@router.message(Command("help"))
async def cmd_help(message: Message, texts: dict):
    await message.answer(texts["/help"])


@router.message(Command("menu"))
async def cmd_menu(message: Message, texts: dict):
    await message.answer(texts["/menu"], reply_markup=menus.menu)
