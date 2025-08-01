from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from core.models.book import Book


class MixinBook:
    _book_unique: bool = False
    _book_nullable: bool = False
    _book_ondelete: str = False
    _book_back_populates: str | None = None

    @declared_attr
    def book_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("books.id", ondelete=cls._book_ondelete),
            unique=cls._book_unique,
            nullable=cls._book_nullable,
        )

    @declared_attr
    def book(cls) -> Mapped["Book"]:
        return relationship(
            "Book",
            back_populates=cls._book_back_populates,
        )
