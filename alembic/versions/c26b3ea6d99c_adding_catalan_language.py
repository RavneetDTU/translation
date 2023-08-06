"""Adding Catalan language

Revision ID: c26b3ea6d99c
Revises: 0b92ca0ea1c4
Create Date: 2023-08-06 10:00:02.591456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c26b3ea6d99c'
down_revision = '0b92ca0ea1c4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ca', 'translate.en_ca');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ca', 'en', 'translate.ca_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ca', 'Això és un test.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ca';""")
    op.execute("""DELETE FROM translation_handler where input_language='ca' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='ca';""")
