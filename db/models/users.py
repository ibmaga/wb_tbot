from sqlalchemy import BIGINT, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import Base, TimeStampMixin, TableNameMixin


class User(Base, TableNameMixin, TimeStampMixin):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, nullable=False
    )
    user_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=True)
    access: Mapped[bool] = mapped_column(default=False, nullable=False)
    banned: Mapped[bool] = mapped_column(default=False, nullable=False)

    def __repr__(self):
        return f"<User {self.user_id} {self.username} {self.access}>"
