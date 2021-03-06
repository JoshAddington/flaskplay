"""empty message

Revision ID: 4e14d364e07
Revises: None
Create Date: 2015-03-25 17:56:07.661441

"""

# revision identifiers, used by Alembic.
revision = '4e14d364e07'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stations',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.Column('number_of_bikes', sa.Integer(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bikes')
    op.drop_table('stations')
    ### end Alembic commands ###
