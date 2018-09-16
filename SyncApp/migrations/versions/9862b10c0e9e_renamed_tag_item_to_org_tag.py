"""renamed tag_item to org_tag

Revision ID: 9862b10c0e9e
Revises: 6c031f947c66
Create Date: 2018-09-15 18:16:24.596641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9862b10c0e9e'
down_revision = '6c031f947c66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_item')
    op.create_table('org_tag',
    sa.Column('org_tag_id', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['org_id'], ['organization.org_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.tag_id'], ),
    sa.PrimaryKeyConstraint('org_tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('org_tag')
    op.create_table('tag_item',
    sa.Column('tag_item_id', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['org_id'], ['organization.org_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.tag_id'], ),
    sa.PrimaryKeyConstraint('tag_item_id')
    )
    # ### end Alembic commands ###
