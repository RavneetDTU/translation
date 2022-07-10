"""add new ukrainian model

Revision ID: c4e09745fd6e
Revises: cdae055766f9
Create Date: 2022-07-11 00:22:42.429720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4e09745fd6e'
down_revision = 'cdae055766f9'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'uk', 'translate.en_uk');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('uk', 'en', 'translate.uk_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('uk', 'Це тест.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='uk';""")
    op.execute("""DELETE FROM translation_handler where input_language='uk' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='uk';""")

