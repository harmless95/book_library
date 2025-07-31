from typing import TYPE_CHECKING
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date

from .base import Base

if TYPE_CHECKING:
    from .author import Author


class Book(Base):
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    year_of_writing: Mapped[date] = mapped_column(Date)
    count: Mapped[int] = mapped_column(default=1)
    book_genre: Mapped[str] = mapped_column(nullable=False)

    author: Mapped["Author"] = mapped_column(ForengeKey)
