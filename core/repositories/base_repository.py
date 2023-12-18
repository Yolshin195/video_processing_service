from typing import TypeVar, Sequence, Type, AsyncIterator
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.entities import BaseEntity

# Объявляем тип-параметр ModelType, который будет использоваться для моделей
ModelType = TypeVar("ModelType", bound=BaseEntity)


class BaseRepository:
    model_type: Type[ModelType] = NotImplementedError

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_all(
        self, skip: int = 0, limit: int = 100
    ) -> AsyncIterator[model_type]:
        find_all_sql = select(self.model_type).offset(skip).limit(limit)
        stream = await self.session.stream_scalars(find_all_sql)
        async for row in stream:
            yield row

    async def find_by_id(self, model_id: UUID) -> ModelType:
        find_by_id = select(self.model_type).where(self.model_type.id == model_id)
        return await self.session.scalar(find_by_id)

    async def add_one(self, model: ModelType) -> ModelType:
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model
