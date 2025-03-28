class WildberriesURLs:
    """URL-адреса API Wildberries"""

    # Базовые URL для API
    BASE_MARKETPLACE = "https://marketplace-api.wildberries.ru"
    BASE_SUPPLIES = "https://suppliers-api.wildberries.ru"

    # получить список складов продавца - get
    LIST_WAREHOUSES = f"{BASE_MARKETPLACE}/api/v3/warehouses"

    # получить остатки товаров - post - {warehouseId}
    STOCKS = f"{BASE_MARKETPLACE}/api/v3/stocks/"

    # проверка подключение или валидация
    PING = f"{BASE_MARKETPLACE}/ping"

    # список складов
    LIST_WAREHOUSES_OTH = f"{BASE_SUPPLIES}/api/v1/warehouses"

    # # URL для работы с каталогом
    # CATALOG = f"{BASE_MARKETPLACE}/content/v1/cards"
    #
    # # URL для работы с поставками
    # SUPPLIES = f"{BASE_MARKETPLACE}/api/v2/supplies"
    #
    # # URL для работы с остатками
    # STOCKS = f"{BASE_MARKETPLACE}/api/v2/stocks"
    #
    # # URL для работы с заказами
    # ORDERS = f"{BASE_MARKETPLACE}/api/v3/orders"
    #
    # # URL для получения статистики
    # STATISTICS = f"{BASE_MARKETPLACE}/analytics/v1/supplier/sales"
