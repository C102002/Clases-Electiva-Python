"""migracion base

Revision ID: 9db22ac78189
Revises: 
Create Date: 2024-11-20 16:02:36.750797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel                    


# revision identifiers, used by Alembic.
revision: str = '9db22ac78189'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
