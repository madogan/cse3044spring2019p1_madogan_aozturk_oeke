"""trivial2

Revision ID: 191b892bb787
Revises: 0ced75605320
Create Date: 2019-06-18 03:20:54.931275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '191b892bb787'
down_revision = '0ced75605320'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('asker_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'asker_name')
    # ### end Alembic commands ###