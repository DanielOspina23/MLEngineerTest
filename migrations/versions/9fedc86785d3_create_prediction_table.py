"""create prediction table

Revision ID: 9fedc86785d3
Revises: 
Create Date: 2020-10-23 10:24:55.481401

"""
from alembic import op
import sqlalchemy as sa
import datetime as dt


# revision identifiers, used by Alembic.
revision = '9fedc86785d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'taken_order',
        sa.Column('id', sa.BigInteger, primary_key=True, unique=True, index=True),
        sa.Column('order_id', sa.BigInteger, nullable=False),
        sa.Column('store_id', sa.BigInteger, nullable=False),
        sa.Column('to_user_distance', sa.Float, nullable=False),
        sa.Column('to_user_elevation', sa.Float, nullable=False),
        sa.Column('total_earning', sa.Integer, nullable=False),
        sa.Column('order_date', sa.DateTime, nullable=False),
        sa.Column('taken_probability', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, default=dt.datetime.utcnow)
    )


def downgrade():
    op.drop_table('taken_order')
