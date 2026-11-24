from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.base import Base


class Expenses(Base):
    __tablename__ = "expenses"
    amount: Mapped[Decimal] = mapped_column(Numeric(19, 4))
    currency: Mapped[str] = mapped_column(String(3))
    description: Mapped[str | None] = mapped_column(nullable=True)
    expense_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    user: Mapped["Users"] = relationship(back_populates="expenses")
    category: Mapped["Categories"] = relationship(back_populates="expenses")