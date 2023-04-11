"""Alterações na tabela

Revision ID: 2ca1bf7637eb
Revises: 
Create Date: 2023-04-10 17:16:45.981440

"""
from alembic import op
import sqlalchemy as sa
from app.models.event import Event

# revision identifiers, used by Alembic.
revision = '2ca1bf7637eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        Event.__tablename__,
        sa.Column('id',sa.Integer(),nullable=False,primary_key=True,autoincrement=True),
        sa.Column('owner',sa.Integer(),nullable=False),
        sa.Column('name',sa.String(255),nullable=False),
        sa.Column('speedSet',sa.Integer(),nullable=False),
        sa.Column('recordingTime',sa.Integer(),nullable=False),
        sa.Column('frame',sa.Text(),nullable=True),
        sa.Column('iniImage',sa.Text(),nullable=True),
        sa.Column('finImage',sa.Text(),nullable=True),
        sa.Column('music',sa.Text(),nullable=True),
        sa.Column('reverse',sa.Boolean(),nullable=False)
    )


def downgrade() -> None:
    op.drop_table(Event.__tablename__)
