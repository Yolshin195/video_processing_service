from fastapi import APIRouter, Depends

from app.models import TaskModel, HandleYoutubeVideo
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
