class WildberriesURLs:
    """URL-адреса API Wildberries"""

    # Базовый URL для API
    BASE = "https://marketplace-api.wildberries.ru"

    # получить список складов продавца - get
    LIST_WAREHOUSES = f"{BASE}/api/v3/warehouses"

    # получить остатки товаров - post - {warehouseId}
    STOCKS = f"{BASE}/api/v3/stocks/"

    # # URL для работы с каталогом
    # CATALOG = f"{BASE}/content/v1/cards"
    #
    # # URL для работы с поставками
    # SUPPLIES = f"{BASE}/api/v2/supplies"
    #
    # # URL для работы с остатками
    # STOCKS = f"{BASE}/api/v2/stocks"
    #
    # # URL для работы с заказами
    # ORDERS = f"{BASE}/api/v3/orders"
    #
    # # URL для получения статистики
    # STATISTICS = f"{BASE}/analytics/v1/supplier/sales"
