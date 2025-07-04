"""first tables

Revision ID: 38b6341a9c06
Revises: 
Create Date: 2024-12-11 20:41:18.059491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel                    


# revision identifiers, used by Alembic.
revision: str = '38b6341a9c06'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def create_authors_table():
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('nationality', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    create_authors_table()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authors')
    # ### end Alembic commands ###
