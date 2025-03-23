from .base_service import BaseService
from utils.wb_api.wb_api import WildberriesAPI


class WildberriesService(BaseService):
    def __init__(self, wb_api: WildberriesAPI = None):
        super().__init__()
        self._wb_api = wb_api
        if not self._wb_api:
            raise ValueError(
                "WildberriesAPI instance is required for WildberriesService"
            )
