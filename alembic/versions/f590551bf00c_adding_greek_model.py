"""adding greek model

Revision ID: f590551bf00c
Revises: d6432c67fc59
Create Date: 2022-08-09 07:43:57.364382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f590551bf00c'
down_revision = 'd6432c67fc59'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'el', 'translate.en_el');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('el', 'en', 'translate.el_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('el', 'This is a test in greek.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='el';""")
    op.execute("""DELETE FROM translation_handler where input_language='el' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='el';""")

