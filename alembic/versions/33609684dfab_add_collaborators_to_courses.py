"""add collaborators to courses

Revision ID: 33609684dfab
Revises: 49b9307f5af8
Create Date: 2021-11-28 17:10:17.760833

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '33609684dfab'
down_revision = '49b9307f5af8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collaborators',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id', 'course_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collaborators')
    # ### end Alembic commands ###
