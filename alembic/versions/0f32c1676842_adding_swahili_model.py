"""adding swahili model

Revision ID: 0f32c1676842
Revises: ca92cd3fff98
Create Date: 2022-04-16 11:17:48.019970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f32c1676842'
down_revision = 'ca92cd3fff98'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'sw', 'translate.en_sw');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('sw', 'en', 'translate.sw_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('sw', 'Huu ni mtihani.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='sw';""")
    op.execute("""DELETE FROM translation_handler where input_language='sw' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='sw';""")
