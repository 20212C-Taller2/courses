"""add exams to courses

Revision ID: 50ebeba79eea
Revises: 33609684dfab
Create Date: 2021-12-02 02:38:20.285937

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '50ebeba79eea'
down_revision = '33609684dfab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courses', 'exams')

    op.create_table('exams',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('course_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('questions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('course_id', sa.Integer(), nullable=False),
                    sa.Column('exam_id', sa.Integer(), nullable=True),
                    sa.Column('number', sa.Integer(), nullable=False),
                    sa.Column('text', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', 'exams')
    op.drop_table('questions')
    op.drop_table('exams')
    # ### end Alembic commands ###
