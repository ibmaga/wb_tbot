from .base_service import BaseService
from utils.wb_api.wb_api import WildberriesAPI


class WildberriesService(BaseService):
    def __init__(self, wb_api: WildberriesAPI):
        super().__init__()
        self._wb_api = wb_api

    async def validated_token(self):
        try:
            return await self._wb_api.validated_token()
        except Exception:
            raise

    async def get_list_warehouses(self):
        return await self._wb_api.get_list_warehouses()

    async def get_stocks(self, warehouse_id: int):
        return await self._wb_api.get_stocks(warehouse_id)

    async def get_list_warehouses_oth(self):
        return await self._wb_api.get_list_warehouses_oth()
