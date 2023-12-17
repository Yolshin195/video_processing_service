"""init reference

Revision ID: 860a77f75b89
Revises: 1959c5727c8e
Create Date: 2023-12-17 12:55:15.552356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.constants import TypeEnum, StatusEnum
from app.entities import TypeEntity, StatusEntity

# revision identifiers, used by Alembic.
revision: str = '860a77f75b89'
down_revision: Union[str, None] = '1959c5727c8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.add_all([
        StatusEntity(
            code=status_enum.value,
            name=status_enum.value
        )
        for status_enum in StatusEnum
    ])
    session.commit()

    session = Session(bind=op.get_bind())
    session.add_all([
        TypeEntity(
            code=type_enum.value,
            name=type_enum.value
        )
        for type_enum in TypeEnum
    ])
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())

    delete_status_entity_sql = delete(StatusEntity).where(StatusEntity.code.in_([
        status_enum.value for status_enum in StatusEnum
    ]))
    session.execute(delete_status_entity_sql)

    delete_type_entity_sql = delete(TypeEntity).where(TypeEntity.code.in_([
        type_enum.value for type_enum in TypeEnum
    ]))
    session.execute(delete_type_entity_sql)

    session.commit()
