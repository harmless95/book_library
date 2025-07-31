from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, String

from .base import Base

if TYPE_CHECKING:
    from .librarian import Librarian


class Library(Base):
    name_library: Mapped[str] = mapped_column(String(150), nullable=False)
    date_of_issue: Mapped[Date] = mapped_column(Date)
    date_of_return: Mapped[Date] = mapped_column(Date)
    # librarian_work_schedule: Mapped["Librarian"] =
