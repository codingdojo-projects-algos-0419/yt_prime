"""empty message

Revision ID: 71525d4f093a
Revises: e0152c53a368
Create Date: 2019-04-13 15:34:44.412645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71525d4f093a'
down_revision = 'e0152c53a368'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photos', sa.Column('created_at', sa.Date(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.drop_column('photos', 'create_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('photos', sa.Column('create_at', sa.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.drop_column('photos', 'created_at')
    # ### end Alembic commands ###