"""generate a table

Revision ID: 1a5dce431497
Revises: 682b9991a05c
Create Date: 2025-12-28 11:34:01.402354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a5dce431497'
down_revision: Union[str, Sequence[str], None] = '682b9991a05c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
