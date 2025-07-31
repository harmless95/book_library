from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date

from .base import Base

if TYPE_CHECKING:
    from .book import Book


class Author(Base):
    name: Mapped[str] = mapped_column(String(34), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    year_of_birth: Mapped[Date] = mapped_column(Date)
    age_recommendation: Mapped[int] = mapped_column(nullable=False)

    books: Mapped[list["Book"]] = mapped_column()
