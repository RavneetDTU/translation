"""adding af in language_helper table

Revision ID: 5b875c45684a
Revises: 4b7bb8fbcfb6
Create Date: 2022-03-25 00:37:12.458857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b875c45684a'
down_revision = '4b7bb8fbcfb6'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('af', 'Hierdie is n toets');""")

def downgrade():
    op.execute("""DELETE FROM language_helper where language='af';""")
