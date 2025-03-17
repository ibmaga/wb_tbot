"""название и значение кнопок"""

KEYBOARDS: dict[str, dict] = {
    "menu": {
        # 'products': 'Продукты',
        "rates": "Ставки",
        "warehouses": "Склады",
        "settings": "Настройки",
        "help": "Помощь",
    },
    # 'products_kbd': {
    #     'send_index': 'Отправить артикул',
    #     'back': 'Назад',
    # },
    # 'send_index_kbd': {
    #     'back': 'Назад'
    # },
    "rates_kbd": {
        "view_rates": "Просмотр",
        "charge_rates": "Изменить",
        "automation_rates": "Автоматизация",
        "back": "Назад",
    },
    "warehouses_kbd": {
        "view_warehouses": "Просмотр",
        "notice_warehouses": "Уведомление",
        "automation_warehouses": "Автоматизация",
        "back": "Назад",
    },
    "view_warehouses_kbd": {"back": "Назад"},
    "settings_kbd": {
        "api_keys": "API ключи",
        "frequency": "Частота обновления",
        "back": "Назад",
    },
    "api_keys_kbd": {"back": "Назад"},
    "help_kbd": {"back": "Назад"},
}
