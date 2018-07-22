"""add field in tokens model

Revision ID: c7a6e9d8bffc
Revises: db4e3b8eb160
Create Date: 2018-07-21 20:53:04.138561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a6e9d8bffc'
down_revision = 'db4e3b8eb160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tokens_Reset_Password', sa.Column('was_used', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Tokens_Reset_Password', 'was_used')
    # ### end Alembic commands ###
