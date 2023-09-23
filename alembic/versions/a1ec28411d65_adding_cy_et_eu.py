"""Adding cy et eu

Revision ID: a1ec28411d65
Revises: 2306a19c3724
Create Date: 2023-09-24 04:08:13.350094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1ec28411d65'
down_revision = '2306a19c3724'
branch_labels = None
depends_on = None


def upgrade():
    # For cy:
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'cy', 'translate.en_cy');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('cy', 'en', 'translate.cy_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('cy', 'Prawf yw hwn.');""")
    # For et:
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'et', 'translate.en_et');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('et', 'en', 'translate.et_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('et', 'See on test.');""")
    # For eu:
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'eu', 'translate.en_eu');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('eu', 'en', 'translate.eu_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('eu', 'Hau proba bat da.');""")


def downgrade():
    # For cy:
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='cy';""")
    op.execute("""DELETE FROM translation_handler where input_language='cy' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='cy';""")
    # For et:
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='et';""")
    op.execute("""DELETE FROM translation_handler where input_language='et' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='et';""")
    # For eu:
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='eu';""")
    op.execute("""DELETE FROM translation_handler where input_language='eu' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='eu';""")
