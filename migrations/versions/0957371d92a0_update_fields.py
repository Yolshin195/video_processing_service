"""update fields

Revision ID: 0957371d92a0
Revises: 860a77f75b89
Create Date: 2023-12-17 13:33:00.627332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0957371d92a0'
down_revision: Union[str, None] = '860a77f75b89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task_entity', 'input_file_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('task_entity', 'output_file_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task_entity', 'output_file_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('task_entity', 'input_file_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###