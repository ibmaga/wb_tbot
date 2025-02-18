from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from configs.config import settings

engine = create_async_engine(url=settings.db_url, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


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
