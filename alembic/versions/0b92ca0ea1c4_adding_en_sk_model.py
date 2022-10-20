"""adding en sk model

Revision ID: 0b92ca0ea1c4
Revises: ff08937304ad
Create Date: 2022-10-20 03:13:01.930475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b92ca0ea1c4'
down_revision = 'ff08937304ad'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'sk', 'translate.en_sk');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('sk', 'en', 'translate.sk_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('sk', 'Toto je test.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='sk';""")
    op.execute("""DELETE FROM translation_handler where input_language='sk' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='sk';""")
