"""empty message

Revision ID: bdfcbaf0d683
Revises: e8fc970c97ac
Create Date: 2021-04-25 01:31:11.409936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdfcbaf0d683'
down_revision = 'e8fc970c97ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visitors',
    sa.Column('v_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('facemask_check', sa.Integer(), nullable=False),
    sa.Column('visitor_name', sa.String(length=255), nullable=False),
    sa.Column('visitor_id', sa.Integer(), nullable=False),
    sa.Column('visitor_temp', sa.Numeric(), nullable=False),
    sa.Column('temp_check', sa.Integer(), nullable=False),
    sa.Column('check_in', sa.Integer(), nullable=False),
    sa.Column('visit_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.venue_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('v_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visitors')
    # ### end Alembic commands ###
