"""add language helpers

Revision ID: 2eef5020a22f
Revises: 916fb0b72d80
Create Date: 2021-12-19 00:54:38.854084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eef5020a22f'
down_revision = '916fb0b72d80'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('en', 'this is test');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('fr', 'ceci est l&apos; essai');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('es', 'el nuevo ensayo');""")


def downgrade():
    op.execute("""DELETE FROM language_helper where language='en';""")
    op.execute("""DELETE FROM language_helper where language='fr';""")
    op.execute("""DELETE FROM language_helper where language='es';""")
