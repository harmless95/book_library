import re
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from sqlalchemy import String, Date, Boolean, Float

from .base import Base

if TYPE_CHECKING:
    from .city_library import Library


class User(Base):

    name: Mapped[str] = mapped_column(String(34), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    year_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str] = mapped_column(String(100), nullable=False)
    scholarship: Mapped[bool] = mapped_column(Boolean, nullable=False)
    average_score: Mapped[float] = mapped_column(Float, nullable=False)

    library_user: Mapped["Library"] = relationship("Library", back_populates="user")

    @validates("email")
    def validates_email(self, key, address):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, address):
            raise ValueError(f"Некорректная электроная почта: {address}")
        return address

    @validates("phone")
    def validates_phone(self, key, number):
        pattern = r"^\+7\d{7,}$"
        if not re.match(pattern, number):
            raise ValueError(f"Некорректный номер телефона: {number}")
        return number

    def to_json(self):
        return {s.name: getattr(self, s.name) for s in self.__table__.columns}
