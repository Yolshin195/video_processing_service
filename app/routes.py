from fastapi import APIRouter, Depends

from app.models import (
    TaskModel,
    HandleYoutubeVideo,
    HandleTorrentFileVideo,
    HandleCustomUserVideo,
)
from app.services import TaskService

task_router = APIRouter(prefix="/task", tags=["Task"])


@task_router.get("/all")
async def find_all_task(
    skip: int = 0, limit: int = 100, task_service: TaskService = Depends()
) -> list[TaskModel]:
    return await task_service.find_all(skip, limit)


@task_router.post("/handle/youtube")
async def handle_youtube_video(
    event: HandleYoutubeVideo, task_service: TaskService = Depends()
) -> TaskModel:
    return await task_service.handle_youtube_video(event)


@task_router.post("/handle/torrent")
async def handle_torrent_file_video(
    event: HandleTorrentFileVideo, task_service: TaskService = Depends()
) -> TaskModel:
    return task_service.handle_torrent_file_video(event)


@task_router.post("/handle/custom")
async def handle_custom_user_video(
    event: HandleCustomUserVideo, task_service: TaskService = Depends()
) -> TaskModel:
    return task_service.handle_custom_user_video(event)
