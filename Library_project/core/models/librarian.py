from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, String

from .base import Base
from .mixins.mixin_library import MixinLibrary


class Librarian(MixinLibrary, Base):
    _library_back_populates = "librarians"

    name: Mapped[str] = mapped_column(String(34), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    year_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    salary: Mapped[int] = mapped_column(nullable=False)
