from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.base import Base


class Users(Base):
    __tablename__ = "users"
    name: Mapped[str]
    telegram_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    home_id: Mapped[int] = mapped_column(ForeignKey("homes.id"))
    home: Mapped["Homes"] = relationship(back_populates="users")

    expenses: Mapped[list["Expenses"]] = relationship(back_populates="user")
