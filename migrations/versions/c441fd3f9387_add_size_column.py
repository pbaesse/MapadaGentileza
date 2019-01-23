"""add size column

Revision ID: c441fd3f9387
Revises: 2920eeb413b3
Create Date: 2019-01-10 23:26:04.195534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c441fd3f9387'
down_revision = '2920eeb413b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Kindness_Files', sa.Column('size', sa.LargeBinary(), nullable=True))
    op.drop_column('Kindness_Files', 'file_size')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Kindness_Files', sa.Column('file_size', mysql.FLOAT(), nullable=True))
    op.drop_column('Kindness_Files', 'size')
    # ### end Alembic commands ###