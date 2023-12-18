from uuid import UUID

from .constants import StatusEnum, TypeEnum
from .entities import TaskEntity
from .models import TaskModel, HandleYoutubeVideo
from .repositories import TaskRepository, StatusRepository, TypeRepository
from core import BaseService


class TaskService(BaseService):
    def __init__post__(self):
        self.repository = TaskRepository(self.session)
        self.status_repository = StatusRepository(self.session)
        self.type_repository = TypeRepository(self.session)

    async def find_all(self, skip: int = 0, limit: int = 100) -> list[TaskModel]:
        return [
            TaskModel.model_validate(entity)
            async for entity in self.repository.find_all(skip, limit)
        ]

    async def find_by_id(self, task_id: UUID) -> TaskModel:
        return TaskModel.model_validate(await self.repository.find_by_id(task_id))

    async def handle_youtube_video(self, event: HandleYoutubeVideo) -> TaskModel:
        current_status = await self.status_repository.find_by_code(
            StatusEnum.CREATED.value
        )
        current_type = await self.type_repository.find_by_code(TypeEnum.YOUTUBE.value)
        new_task = TaskEntity(
            status_id=current_status.id,
            type_id=current_type.id,
            file_source_url=event.url,
        )
        return TaskModel.model_validate(await self.repository.add_one(new_task))
