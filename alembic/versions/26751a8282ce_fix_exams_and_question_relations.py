"""fix exams and question relations

Revision ID: 26751a8282ce
Revises: 50ebeba79eea
Create Date: 2021-12-06 04:43:39.957100

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '26751a8282ce'
down_revision = '50ebeba79eea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'course_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
