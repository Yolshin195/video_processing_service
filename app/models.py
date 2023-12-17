from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ReferenceModel(BaseModel):
    code: str
    name: str


class FileModel(BaseModel):
    file_id: UUID
    name: str


class TaskModel(BaseModel):
    status: ReferenceModel
    type: ReferenceModel
    file_source_url: Optional[str]
    source_file: Optional[FileModel]
    input_file: Optional[FileModel]
    output_file: Optional[FileModel]


class HandleYoutubeVideo(BaseModel):
    url: str


class HandleTorrentFileVideo(BaseModel):
    torrent_file: FileModel


class HandleCustomUserVideo(BaseModel):
    user_video: FileModel
