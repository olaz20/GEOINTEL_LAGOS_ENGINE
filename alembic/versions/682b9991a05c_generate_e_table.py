"""generate e table

Revision ID: 682b9991a05c
Revises: b7aab341618c
Create Date: 2025-12-28 05:23:24.191740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '682b9991a05c'
down_revision: Union[str, Sequence[str], None] = 'b7aab341618c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
