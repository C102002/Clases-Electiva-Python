"""create users table

Revision ID: e9f6585b8206
Revises: a2212016ece6
Create Date: 2025-07-01 00:17:23.697511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel                    


# revision identifiers, used by Alembic.
revision: str = 'e9f6585b8206'
down_revision: Union[str, None] = 'a2212016ece6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('surname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('birthday', sa.DATE(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
