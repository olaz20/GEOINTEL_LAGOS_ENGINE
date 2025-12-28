"""create user table

Revision ID: b1ece41e8ef2
Revises: 57ced9d7da86
Create Date: 2025-12-28 04:55:54.713668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1ece41e8ef2'
down_revision: Union[str, Sequence[str], None] = '57ced9d7da86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
