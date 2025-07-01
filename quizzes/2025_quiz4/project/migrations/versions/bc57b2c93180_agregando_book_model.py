"""Agregando Book Model

Revision ID: bc57b2c93180
Revises: 38b6341a9c06
Create Date: 2025-06-10 13:14:42.181997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel                    


# revision identifiers, used by Alembic.
revision: str = 'bc57b2c93180'
down_revision: Union[str, None] = '38b6341a9c06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('books',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column("author_id", sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(
    ['author_id'],      # Columna(s) en la tabla que se está creando
    ['authors.id'], # Columna(s) en la tabla referenciada
    name='books_authors_table',
    ondelete='CASCADE')
    )                    # Comportamiento al eliminar el padre


def downgrade() -> None:
    op.drop_table('books')
