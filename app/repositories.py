from uuid import UUID

from sqlalchemy import select

from app.entities import TaskEntity, FileEntity, TypeEntity, StatusEntity
from core import BaseRepository
from core.repositories.base_repository import ModelType


class StatusRepository(BaseRepository):
    model_type = StatusEntity

    async def find_by_code(self, code: str) -> ModelType:
        find_by_code_sql = select(self.model_type).where(self.model_type.code == code)
        return await self.session.scalar(find_by_code_sql)


class TypeRepository(BaseRepository):
    model_type = TypeEntity

    async def find_by_code(self, code: str) -> ModelType:
        find_by_code_sql = select(self.model_type).where(self.model_type.code == code)
        return await self.session.scalar(find_by_code_sql)


class FileRepository(BaseRepository):
    model_type = FileEntity


class TaskRepository(BaseRepository):
    model_type = TaskEntity
