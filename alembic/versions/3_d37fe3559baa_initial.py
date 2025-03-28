"""initial

Revision ID: d37fe3559baa
Revises: 3758ed417f58
Create Date: 2025-03-23 15:39:54.348683

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d37fe3559baa"
down_revision: Union[str, None] = "3758ed417f58"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("api_token", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "api_token")
    # ### end Alembic commands ###
