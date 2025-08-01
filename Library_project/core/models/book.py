from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date

from .base import Base
from .mixins.mixin_author import MixinAuthor
from .mixins.mixin_library import MixinLibrary


class Book(MixinLibrary, MixinAuthor, Base):
    _author_back_populates = "books"
    _library_back_populates = "book"

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    year_of_writing: Mapped[date] = mapped_column(Date)
    count: Mapped[int] = mapped_column(default=1)
    book_genre: Mapped[str] = mapped_column(nullable=False)
    age_recommendation: Mapped[int] = mapped_column(nullable=False)

    def to_json(self):
        return {book.name: getattr(self, book.name) for book in self.__table__.columns}
