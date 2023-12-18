from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.constants import StatusEnum, TypeEnum
from core import BaseEntity, BaseReferenceEntity


class StatusEntity(BaseReferenceEntity):
    __tablename__ = "status_entity"

    @property
    def status_enum(self):
        return StatusEnum(self.code)


class TypeEntity(BaseReferenceEntity):
    __tablename__ = "type_entity"

    @property
    def type_enum(self):
        return TypeEnum(self.code)


class FileEntity(BaseEntity):
    __tablename__ = "file_entity"

    name: Mapped[str]


class TaskEntity(BaseEntity):
    __tablename__ = "task_entity"

    file_source_url: Mapped[str | None]

    status_id: Mapped[UUID] = mapped_column(ForeignKey("status_entity.id"))
    status: Mapped["StatusEntity"] = relationship(foreign_keys=status_id, lazy="joined")

    type_id: Mapped[UUID] = mapped_column(ForeignKey("type_entity.id"))
    type: Mapped["TypeEntity"] = relationship(foreign_keys=type_id, lazy="joined")

    input_file_id: Mapped[UUID | None] = mapped_column(ForeignKey("file_entity.id"))
    input_file: Mapped["FileEntity"] = relationship(
        foreign_keys=input_file_id, lazy="joined"
    )

    output_file_id: Mapped[UUID | None] = mapped_column(ForeignKey("file_entity.id"))
    output_file: Mapped["FileEntity"] = relationship(
        foreign_keys=output_file_id, lazy="joined"
    )
