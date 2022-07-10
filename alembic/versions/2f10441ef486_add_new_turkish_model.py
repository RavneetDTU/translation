"""add new turkish model

Revision ID: 2f10441ef486
Revises: c4e09745fd6e
Create Date: 2022-07-11 00:34:42.004725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f10441ef486'
down_revision = 'c4e09745fd6e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'tr', 'translate.en_tr');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('tr', 'en', 'translate.tr_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('tr', 'Bu bir test.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='tr';""")
    op.execute("""DELETE FROM translation_handler where input_language='tr' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='tr';""")
