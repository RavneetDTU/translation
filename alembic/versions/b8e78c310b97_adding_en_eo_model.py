"""adding en eo model

Revision ID: b8e78c310b97
Revises: f590551bf00c
Create Date: 2022-10-20 02:52:09.358963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8e78c310b97'
down_revision = 'f590551bf00c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'eo', 'translate.en_eo');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('eo', 'en', 'translate.eo_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('eo', 'Ĉi tio estas testo.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='eo';""")
    op.execute("""DELETE FROM translation_handler where input_language='eo' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='eo';""")

