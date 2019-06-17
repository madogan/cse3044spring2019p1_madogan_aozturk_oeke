"""remove user_type

Revision ID: 17f5d0adbc52
Revises: 6e6de43cd617
Create Date: 2019-06-17 17:32:37.429446

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '17f5d0adbc52'
down_revision = '6e6de43cd617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('first_name', sa.String(length=24), nullable=False),
    sa.Column('last_name', sa.String(length=24), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('register_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.drop_index('ix_article_id', table_name='article')
    op.drop_table('article')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('source', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('tags', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='article_pkey')
    )
    op.create_index('ix_article_id', 'article', ['id'], unique=False)
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###