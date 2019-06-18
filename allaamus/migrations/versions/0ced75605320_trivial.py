"""trivial

Revision ID: 0ced75605320
Revises: 2e29bcc78797
Create Date: 2019-06-18 02:30:52.258532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ced75605320'
down_revision = '2e29bcc78797'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('topic', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'topic')
    # ### end Alembic commands ###