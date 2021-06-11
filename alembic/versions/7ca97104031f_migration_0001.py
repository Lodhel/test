"""migration_0001

Revision ID: 7ca97104031f
Revises: 
Create Date: 2021-06-11 19:19:34.226377

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision = '7ca97104031f'
down_revision = None
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
