"""generate first table

Revision ID: b7aab341618c
Revises: b9702fad4958
Create Date: 2025-12-28 05:20:44.036138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7aab341618c'
down_revision: Union[str, Sequence[str], None] = 'b9702fad4958'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
