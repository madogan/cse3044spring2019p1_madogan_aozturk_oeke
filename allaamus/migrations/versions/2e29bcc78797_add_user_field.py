""" add user field.

Revision ID: 2e29bcc78797
Revises: 0f29cb613f32
Create Date: 2019-06-18 01:23:04.482646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e29bcc78797'
down_revision = '0f29cb613f32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about', sa.String(), nullable=True))
    op.add_column('user', sa.Column('job', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'job')
    op.drop_column('user', 'about')
    # ### end Alembic commands ###
