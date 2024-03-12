"""empty message

Revision ID: 137a4b059889
Revises: 2200efe10f98
Create Date: 2024-03-12 16:25:00.251292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137a4b059889'
down_revision = '2200efe10f98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
