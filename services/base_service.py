from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from utils.wb_api.wb_api import WildberriesAPI


class BaseService:
    def __init__(self, session: Optional[AsyncSession] = None):
        self._session = session
