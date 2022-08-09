"""adding fi model

Revision ID: d6432c67fc59
Revises: ac9213272811
Create Date: 2022-08-09 07:41:37.879125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6432c67fc59'
down_revision = 'ac9213272811'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'fi', 'translate.en_fi');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('fi', 'en', 'translate.fi_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('fi', 'Tämä on testi.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='fi';""")
    op.execute("""DELETE FROM translation_handler where input_language='fi' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='fi';""")
