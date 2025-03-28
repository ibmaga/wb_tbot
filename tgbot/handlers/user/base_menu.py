from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from services.user_service import UserService
from services.wb_service import WildberriesService
from tgbot.keyboards.user import menus
from tgbot.states import UserState

router = Router()


@router.message(UserState.send_token)
async def send_token(
    message: Message,
    texts: dict,
    user_service: UserService,
    wb_service: WildberriesService,
):
    user_id = message.from_user.id
    await user_service.update_api_token(user_id, "supplies", message.text)
    # try:
    #     wb_service.validated_token()
    # except Exception:
    #     pass
    """
    сделать так чтобы когда пользователь отправляет токен и
    он сам определялся к какому категорию оно относиться(декодировать токен),
    автоматически записывался свою колонку в дб
    """


@router.callback_query(menus.CFactory.filter("warehouses" == F.name))
async def warehouses(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(
        text=texts["warehouses"], reply_markup=menus.warehouses
    )


@router.callback_query(menus.CFactory.filter("rates" == F.name))
async def rates(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(text=texts["rates"], reply_markup=menus.rates)


@router.callback_query(menus.CFactory.filter("settings" == F.name))
async def settings(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(
        text=texts["settings"], reply_markup=menus.settings
    )


@router.callback_query(menus.CFactory.filter("api_keys" == F.name))
async def api_keys(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(
        text=texts["api_keys"], reply_markup=menus.api_keys
    )


@router.callback_query(menus.CFactory.filter("help" == F.name))
async def helps(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(text=texts["help"], reply_markup=menus.help)


@router.callback_query(menus.CFactory.filter("back" == F.name))
async def back(callback_query: CallbackQuery, state: FSMContext, texts: dict):
    data: dict = await state.get_data()
    history: list = data.get("history", [])

    if history and len(history) > 1:
        # Убираем последний элемент из истории и используем предпоследний
        history.pop()
        previous_state = history[-1]
        await state.update_data(history=history)

        await callback_query.message.edit_text(
            text=texts[previous_state["lexicon_key"]],
            reply_markup=menus.kbds[previous_state["keyboard"]],
        )

    else:
        # Если история пуста, возвращаемся в главное меню
        await callback_query.message.edit_text(
            text=texts["/menu"], reply_markup=menus.menu
        )
