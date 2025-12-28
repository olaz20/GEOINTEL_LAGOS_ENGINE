"""generate iniatial  table

Revision ID: f05dcd78778b
Revises: 70feeb93fbf4
Create Date: 2025-12-28 05:10:58.399982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f05dcd78778b'
down_revision: Union[str, Sequence[str], None] = '70feeb93fbf4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
