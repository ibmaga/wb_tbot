from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings

engine = create_async_engine(url=settings.db_url, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


"""
from typing import Any

user_db = {
    "tokens": {
        "analytics": None,
        "statistics": None,
        "promotion": None,
    },
    # 'products': [],
    "username": None,
    "banned": False,
    "access": False,
}
users_db: dict[str, Any] = {}
"""
