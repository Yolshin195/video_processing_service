from sqlalchemy.orm import Mapped

from .base_entity import BaseEntity


class BaseReferenceEntity(BaseEntity):
    __abstract__ = True

    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


    