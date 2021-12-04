"""add status helpers

Revision ID: a5f2b6bf88e6
Revises: b07981abb72b
Create Date: 2021-12-05 01:21:38.388535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5f2b6bf88e6'
down_revision = 'b07981abb72b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO status_helper (input_language, sample_text) VALUES ('en', 'this is test');""")
    op.execute("""INSERT INTO status_helper (input_language, sample_text) VALUES ('fr', 'ceci est l&apos; essai');""")
    op.execute("""INSERT INTO status_helper (input_language, sample_text) VALUES ('es', 'el nuevo ensayo');""")


def downgrade():
    op.execute("""DELETE FROM status_helper where input_language='en';""")
    op.execute("""DELETE FROM status_helper where input_language='fr';""")
    op.execute("""DELETE FROM status_helper where input_language='es';""")
