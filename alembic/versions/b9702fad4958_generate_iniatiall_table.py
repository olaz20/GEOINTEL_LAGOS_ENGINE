"""generate iniatialL  table

Revision ID: b9702fad4958
Revises: f05dcd78778b
Create Date: 2025-12-28 05:19:37.599859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9702fad4958'
down_revision: Union[str, Sequence[str], None] = 'f05dcd78778b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
