"""empty message

Revision ID: bc3adba1f02d
Revises: 
Create Date: 2023-10-27 18:11:51.614860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc3adba1f02d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('delivery_adress', sa.String(length=256), nullable=True),
    sa.Column('order_status', sa.String(length=256), nullable=True),
    sa.Column('order_comment', sa.String(length=256), nullable=True),
    sa.Column('promocode', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###
