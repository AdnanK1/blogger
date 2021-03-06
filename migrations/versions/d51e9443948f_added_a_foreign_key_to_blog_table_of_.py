"""Added a foreign key to blog table of comments table

Revision ID: d51e9443948f
Revises: 10c65edf14da
Create Date: 2022-05-16 15:55:22.002296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd51e9443948f'
down_revision = '10c65edf14da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blogs', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'comments', ['blogs'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'blogs')
    # ### end Alembic commands ###
