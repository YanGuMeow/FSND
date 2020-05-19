"""empty message

Revision ID: afaf401040ed
Revises: 5d12a4c5f7d3
Create Date: 2020-05-18 18:35:19.520637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afaf401040ed'
down_revision = '5d12a4c5f7d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('venue', 'upcoming_shows_count')
    op.drop_column('venue', 'past_shows_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('artist', 'website_link')
    op.drop_column('artist', 'seeking_venue')
    op.drop_column('artist', 'seeking_description')
    op.drop_table('show')
    # ### end Alembic commands ###
