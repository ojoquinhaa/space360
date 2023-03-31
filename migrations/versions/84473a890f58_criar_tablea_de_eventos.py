"""Criar tablea de eventos

Revision ID: 84473a890f58
Revises: 
Create Date: 2023-03-30 18:54:19.118407

"""
from alembic import op
from sqlalchemy import Column, Integer, String, Boolean
from cam360.connection.models import Event


# revision identifiers, used by Alembic.
revision = '84473a890f58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(Event.__tablename__,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String(100)),
        Column('speedSet', Integer),
        Column('recordingTime', Integer),
        Column('frame', String(100)),
        Column('music', String(100)),
        Column('reverse', Boolean),
        Column('iniImage',String(100)),
        Column('finImage',String(100)),
        Column('owner', Integer)
    )

def downgrade():
    op.drop_table(Event.__tablename__)