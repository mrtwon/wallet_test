"""empty message

Revision ID: 0667837e40cf
Revises: 
Create Date: 2025-03-20 15:10:00.810962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0667837e40cf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('operation_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('operation_id'),
    sa.UniqueConstraint('operation_id')
    )
    op.create_table('status',
    sa.Column('status_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('status_id'),
    sa.UniqueConstraint('status_id')
    )
    op.create_table('wallet',
    sa.Column('wallet_id', sa.UUID(), nullable=False),
    sa.Column('wallet_balance', sa.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('wallet_id'),
    sa.UniqueConstraint('wallet_id')
    )
    op.create_table('wallet_operation',
    sa.Column('wallet_operation_id', sa.UUID(), nullable=False),
    sa.Column('operation_id', sa.String(), nullable=True),
    sa.Column('status_id', sa.String(), nullable=True),
    sa.Column('wallet_id', sa.UUID(), nullable=True),
    sa.Column('amount', sa.FLOAT(), nullable=False),
    sa.Column('create_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('update_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['operation_id'], ['operation.operation_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.status_id'], ),
    sa.ForeignKeyConstraint(['wallet_id'], ['wallet.wallet_id'], ),
    sa.PrimaryKeyConstraint('wallet_operation_id'),
    sa.UniqueConstraint('wallet_operation_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet_operation')
    op.drop_table('wallet')
    op.drop_table('status')
    op.drop_table('operation')
    # ### end Alembic commands ###
