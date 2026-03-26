"""test

Revision ID: 325d3ccf94ad
Revises: 75fa2d5fc577
Create Date: 2026-03-26 22:52:08.810922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '325d3ccf94ad'
down_revision: Union[str, Sequence[str], None] = '75fa2d5fc577'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
