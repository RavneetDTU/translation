"""add new arabic model

Revision ID: cdae055766f9
Revises: d52e55cd3829
Create Date: 2022-07-11 00:07:30.738178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdae055766f9'
down_revision = 'd52e55cd3829'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ar', 'translate.en_ar');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ar', 'en', 'translate.ar_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ar', 'sample_text');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ar';""")
    op.execute("""DELETE FROM translation_handler where input_language='ar' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='ar';""")

