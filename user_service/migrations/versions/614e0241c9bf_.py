"""empty message

Revision ID: 614e0241c9bf
Revises: 
Create Date: 2023-11-04 11:08:33.779912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '614e0241c9bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('date_birth', sa.String(length=10), nullable=True),
    sa.Column('customer_type', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('token', sa.String(length=256), nullable=True),
    sa.Column('token_issue_time', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###