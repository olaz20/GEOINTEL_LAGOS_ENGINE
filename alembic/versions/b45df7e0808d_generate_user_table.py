"""generate user table

Revision ID: b45df7e0808d
Revises: b1ece41e8ef2
Create Date: 2025-12-28 05:00:01.027068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b45df7e0808d'
down_revision: Union[str, Sequence[str], None] = 'b1ece41e8ef2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
