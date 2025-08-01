from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey


if TYPE_CHECKING:
    from core.models.city_library import Library


class MixinLibrary:
    _library_unique: bool = False
    _library_nullable: bool = False
    _library_ondelete: str = False
    _library_back_populates: str | None = None

    @declared_attr
    def library_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("librarys.id", ondelete=cls._library_ondelete),
            nullable=cls._library_nullable,
            unique=cls._library_unique,
        )

    @declared_attr
    def library(cls) -> Mapped["Library"]:
        return relationship(
            "Library",
            back_populates=cls._library_back_populates,
        )
