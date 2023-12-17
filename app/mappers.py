from app.constants import StatusEnum, TypeEnum
from app.entities import FileEntity, TaskEntity
from app.models import ReferenceModel, FileModel, TaskModel
from core import BaseReferenceEntity


def reference_mapper(reference: BaseReferenceEntity) -> ReferenceModel:
    return ReferenceModel(
        code=reference.code,
        name=reference.name
    )


def file_mapper(file_entity: FileEntity) -> FileModel | None:
    return FileModel(
        file_id=file_entity.id,
        name=file_entity.name
    ) if file_entity else None


def task_mapper(task_entity: TaskEntity) -> TaskModel:
    return TaskModel(
        status=reference_mapper(task_entity.status),
        type=reference_mapper(task_entity.type),
        file_source_url=task_entity.file_source_url,
        input_file=file_mapper(task_entity.input_file),
        output_file=file_mapper(task_entity.output_file)
    )


def face_task_mapper(status: StatusEnum, type: TypeEnum, source_file: FileModel) -> TaskModel:
    return TaskModel(
        status=ReferenceModel(
            code=status.value,
            name=status.value
        ),
        type=ReferenceModel(
            code=type.value,
            name=type.value
        ),
        source_file=source_file,
        file_source_url=None,
        input_file=None,
        output_file=None,
    )
