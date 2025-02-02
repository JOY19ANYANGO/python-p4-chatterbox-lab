"""your message

Revision ID: 34d46aa029e8
Revises: 0e12555d4c52
Create Date: 2023-09-21 23:34:11.238006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34d46aa029e8'
down_revision = '0e12555d4c52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
