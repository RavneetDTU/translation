"""Adding CZ

Revision ID: ac9213272811
Revises: 55a71b4c45e4
Create Date: 2022-08-09 07:35:29.099841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac9213272811'
down_revision = '55a71b4c45e4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'cz', 'translate.en_cz');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('cz', 'en', 'translate.cz_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('cz', 'Tohle je zkouška.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='cz';""")
    op.execute("""DELETE FROM translation_handler where input_language='cz' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='cz';""")
