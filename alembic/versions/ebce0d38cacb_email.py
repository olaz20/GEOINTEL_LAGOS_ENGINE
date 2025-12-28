"""email

Revision ID: ebce0d38cacb
Revises: 1a5dce431497
Create Date: 2025-12-28 11:43:04.705895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ebce0d38cacb'
down_revision: Union[str, Sequence[str], None] = '1a5dce431497'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
