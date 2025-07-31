from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, String

from .base import Base


class Librarian(Base):
    name: Mapped[str] = mapped_column(String(34), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    year_of_birth: Mapped[Date] = mapped_column(Date)
    salary: Mapped[int] = mapped_column(nullable=False)
