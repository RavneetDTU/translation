"""adding af into language_helper table

Revision ID: ca92cd3fff98
Revises: 5b875c45684a
Create Date: 2022-03-25 01:12:42.701623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca92cd3fff98'
down_revision = '5b875c45684a'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('af', 'Hierdie is n toets');""")


def downgrade():
    op.execute("""DELETE FROM language_helper where language='af';""")
