"""generate  table

Revision ID: 70feeb93fbf4
Revises: b45df7e0808d
Create Date: 2025-12-28 05:07:26.170757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70feeb93fbf4'
down_revision: Union[str, Sequence[str], None] = 'b45df7e0808d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
