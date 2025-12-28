"""admin

Revision ID: 783788a81413
Revises: ebce0d38cacb
Create Date: 2025-12-28 11:44:13.081231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '783788a81413'
down_revision: Union[str, Sequence[str], None] = 'ebce0d38cacb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
