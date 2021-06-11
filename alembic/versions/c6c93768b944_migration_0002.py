"""migration_0002

Revision ID: c6c93768b944
Revises: 7ca97104031f
Create Date: 2021-06-11 20:18:39.774010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6c93768b944'
down_revision = '7ca97104031f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'url_information',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('url', sa.Text(), nullable=False, unique=True),
        sa.Column('data', sa.Text())
    )


def downgrade():
    pass
