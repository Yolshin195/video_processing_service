from typing import AsyncIterator
from uuid import UUID

from .constants import StatusEnum, TypeEnum
from .entities import TaskEntity, StatusEntity, TypeEntity
from .mappers import task_mapper, face_task_mapper
from .models import (
    TaskModel,
    HandleYoutubeVideo,
    HandleTorrentFileVideo,
    HandleCustomUserVideo,
)
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
        return task_mapper(await self.repository.find_by_id(task_id))

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
        return task_mapper(await self.repository.add_one(new_task))

    def handle_torrent_file_video(self, event: HandleTorrentFileVideo) -> TaskModel:
        return face_task_mapper(
            StatusEnum.CREATED, TypeEnum.TORRENT, event.torrent_file
        )

    def handle_custom_user_video(self, event: HandleCustomUserVideo) -> TaskModel:
        return face_task_mapper(StatusEnum.CREATED, TypeEnum.CUSTOM, event.user_video)
