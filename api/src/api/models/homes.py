from sqlalchemy.orm import Mapped, relationship

from api.models.base import Base


class Homes(Base):
    __tablename__ = "homes"
    name: Mapped[str]
    users: Mapped[list["Users"]] = relationship(back_populates="home")
    categories: Mapped[list["Categories"]] = relationship(back_populates="home")
