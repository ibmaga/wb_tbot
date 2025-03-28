"""название и значение кнопок"""

_back_button = {"back": "Назад"}

KEYBOARDS: dict[str, dict] = {
    "menu": {
        # 'products': 'Продукты',
        "warehouses": "Склады",
        "rates": "Ставки",
        "settings": "Настройки",
        "help": "Помощь",
    },
    "rates_kbd": {
        "view_rates": "Просмотр",
        "charge_rates": "Изменить",
        "automation_rates": "Автоматизация",
        **_back_button,
    },
    "warehouses_kbd": {
        "list_warehouses": "Ваши склады",
        "notice_warehouses": "Уведомление",
        "automation_warehouses": "Автоматизация",
        **_back_button,
    },
    "list_warehouses_kbd": {**_back_button},
    "settings_kbd": {
        "api_keys": "API ключи",
        "frequency": "Частота обновления",
        **_back_button,
    },
    "api_keys_kbd": {"ничего": "nothing", **_back_button},
    "help_kbd": _back_button,
    "back_kbd": _back_button,
}
