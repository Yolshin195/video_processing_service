from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EntityModel(BaseModel):
    id: UUID


class ReferenceModel(EntityModel):
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True)


class FileModel(EntityModel):
    file_id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class TaskModel(EntityModel):
    status: ReferenceModel
    type: ReferenceModel
    file_source_url: Optional[str]
    input_file: Optional[FileModel]
    output_file: Optional[FileModel]

    model_config = ConfigDict(from_attributes=True)


class HandleYoutubeVideo(BaseModel):
    url: str


class HandleTorrentFileVideo(BaseModel):
    torrent_file: FileModel


class HandleCustomUserVideo(BaseModel):
    user_video: FileModel
