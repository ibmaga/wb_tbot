import aiohttp
from typing import Dict, Any, Optional
from utils.wb_api.urls import WildberriesURLs


class WildberriesAPI:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = {"Authorization": api_token, "Content-Type": "application/json"}

    async def _make_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Выполняет запрос к API Wildberries

        Args:
            method: Метод запроса (GET, POST, PUT, DELETE)
            url: URL запроса
            params: Параметры запроса
            data: Данные для отправки в теле запроса

        Returns:
            Dict[str, Any]: Ответ от API
        """
        async with aiohttp.ClientSession() as session:
            request_method = getattr(session, method.lower())
            async with request_method(
                url, headers=self.headers, params=params, json=data
            ) as response:
                if response.status >= 400:
                    error_text = await response.text()
                    raise Exception(f"API Error: {response.status} - {error_text}")
                return await response.json()
