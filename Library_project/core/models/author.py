from typing import TYPE_CHECKING
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date

from .base import Base

if TYPE_CHECKING:
    from .book import Book


class Author(Base):
    name: Mapped[str] = mapped_column(String(34), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    year_of_birth: Mapped[date] = mapped_column(Date, nullable=False)

    books: Mapped[list["Book"]] = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Год рождения: {self.year_of_birth}"

    def to_json(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
