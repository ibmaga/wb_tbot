from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from lexicon.lexicon import BUTTONS


class CFactory(CallbackData, prefix='pages', sep='|'):
    name: str
    first: int
    second: int = 0
    third: int = 0


inline = InlineKeyboardButton


# меню для доступа к возможностям
def create_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    for i, item in enumerate(BUTTONS['menu'].items(), 1):
        key, value = item
        keyboard.add(
            inline(text=value, callback_data=CFactory(name=key, first=i).pack())
        )

    return keyboard.adjust(3, 1).as_markup()


# создание разделов в продукты
# def create_products(products: list[str | int] | None = None) -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardBuilder()
#
#     if products is not None:
#         for i, value in enumerate(products, 1):
#             keyboard.row(
#                 inline(text=value, callback_data=CFactory(name=value, first=1, second=i).pack()),
#                 width=1
#             )
#
#     for i, item in enumerate(BUTTONS['products_kbd'].items(), len(products) + 1 if products else 1):
#         key, value = item
#         keyboard.row(
#             inline(text=value, callback_data=CFactory(name=key, first=1, second=i).pack()),
#             width=1
#         )
#
#     return keyboard.as_markup()
#
# def create_send_index():
#     keyboard = InlineKeyboardBuilder()
#
#     keyboard.row(inline(text=BUTTONS['send_index_kbd']['back'],
#                         callback_data=CFactory(name='back', first=1, second=1, third=1).pack()))
#     return keyboard.as_markup()
#

def create_rates():
    keyboard = InlineKeyboardBuilder()
    for key, value in BUTTONS['rates_kbd'].items():
        keyboard.add(
            inline(text=value, callback_data=CFactory(name=key, first=1).pack())
        ).adjust(3, 1)
    return keyboard.as_markup()


def create_warehouses():
    keyboard = InlineKeyboardBuilder()
    for key, value in BUTTONS['warehouses_kbd'].items():
        keyboard.row(
            inline(text=value, callback_data=CFactory(name=key, first=2).pack())
        ).adjust(3, 1)
    return keyboard.as_markup()


def create_view_warehouses():
    keyboard = InlineKeyboardBuilder()
    for key, value in BUTTONS['view_warehouses_kbd'].items():
        keyboard.row(
            inline(text=value, callback_data=CFactory(name=key, first=2).pack())
        )
    return keyboard.as_markup()


def create_settings():
    keyboard = InlineKeyboardBuilder()
    for key, value in BUTTONS['settings_kbd'].items():
        keyboard.row(
            inline(text=value, callback_data=CFactory(name=key, first=3).pack()),
            width=1
        )
    return keyboard.as_markup()


def create_api_keys_kbd():
    keyboard = InlineKeyboardBuilder()
    for key, value in BUTTONS['api_keys_kbd'].items():
        keyboard.row(
            inline(text=value, callback_data=CFactory(name=key, first=3).pack()),
        )
    return keyboard.as_markup()


# создание раздела "помощь"
def create_help() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    for key, value in BUTTONS['help_kbd'].items():
        keyboard.row(
            inline(text=value, callback_data=CFactory(name=key, first=4).pack()),
            width=1
        )

    return keyboard.as_markup()


kbds = {
    'rates': create_rates,
    'warehouses': create_warehouses,
    'settings': create_settings,
    'help': create_help,
    'menu': create_menu,
    'api_keys': create_api_keys_kbd,
}
