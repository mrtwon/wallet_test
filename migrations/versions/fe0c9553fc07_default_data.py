"""default_data

Revision ID: fe0c9553fc07
Revises: 77fc3697aee2
Create Date: 2025-03-20 11:08:35.786822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'fe0c9553fc07'
down_revision: Union[str, None] = '0667837e40cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO status VALUES ('CREATE')
    """)
    op.execute("""
        INSERT INTO status VALUES ('PENDING')
    """)
    op.execute("""
            INSERT INTO status VALUES ('CONFIRM')
        """)
    op.execute("""
            INSERT INTO status VALUES ('CANCEL')
        """)

    op.execute("""
            INSERT INTO operation VALUES ('DEPOSIT')
        """)
    op.execute("""
            INSERT INTO operation VALUES ('WITHDRAW')
        """)


def downgrade() -> None:
    op.execute('DELETE FROM operation')
    op.execute('DELETE FROM status')
