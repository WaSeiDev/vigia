from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.base import Base


class Categories(Base):
    __tablename__ = "categories"
    name: Mapped[str]
    expenses: Mapped[list["Expenses"]] = relationship(back_populates="category")

    home_id: Mapped[int | None] = mapped_column(ForeignKey("homes.id"))
    home: Mapped["Homes | None"] = relationship(back_populates="categories")

    __table_args__ = (
        UniqueConstraint(
            "name",
            "home_id",
            name="uq_categories_name_home_id",
        ),
    )

