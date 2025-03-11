from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.user import menus
from services.responses import super_find_value

router = Router()


# class FSM(StatesGroup):
#     history = State()

# нужно написать: проверку на наличие токена вб, проверка на правильность токена,
# обработки на ошибки апи вб
# @router.callback_query(CFactory.filter('products' == F.name))
# async def products(callback: CallbackQuery, texts: dict, users_db: dict):
#     await callback.message.edit_text(
#         text=texts['products'],
#         reply_markup=create_products(users_db[str(callback.message.chat.id)]['products'])
#     )
#
#
# @router.callback_query(CFactory.filter('send_index' == F.name))
# async def send_index(callback: CallbackQuery, state: FSMContext, texts: dict):
#     await callback.message.edit_text(
#         text=texts['send_index'],
#         reply_markup=create_send_index()
#     )
#     await state.set_state(FSM.fill_index)


# сделать проверку через внутренний middleware, на наличие нужного токена
@router.callback_query(menus.CFactory.filter("rates" == F.name))
async def rates(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(text=texts["rates"], reply_markup=menus.rates)


@router.callback_query(menus.CFactory.filter("warehouses" == F.name))
async def warehouses(callback: CallbackQuery, texts: dict):
    await callback.message.edit_text(
        text=texts["warehouses"], reply_markup=menus.warehouses
    )


@router.callback_query(menus.CFactory.filter("view_warehouses" == F.name))
async def view_warehouses(callback: CallbackQuery, view_warehouses_lexicon: dict):
    await callback.message.edit_text(
        text="\n".join(
            [
                f"{text} - {super_find_value(k)}"
                for k, text in view_warehouses_lexicon.items()
            ]
        ),
        reply_markup=menus.view_warehouses,
    )


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


# сделать callback_data, для проверки в каком месте кнопок находиться данный момент, чтобы потом можно было с помощью
# кнопки "назад" вернуться на предыдущую состоянию кнопок
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
