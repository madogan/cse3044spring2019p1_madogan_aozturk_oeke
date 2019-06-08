"""first migration

Revision ID: 6e6de43cd617
Revises: 
Create Date: 2019-06-08 13:54:29.946329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e6de43cd617'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('category', sa.Enum('eğitim', 'teknoloji', 'psikoloji', name='article_categories'), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('tags', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_article_id'), 'article', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('first_name', sa.String(length=24), nullable=False),
    sa.Column('last_name', sa.String(length=24), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('user_type', sa.Enum('meraklı', 'usta', name='user_types'), nullable=True),
    sa.Column('register_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.drop_table('mobile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mobile',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('model', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('price', sa.REAL(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='mobile_pkey')
    )
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_article_id'), table_name='article')
    op.drop_table('article')
    # ### end Alembic commands ###
