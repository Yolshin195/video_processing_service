from enum import Enum


class StatusEnum(Enum):
    CREATED = "created"
    STARTED_DOWNLOADING = "started_downloading"
    FINISHED_DOWNLOADING = "finished_downloading"
    STARTED_PROCESSING = "started_processing"
    FINISHED_PROCESSING = "finished_processing"
    ERROR = "error"
    COMPLETED = "completed"


class TypeEnum(Enum):
    CUSTOM = "custom"
    YOUTUBE = "youtube"
    TORRENT = "torrent"
