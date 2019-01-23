"""add column in Users

Revision ID: 68c6d4e55ed2
Revises: 7071662e1d4c
Create Date: 2019-01-10 21:30:06.265797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68c6d4e55ed2'
down_revision = '7071662e1d4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('count_logins_failed', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'count_logins_failed')
    # ### end Alembic commands ###
