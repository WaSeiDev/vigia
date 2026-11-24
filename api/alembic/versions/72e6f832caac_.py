"""empty message

Revision ID: 72e6f832caac
Revises: a6d6d04a25c4
Create Date: 2026-11-24 21:15:35.912831

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72e6f832caac'
down_revision: Union[str, Sequence[str], None] = 'a6d6d04a25c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
