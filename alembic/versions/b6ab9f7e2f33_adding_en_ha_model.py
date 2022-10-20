"""adding en ha model

Revision ID: b6ab9f7e2f33
Revises: 1b785034decc
Create Date: 2022-10-20 03:03:29.353944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6ab9f7e2f33'
down_revision = '1b785034decc'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ga', 'translate.en_ga');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ga', 'en', 'translate.ga_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ga', 'Is tástáil é seo.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ga';""")
    op.execute("""DELETE FROM translation_handler where input_language='ga' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='ga';""")
