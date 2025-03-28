from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup

from tgbot.keyboards.base.inline import InlineKeyBoard
from tgbot.lexicon.buttons import KEYBOARDS


class UserInlineKeyboard(InlineKeyBoard):
    pass


class CFactory(CallbackData, prefix="pages", sep="|"):
    name: str
    first: int
    second: int = 0


menu = UserInlineKeyboard(
    *[
        (item[1], CFactory(name=item[0], first=i).pack())
        for i, item in enumerate(KEYBOARDS["menu"].items(), 1)
    ],
)(3)

rates = UserInlineKeyboard(
    *[
        (text, CFactory(name=call, first=1).pack())
        for call, text in KEYBOARDS["rates_kbd"].items()
    ],
)(3)

warehouses = UserInlineKeyboard(
    *[
        (text, CFactory(name=call, first=2).pack())
        for call, text in KEYBOARDS["warehouses_kbd"].items()
    ],
)(3)

settings = UserInlineKeyboard(
    *[
        (text, CFactory(name=call, first=3).pack())
        for call, text in KEYBOARDS["settings_kbd"].items()
    ]
)(2)

api_keys = UserInlineKeyboard(
    *[
        (text, CFactory(name=call, first=3).pack())
        for call, text in KEYBOARDS["api_keys_kbd"].items()
    ]
)(3)

help = UserInlineKeyboard(
    *[
        (text, CFactory(name=call, first=4).pack())
        for call, text in KEYBOARDS["help_kbd"].items()
    ]
)(3)

back = UserInlineKeyboard(
    *[
        (text, CFactory(name=call, first=0).pack())
        for call, text in KEYBOARDS["back_kbd"].items()
    ]
)(1)


def create_list_warehouses(list_warehouses: list) -> InlineKeyboardMarkup:
    """Создание клавиатуры для списка складов"""
    return UserInlineKeyboard(
        *[
            (item["name"], CFactory(name=item["id"], first=2).pack())
            for item in list_warehouses
        ],
        *[
            (text, CFactory(name=call, first=0).pack())
            for call, text in KEYBOARDS["back_kbd"].items()
        ],
    )(1)


kbds = {
    "rates": rates,
    "warehouses": warehouses,
    "settings": settings,
    "help": help,
    "menu": menu,
    "api_keys": api_keys,
}
