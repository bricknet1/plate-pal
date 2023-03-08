"""add instructions to recipe

Revision ID: 43c1198ea6d7
Revises: f5c23f973d7d
Create Date: 2023-03-08 08:14:21.044701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43c1198ea6d7'
down_revision = 'f5c23f973d7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('instructions', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'instructions')
    # ### end Alembic commands ###
