from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards import create_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, lexicon: dict):
    await message.answer(lexicon['/start'])


@router.message(Command('help'))
async def cmd_help(message: Message, lexicon: dict):
    await message.answer(lexicon['/help'])


@router.message(Command('menu'))
async def cmd_menu(message: Message, lexicon: dict):
    await message.answer(lexicon['/menu'], reply_markup=create_menu())
