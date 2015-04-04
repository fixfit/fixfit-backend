"""Add user table

Revision ID: 7c1369b5beb
Revises: None
Create Date: 2015-04-04 15:46:48.430467

"""

# revision identifiers, used by Alembic.
revision = '7c1369b5beb'
down_revision = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=64), nullable=True),
        sa.Column('last_name', sa.String(length=64), nullable=True),
        sa.Column('email', sa.String(length=254), nullable=True),
        sa.Column('password', sa.String(length=128), nullable=True),
        sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=True),
        sa.Column('address', sa.String(length=64), nullable=True),
        sa.Column('profile_pic', sa.String(length=256), nullable=True),
        sa.Column('current_card_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_user_email'), 'user', ['email'], unique=True
    )


def downgrade():
    op.create_table(
        'user',
        )
