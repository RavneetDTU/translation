"""adding en hu model

Revision ID: 1b785034decc
Revises: b8e78c310b97
Create Date: 2022-10-20 02:58:12.443812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b785034decc'
down_revision = 'b8e78c310b97'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'hu', 'translate.en_hu');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('hu', 'en', 'translate.hu_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('hu', 'Ez egy teszt.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='hu';""")
    op.execute("""DELETE FROM translation_handler where input_language='hu' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='hu';""")
