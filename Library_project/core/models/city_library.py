from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey

from .base import Base

if TYPE_CHECKING:
    from .book import Book
    from .librarian import Librarian


class Library(Base):
    id_book: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date_issue: Mapped[Date] = mapped_column(Date)
    date_return: Mapped[Date] = mapped_column(Date)
    # librarians: Mapped["Librarian"] = relationship(
    #     "Librarian",
    #     back_populates="library",
    #     cascade="all, delete-orphan",
    #     passive_deletes=True,
    # )
    book: Mapped["Book"] = relationship("Book", back_populates="library")
    user = relationship("users", back_populates="library_user")

    def __repr__(self):
        return (
            f"Книга: {self.id_book},"
            f"Студент: {self.id_user},"
            f"Дата выдачи: {self.date_issue},"
            f"Дата возврата: {self.date_return},"
            f"Кол-во дней, который держал/держит читатель: {self.count_date_book()}"
        )

    def count_date_book(self):
        if self.date_return:
            return (self.date_return - self.date_issue).days
        else:
            return (datetime.now() - self.date_issue).days

    def to_json(self):
        return {
            "id": self.id,
            "id_book": self.id_book,
            "id_user": self.id_user,
            "date_issue": self.date_issue,
            "date_return": self.date_return,
            "count_date_book": self.count_date_book(),
        }
