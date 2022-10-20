"""adding en fa model

Revision ID: ff08937304ad
Revises: b6ab9f7e2f33
Create Date: 2022-10-20 03:09:08.455473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff08937304ad'
down_revision = 'b6ab9f7e2f33'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'fa', 'translate.en_fa');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('fa', 'en', 'translate.fa_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('fa', 'Persian Test.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='fa';""")
    op.execute("""DELETE FROM translation_handler where input_language='fa' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='fa';""")
